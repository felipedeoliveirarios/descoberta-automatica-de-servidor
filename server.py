import rpyc
from rpyc.utils.server import ForkingServer

import socket
import const

class ApplicationServer(rpyc.Service):

	serverName = ""

	def self_register(self, name):
		print("Trying to self-register as \"{}\"...".format(name))
		local_ip = socket.gethostbyname(socket.gethostname())
		dir_conn = rpyc.connect(DIR_IP, DIR_PORT)
		if !self.query_directory(name):
			dir_conn.root.server_register(name, local_ip, const.APP_PORT)
			print("Sucess! Registered as \"{}\".".format(name))
			serverName = name
			return True
		else:
			print("Failed. There is already a server registered as \"{}\".".format(name))
			return False

	def self_unregister(self):
		print("Trying to self-unregister...")

		if serverName == "":
			print("Failed. Server not registered.")
			return False

		dir_conn = rpyc.connect(const.DIR_IP, const.DIR_PORT)

		if dir_conn.root.query_registry(serverName):
			dir_conn.root.server_remove(serverName)
			print("Sucess! Unregistered from directory server.")
			serverName = ""
			return True
		else:
			print("Falied. No register found with server name.")
			serverName = ""
			return False

	def run_application(self, weight, height):
		bmi = (weight/(height**2))
		return bmi

	def query_directory(self, name):
		dir_conn = rpyc.connect(DIR_IP, DIR_PORT)
		return dir_conn.root.query_registry(name)


if __name__ == "__main__":
	server = ForkingServer(ApplicationServer, const.APP_PORT)
	server.self_register(const.APP_NAME)
	server.start()