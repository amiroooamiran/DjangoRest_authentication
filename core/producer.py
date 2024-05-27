# amqps://jobgloyb:4IL8D0pdBrNCQoxlj6j_MFBQGSIU60Wd@rat.rmq2.cloudamqp.com/jobgloyb
import pika

params = pika.URLParameters('amqps://jobgloyb:4IL8D0pdBrNCQoxlj6j_MFBQGSIU60Wd@rat.rmq2.cloudamqp.com/jobgloyb')
connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')