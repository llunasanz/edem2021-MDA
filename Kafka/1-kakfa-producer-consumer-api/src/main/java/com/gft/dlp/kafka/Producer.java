package com.gft.dlp.kafka;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;

public class Producer {

    public static void main(String[] args){
        Properties properties = new Properties();
        properties.put("bootstrap.servers", "localhost:9092");
        properties.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        KafkaProducer<String, String> kafkaProducer = new KafkaProducer<String, String>(properties);
        try{
            for(int i = 0; i < 100; i++){
                if(i == 99){
                    System.out.println("{Name: Ada}");
                    kafkaProducer.send(new ProducerRecord<String, String>("myTopic", Integer.toString(i), "test message - " + "{Name: Ada}" ));
                }
                else{
                    System.out.println("{Name: Lluna}");
                    kafkaProducer.send(new ProducerRecord<String, String>("myTopic", Integer.toString(i), "test message - " + "{Name: Lluna}" ));
                }
            }
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            kafkaProducer.close();
        }
    }
}