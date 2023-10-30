from fastapi import FastAPI

app = FastAPI()

import pika

conn_params = pika.ConnectionParameters(host='127.0.0.1')
conn = pika.BlockingConnection(conn_params)
channel = conn.channel()
channel.queue_declare(queue='wab_4')

def callback(channel, method, properties, body):
    print(f"{channel}\n\n{method}\n\n{properties}\n\n{body}")

channel.basic_consume(
    queue='wab_4',
    auto_ack=True,
    on_message_callback=callback
)
