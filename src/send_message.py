import pika

conn_params = pika.ConnectionParameters(
    host='127.0.0.1',
    port=5672,
    credentials=pika.PlainCredentials('guest', 'guest')
)
conn = pika.BlockingConnection(conn_params)
channel = conn.channel()
channel.queue_declare(queue='wab_4')
channel.basic_publish(
    exchange='',
    routing_key='wab_4',
    body="Hello 2"
)

conn.close()