import pika, json

params = pika.URLParameters('amqps://jodsdmyk:3J9-EiOPkgY43ycfsulNN82DmLGN3oeA@shark.rmq.cloudamqp.com/jodsdmyk')


connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):

    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dump(body), properties=properties)

