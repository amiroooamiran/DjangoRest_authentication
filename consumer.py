"""
go to the cloudamqp.com create and create 
"""
import pika

params = pika.URLParameters('amqps://jobgloyb:4IL8D0pdBrNCQoxlj6j_MFBQGSIU60Wd@rat.rmq2.cloudamqp.com/jobgloyb')
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("Recibed in admin")
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callable)
print('start Consuming')

channel.start_consuming()
channel.close()