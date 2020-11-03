import rpyc
from rpyc.utils.server import ForkingServer

import socket
import const

class ApplicationServer(rpyc.Service):

	def self_register(self):
		local_ip = socket.gethostbyname(socket.gethostname())
		dir_conn = rpyc.connect(DIR_IP, DIR_PORT)
		dir_conn.root.server_register(const.APP_NAME, local_ip, const.APP_PORT)

	def self_unregister(self):
		dir_conn = rpyc.connect(const.DIR_IP, const.DIR_PORT)
		dir_conn.root.server_remove(const.APP_NAME)

	def run_application(self, weight, height):
		bmi = (weight/(height**2))
		return bmi

if __name__ == "__main__":
	server = ForkingServer(ApplicationServer, const.APP_PORT)
	server.self_register()
	server.start()