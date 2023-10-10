from pyhive import hive
from confluent_kafka import Consumer, KafkaError
import json
from datetime import datetime

def create_hive_table():
    # Create a Hive table if it doesn't exist
    # cursor.execute("""
    # CREATE DATABASE IF NOT EXISTS testdb2;
    # USE testdb2;
    # CREATE TABLE IF NOT EXISTS testdb2 (
    #     id INT,
    #     name STRING,
    #     modified TIMESTAMP
    # )
    # """)
    # cursor.close()
    return

def basic_consume_loop(c, topics):
    try:
        print('try')
        c.subscribe(topics)

    # try:
        while True:
            msg = c.poll(timeout= 1.0)
            # for msg in c:
            if msg is None: continue
            
            if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        print('Reached end of partition')
                    else:
                        print('Error while consuming message: {}'.format(msg.error()))
            else:
                try:
                    message_data = json.loads(msg.value())
                    print(message_data)
                    # message_data = message_data['payload']
                    # try:
                    #     decoded_string = msg.value().decode('utf-8')
                    #     message_data = json.loads(decoded_string)
                    # except:
                    # # Parse the string as JSON
                    #     message_data = json.loads(msg.value())

                    # Insert data into Hive table
                    insert_into_hive(message_data)
                except Exception as e:
                    # decoded_string = msg.value().decode('utf-8', errors='replace')
                    print('Error processing message: {}'.format(e))
                    # insert_into_hive(decoded_string)
                    # insert_into_hive(message_data)

    # except KeyboardInterrupt:
    #     pass
    finally:
        c.close()

def insert_into_hive(data):
    # Insert data into Hive table
    data = data['payload']
    dt = datetime.fromtimestamp(data['modified'] / 1000.0)
    
    convert_dt = dt.strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('use testdb2')
    cursor.execute("""
    INSERT INTO TABLE testdb2 VALUES ({}, '{}', '{}')
    """.format(data['id'], data['name'],convert_dt))# data['modified']))

if __name__ == '__main__':
    # Set up a connection to Hive
    connection = hive.Connection(host='localhost', port=10000)
    cursor = connection.cursor()
    
    # Create the Hive table if it doesn't exist
    create_hive_table()

    # Set up Kafka consumer
    c = Consumer({'bootstrap.servers': 'localhost:9092',
                  'group.id': 'group1',
                  'auto.offset.reset': 'earliest'})

    # Define the Kafka topic you want to consume
    topics = ['quickstart-jdbc-testdb2']

    # Start consuming messages and insert them into Hive
    basic_consume_loop(c, topics)
