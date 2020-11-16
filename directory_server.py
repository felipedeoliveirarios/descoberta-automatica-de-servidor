import rpyc
from rpyc.utils.server import ThreadedServer

import const

"""
Mantém uma lista de servidores disponíveis para acesso.
Repassa o endereço de um servidor quando solicitado pelo cliente.
"""
def DirectoryServer(rpyc.Service):
	server_registry = {} # Guarda tuplas com ip e porta dos servidores, usando o nome como índice.

	# Registra um servidor usando nome, ip e porta.
	def server_register(self, name, ip, port):
		if not (name in server_registry):
			server_registry[name] = (ip, port)
			print("Server @ {}:{} registered as {}.".format(ip, port, name))
			return True
		else:
			print("Server not registered: there is already an entry named {}.".format(name))
			return False

	# Remove o registro de um servidor.
	def server_remove(self, name):
		print("Removing server with name \"{}\"...".format(name))
		if name in server_registry:
			del server_registry[name]
			print("\tSuccess!")
			return True
		else:
			print("\tEntry not found.")
			return False

	# Retorna um servidor, se existir, da lista.
	def fetch_server(self, name):
		
		if self.query_registry(name):
			print("\tSuccess!")
			return (server_registry[name][1], server_registry[name][2])
		else:
			print("\tEntry not found.")
			return None

	def query_registry(self, name)
		print("Looking for server with name \"{}\"...".format(name))
		if name in server_registry:
			print("Name \"{}\" found in registry.".format(name))
			return True
		else:
			print("Name \"{}\" not found in registry.".format(name))
			return False


if __name__ == "__main__":
	directory_server = ThreadedServer(DirectoryServer, port=const.DIR_PORT)
	directory_server.start()