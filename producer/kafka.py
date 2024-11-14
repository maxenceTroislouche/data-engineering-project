import json
from confluent_kafka import Producer

class KafkaProducer:
    _producer = None
    
    servers: str
    client_id: str
    
    def __init__(self, servers: str, client_id: str):
        self.servers = servers
        self.client_id = client_id
        
        self._producer = Producer({
            'bootstrap.servers': servers,
            'client.id': client_id
        })
        
    def send_message(self, topic: str, message: dict, callback: callable=None):
        self._producer.produce(topic, value=json.dumps(message), callback=callback)
        self._producer.poll(0)
        
    def flush(self):
        self._producer.flush()
        