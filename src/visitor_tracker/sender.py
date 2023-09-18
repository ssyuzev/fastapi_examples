
import pika


def sender(body: dict):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='logs')

    channel.basic_publish(exchange='', routing_key='logs', body=body)
    print(" [x] Sent 'Logs'")
    connection.close()
