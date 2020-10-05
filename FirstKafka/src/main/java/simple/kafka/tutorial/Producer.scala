package simple.kafka.tutorial
import java.util.Properties

import org.apache.kafka.clients.producer.{KafkaProducer, ProducerConfig, ProducerRecord}


object Producer extends App {
  val p = new Properties()
  p.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,"127.0.0.1:9092")
  p.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG,"org.apache.kafka.common.serialization.StringSerializer")
  p.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG,"org.apache.kafka.common.serialization.StringSerializer")


  val producer = new KafkaProducer[String,String](p)

  val record = new ProducerRecord[String,String]("lasttopic","Hello")

  producer.send(record)
  producer.flush()
  producer.close()





}
