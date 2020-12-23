import rpyc
from rpyc.utils.server import ThreadedServer

import const

"""
Mantém uma lista de servidores disponíveis para acesso.
Repassa o endereço de um servidor quando solicitado pelo cliente.
"""
def DirectoryServer(rpyc.Service):
	server_name = ''
	server_registry = {} # Guarda tuplas com ip e porta dos servidores, usando o nome como índice.
	sub_servers = {}

	# Registra um servidor usando nome, ip e porta.
	def register(self, name, address):
		print('[INFO] Starting register procedure.')
		if not (name in server_registry):

			server_registry[name] = address
			fully_qualified_name = server_name + ':' + name
			print("[INFO] Server @ {}:{} registered as {}.".format(ip, port, name))
			return fully_qualified_name

		else:
			print("[INFO] Server not registered: there is already an entry named {}.".format(name))
			return "[ERROR] There is already an entry named {}".format(name)

	# Resolve um nome. Retorna o endereço associado ao nome, se existir, ou uma mensagem de erro.
	def lookup(self, name):
		print("[INFO] Starting lookup for {}.".format(name))
		separator_position = name.find(':')

		if separator_position < 0: # Não é um FQN
			print("[INFO] Starting local lookup for {}.".format(name))
			if name in server_registry:
				print("[INFO] Success!")
				return server_registry[name]
			else:
				print("[INFO] Entry not found.")
				return "[ERROR] Local entry \"{}\" not found.".format(name)

		else: # É um FQN
			naming_context = name[:separator_position]
			local_name = name[separator_position+1:]

			if server == self.server_name: # É um FQN do servidor local
				print("[INFO] Starting local lookup for {}.".format(name))
				if name in registry:
					print("[INFO] Success!")
					return server_registry[name]
				else:
					print("[INFO] Entry not found.")
					return "[ERROR] Local entry \"{}\" not found.".format(name)
			
			else: # É um FQN de outro servidor
				if naming_context in sub_servers: # O contexto é válido.
					print("[INFO] Starting lookup for \"{}\" at \"{}\".".format(local_name, naming_context))
					sub_server = rpyc.connect(sub_servers[naming_context])
					result = sub_server.root.lookup(local_name)

					if type(result) is tuple: # Encontrado no outro servidor.
						print("[INFO] Success!")

					else: # Não encontrado no servidor.
						print("[INFO] Entry not found.")

					return result

				else: # O contexto é inválido.
					print("[INFO] Invalid Context.")
					return "[ERROR] Invalid Context." 

	# Remove um registro 
	def unregister(self, name):
		print("[INFO] Starting removal of entry \"{}\".".format(name))
		separator_position = name.find(':')

		if separator_position < 0: # Nome não é FQN
			print("[INFO] Starting local removal of entry \"{}\".".format(name))
			if name in server_registry: # Nome está no registro
				del server_registry[name]
				print("[INFO] Success!")
				return (name)

			else: # Nome não está no registro
				print("[INFO] Entry not found.")
					return "[ERROR] Local entry \"{}\" not found.".format(name)

		else: # Nome é FQN
			naming_context = name[:separator_position]
			local_name = name[separator_position+1:]

			if server == self.server_name: # É um FQN do servidor local
				print("[INFO] Starting local removal of \"{}\".".format(name))
				if name in server_registry: # Nome está no registro
					del server_registry[name]
					print("[INFO] Success!")
					return (name)

				else: # Nome não está no registro.
					print("[INFO] Entry not found.")
					return "[ERROR] Local entry \"{}\" not found.".format(name)

			else: # É um FQN de outro servidor.
				if naming_context in sub_servers: # O contexto é válido.
					print("[INFO] Starting removal of \"{}\" at \"{}\".".format(local_name, naming_context))
					sub_server = rpyc.connect(sub_servers[naming_context])
					result = sub_server.root.unregister(local_name)

					if type(result) is tuple: # Encontrado no outro servidor.
						print("[INFO] Success!")

					else: # Não encontrado no servidor.
						print("[INFO] Entry not found.")

					return result

				else: # O contexto é inválido.
					print("[INFO] Invalid Context.")
					return "[ERROR] Invalid Context." 

	# Atualiza o endereço associado a um nome.
	def re_register(self, name, address):
		print("[INFO] Starting update of entry \"{}\".".format(name))
		separator_position = name.find(':')

		if separator_position < 0: # Nome não é FQN
			print("[INFO] Starting local removal of entry \"{}\".".format(name))
			if name in server_registry: # Nome está no registro
				server_registry[name] = address
				print("[INFO] Success!")
				return address

			else: # Nome não está no registro
				print("[INFO] Entry not found.")
					return "[ERROR] Local entry \"{}\" not found.".format(name)

		else: # Nome é FQN
			naming_context = name[:separator_position]
			local_name = name[separator_position+1:]

			if server == self.server_name: # É um FQN do servidor local
				print("[INFO] Starting local removal of \"{}\".".format(name))
				if name in server_registry: # Nome está no registro
					server_registry[name] = address
					print("[INFO] Success!")
					return address

				else: # Nome não está no registro.
					print("[INFO] Entry not found.")
					return "[ERROR] Local entry \"{}\" not found.".format(name)

			else: # É um FQN de outro servidor.
				if naming_context in sub_servers: # O contexto é válido.
					print("[INFO] Starting removal of \"{}\" at \"{}\".".format(local_name, naming_context))
					sub_server = rpyc.connect(sub_servers[naming_context])
					result = sub_server.root.re_register(local_name, address)

					if type(result) is tuple: # Encontrado no outro servidor.
						print("[INFO] Success!")

					else: # Não encontrado no servidor.
						print("[INFO] Entry not found.")

					return result

				else: # O contexto é inválido.
					print("[INFO] Invalid Context.")
					return "[ERROR] Invalid Context." 

if __name__ == "__main__":
	directory_server = ThreadedServer(DirectoryServer, port=const.DIR_PORT)
	directory_server.start()