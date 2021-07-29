#
# filename    : eval-rabbitmq-py-receive.py
# Description : 
# Docs        :
#               * https://www.rabbitmq.com/tutorials/tutorial-one-python.html
#				* https://hub.docker.com/_/rabbitmq
#				* https://www.embarcados.com.br/amqp-cliente-pika-e-broker-rabbitmq/
# Requirements:
#               * python -m pip install pika --upgrade
#

import pika, sys, os
from time import sleep

def callback(ch, method, properties, body):
	print("  callback received msg: %r" % body)

def main():
	#amqs_url = 'amqp://admin:admin@localhost/vhosts'
	amqs_url = 'amqps://********:********************************@jackal.rmq.cloudamqp.com/********' # secrets.tmp
	queue_name = 'queue-eval'
	parameters = pika.URLParameters(amqs_url)
	print(f'  pika.BlockingConnection({amqs_url})')
	connection = pika.BlockingConnection(parameters)
	channel = connection.channel()
	print('  channel.queue_declare()')
	channel.queue_declare(queue=queue_name)  # create queue
	channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
	channel.start_consuming()



#
# __main__:
#
if __name__ == '__main__':

	print('eval-rabbitmq-py-send:')
	try:
		main()
	except KeyboardInterrupt:
		print('^C interruption: exiting')

	print('eval-rabbitmq-py-receive: Done!')
