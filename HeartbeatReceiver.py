#!/usr/bin/env python
import pika
import sys,time

class HeartbeatReceiver:
    pass

proc_name = raw_input("Give a name for this proc:  ")

my_routing_key=proc_name+".hb"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel_hb_receive = connection.channel()
channel_hb_receive.exchange_declare(exchange='heartbeat_reqs',type='fanout')
result = channel_hb_receive.queue_declare(exclusive=True)
my_queue_name = result.method.queue

channel_status_send = connection.channel()
channel_status_send.exchange_declare(exchange='heartbeat_messages',type='topic')

def callback(ch,method,properties,body):
    print " [x] Heartbeat msg received: %r" % (body,)
    #ch.basic_ack(delivery_tag = method.delivery_tag)
    if(body=="badump"):
        channel_status_send.basic_publish(exchange='heartbeat_messages',
                                          routing_key=my_routing_key,
                                          body='ALIVE!')
    print " [x] Status sent!"

channel_hb_receive.queue_bind(exchange='heartbeat_reqs',queue=my_queue_name)
channel_hb_receive.basic_consume(callback,queue=my_queue_name,no_ack=True)

print ' [*] Process ' + proc_name + ' waiting for heartbeats. To exit, press CTRL+C'
channel_hb_receive.start_consuming()
