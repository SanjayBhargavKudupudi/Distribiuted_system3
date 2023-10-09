import pika

received_count = 0

def callback(ch, method, properties, body):
    global received_count
    received_count += 1
    print(f" [x] Received {body}")
    if received_count == 10000:
        print("Received all 10,000 messages!")
        connection.close()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
