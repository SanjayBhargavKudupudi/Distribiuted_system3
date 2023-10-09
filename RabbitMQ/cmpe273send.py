import pika

# Establish a connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='hello')

# Send 10,000 messages
for i in range(1000):
    channel.basic_publish(exchange='', routing_key='hello', body=f'Message {i+1}')
    print(f" [x] Sent 'Message {i+1}'")

connection.close()
