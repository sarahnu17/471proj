# Created on : 4-3-2018
# Created by: Erine Estrella

import socket
import os
import sys

from cmd import Cmd
#from signal import signal, SIGPIPE, SIG_DFL

#signal(SIGPIPE,SIG_DFL)
#server address
serverAddress = "ecs.fullerton.edu"


bytesSent = 0
fileData = None

class MyShell(Cmd):

	def do_get(self, args):
		serverPort = 1234
		filename = args
		print "Now downloading filename : %s from the server..." % filename
		fileObj = open(filename, "r")
		connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		while True: 
			fileData = fileObj.read(65536)
			
			#make sure we do not hit EOF
			if fileData:
				dataSize = str(len(fileData))
				
				while len(dataSize)< 10:
					dataSize = "0" + dataSize
				fileData = dataSize + fileData
				bytesSent = 0
				while len(fileData) > bytesSent: 
					bytesSent += connSock.send(fileData[bytesSent:])
			else:
				break 
				
		print "Filname: ", filename, " with size ", bytesSent, " has been downloaded."
		
		connSock.close()
		fileObj.close()
				
	#def do_put(self, args):
	#def do_ls (self, args):
	def do_quit(self, args):
		print "Now disconnecting from the server and quiting..."
		raise SystemExit
		
if __name__ == '__main__':
	shell = MyShell()
	shell.prompt = 'ftp> '
	shell.cmdloop('Starting Client...')





