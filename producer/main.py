import json
import time
from kafka import KafkaProducer

# Configuration du producteur Kafka
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

# Création d'une instance de producteur Kafka
producer = KafkaProducer(servers=conf['bootstrap.servers'], client_id=conf['client.id'])

# Fonction de callback pour la livraison du message
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic} [{msg.partition}] at offset {msg.offset}")

# Données à envoyer
data = {
    "name": "Maxence",
    "age": 30,
    "is_student": False
}

# Intervalle en secondes (par exemple, envoyer toutes les 5 secondes)
N = 5
topic = 'my_topic'  # Nom du topic Kafka

# Envoi des messages toutes les N secondes
try:
    while True:
        producer.send_message(topic, data, delivery_report)
        print(f"Sent data: {json.dumps(data)}")
        time.sleep(N)  # Attente de N secondes avant d'envoyer à nouveau
except KeyboardInterrupt:
    print("Process interrupted by user")

# Assurez-vous que tous les messages sont envoyés avant de quitter
producer.flush()
