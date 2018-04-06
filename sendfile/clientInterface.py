#####################################
# Created on : 4-3-2018				#
# Created by: Erine Estrella		#
#####################################

#importing modules

from cmd import Cmd
import socket
import os import system
import sys



def run(clientArg):

	# initializing the server and port number from input
	arg_length = len(clientArg)

	if arg_length == 3:
		return clientArg[1], clientArg[2]
	else:
		print "\n Please use the format: python clientInterface.py <server address> <server port number>" \
		"Example: python clientInterface.py ecs.fullerton.edu 1234"
	
	address, portNumber = clientArg
	
	#initializing ftp command connection
	commandSocket = initializeConnection(address, portNumber)

	clientRequestHandler(address, commandSocket)


def initializeConnection(serverAddress, serverPortNum):
	
	# converting port Number string to integer
	serverPortNum = int(serverPortNum)
	
	# create the command socket
	interface = ClientInterface()
	cmdSocket = interface.createSocket(serverAddress, serverPortNum)

	return cmdSocket
	
def clientRequestHandler(addr, cmdSocket = None)

	if cmdSocket is not None:
	
		# creating client interface and store the command socket
		interface = ClientInterface()
		interface.saveHostDetails(addr, cmdSocket)
		interface.cmdloop()

class ClientInterface(Cmd):

	# save host address and host socket
	hostAddress = ''
	cmdSocket = ''
	prompt = "ftp> "
	
	#############################
	#	Main Command Methods	#
	#############################
	
	def do_get(self, args):
		filename = args
		if filename:
			print "Now downloading filename : %s from the server..." % filename
		else:
			print "Sorry, that was incorrect formatting. Please try again."
	#def do_put(self, args):
	#def do_ls (self, args):
	def do_quit(self, args):
		print "Now disconnecting from the server and quiting..."
		raise SystemExit
		
	#############################
	#	Worker Functions		#
	#############################
	
	def saveHostDetails (self, hostAddr, socket):
		self.hostAddr = hostAddr
		self.cmdSocket = socket
		
	def createSocket(self, addr, portNum):
		# try to create a socket, if not return error
		
		try:
			createSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			createSocket.connect((hostAddr, portNum))
			print "\nConnection to server has been made on port #%s ." % portNum


# run main

if __name__ == '__main__':

	run(sys.argv)


