from pykafka import *

client = KafkaClient(hosts="127.0.0.1:9092")

topic = client.topics["FirstPytopic"]
produce = topic.get_producer()
for i in range(4):
    produce.produce(("Square of "+str(i)+" is "+str(i**2)).encode('ascii'))


