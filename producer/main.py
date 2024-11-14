from data_transform import get_json_string_from_pacemaker_measure
from kafka import KafkaProducer
from measure_generator import generate_measure_for_pacemaker
from pacemaker import Pacemaker

kafka_conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

producer = KafkaProducer(servers=kafka_conf['bootstrap.servers'], client_id=kafka_conf['client.id'])

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic} [{msg.partition}] at offset {msg.offset}")

pacemaker = Pacemaker(id=1)
measure = generate_measure_for_pacemaker(pacemaker)

producer.send_message('pacemaker-measures', get_json_string_from_pacemaker_measure(measure), delivery_report)
# N = 5
# topic = 'my_topic'  # Nom du topic Kafka

# Envoi des messages toutes les N secondes
# try:
#     while True:
#         producer.send_message(topic, data, delivery_report)
#         print(f"Sent data: {json.dumps(data)}")
#         time.sleep(N)  # Attente de N secondes avant d'envoyer à nouveau
# except KeyboardInterrupt:
#     print("Process interrupted by user")


# Assurez-vous que tous les messages sont envoyés avant de quitter
producer.flush()
