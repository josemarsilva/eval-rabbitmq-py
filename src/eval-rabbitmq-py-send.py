#
# filename    : eval-rabbitmq-py-send.py
# Description : 
# Docs        :
#               * https://www.rabbitmq.com/tutorials/tutorial-one-python.html
#				* https://hub.docker.com/_/rabbitmq
#				* https://www.embarcados.com.br/amqp-cliente-pika-e-broker-rabbitmq/
# Requirements:
#               * python -m pip install pika --upgrade
#

import pika
from time import sleep

#
# __main__:
#
if __name__ == '__main__':

	print('eval-rabbitmq-py-send:')

	# Startup application module ...
	#amqs_url = 'amqp://admin:admin@localhost/vhosts'
	amqs_url = 'amqps://fojschhk:AnTrXn3Z3dn4Co9yjOhulcVFjE0Z8Jkd@jackal.rmq.cloudamqp.com/fojschhk'
	queue_name = 'queue-eval'
	body_msg = 'Hello, this is message number {num}. Did you get it?'
	count_msg = 50
	parameters = pika.URLParameters(amqs_url)
	print(f'  pika.BlockingConnection({amqs_url})')
	connection = pika.BlockingConnection(parameters)
	channel = connection.channel()
	print('  channel.queue_declare()')
	channel.queue_declare(queue=queue_name)  # create queue

	# loop "count_msg" times publishing ...
	for i in range(count_msg):
		print(f'  channel.basic_publish({i+1})')
		sleep(0)
		channel.basic_publish(exchange='', routing_key=queue_name, body=(body_msg.replace('{num}',str(i+1))))

	# close ...
	print('  connection.close()')
	connection.close()
	
	print('eval-rabbitmq-py-send: Done!')
