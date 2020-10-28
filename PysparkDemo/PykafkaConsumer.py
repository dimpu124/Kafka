from pykafka import *

client = KafkaClient(hosts="127.0.0.1:9092")

topic = client.topics["FirstPytopic"]
produce = topic.get_producer()
for i in client.topics["FirstPytopic"].get_simple_consumer():
    print(i.value.decode())

