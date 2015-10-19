#!/usr/bin/env python
import time

from RabbitMQ_Server import RabbitMQ_Server

server = RabbitMQ_Server()

server.StartServer()

time.sleep(5)

server.StopServer()


print "TEST Done!"
