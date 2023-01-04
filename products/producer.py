import pika

params = pika.URLParameters('amqps://jodsdmyk:3J9-EiOPkgY43ycfsulNN82DmLGN3oeA@shark.rmq.cloudamqp.com/jodsdmyk')


connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')

