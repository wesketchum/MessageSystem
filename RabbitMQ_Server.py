#!/usr/bin/env python
import sys, subprocess


class RabbitMQ_Server:

    def __init__(self,cmd_loc="/Users/wketchum/Messaging/rabbitmq_server-3.5.6/sbin/"):
        print "Initialized server object."
        self.cmd = cmd_loc+"rabbitmq-server"

    def StartServer(self):
        print "Going to run server command " + self.cmd
        self.myprocess = subprocess.Popen(self.cmd)

    def StopServer(self):
        self.myprocess.terminate()
        print "Stopped server."
