from confluent_kafka import Consumer, KafkaException, KafkaError

# Configuration du Consumer
conf = {
    'bootstrap.servers': 'localhost:9092',  # Adresse du broker Kafka
    'group.id': 'mon-consumer-group',       # ID du groupe de consumers
    'auto.offset.reset': 'earliest'         # Commencer à lire depuis le début si aucun offset n'est trouvé
}

# Création du Consumer
consumer = Consumer(conf)

# S'abonner au topic
topic = 'my_topic'  # Remplace par le nom de ton topic
consumer.subscribe([topic])

try:
    while True:
        # Lire un message avec un timeout de 1 seconde
        msg = consumer.poll(1.0)
        
        # Vérifier si un message a été reçu
        if msg is None:
            print("Aucun message reçu.")
            continue
        if msg.error():
            # Vérifier si une erreur de partition est survenue
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print(f"Fin de partition {msg.partition} atteinte à l'offset {msg.offset}")
            else:
                raise KafkaException(msg.error())
        
        # Afficher le message reçu
        print(f"Message reçu : {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    print("Arrêt du consumer.")

finally:
    # Fermeture propre du consumer
    consumer.close()
