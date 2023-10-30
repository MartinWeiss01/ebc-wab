import pika
import logging

from logging import basicConfig

basicConfig(
    filename='logFileR.txt',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
conn_params = pika.ConnectionParameters(host='127.0.0.1')

def publish(msg: str):
    try:
        conn = pika.BlockingConnection(conn_params)
        channel = conn.channel()
        channel.basic_publish(
            exchange='',
            routing_key='wab_4',
            body=msg
        )
        conn.close()
        logging.info("Publish event '%s'", msg)
    except Exception as e:
        logging.error("Publish failed")
    
    