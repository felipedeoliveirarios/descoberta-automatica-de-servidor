import rpyc
from datetime import datetime
import random

import socket
import const

class ApplicationServer(rpyc.Service):
	'''
	Classe base para os serviços oferecidos no projeto.
	Contém implementações de registro, remoção e alteração de endereço junto a um servidor de nomes.
	'''

	app_name = ""

	def register(self, name, port, directory_server_name):
		print("[INFO] Trying to self-register as \"{}\"...".format(name))

		root_conn = rpyc.connect(const.ROOT_IP, const.ROOT_PORT) # Se conecta ao servidor de nomes raiz
		directory_server_address = root_conn.root.lookup(directory_server_name) # Encontra o endereço do servidor de diretório.

		if type(directory_server_address) is not tuple: # Caso o retorno não seja o endereço...
			print(directory_server_address) # Exibe a mensagem de erro retornada.
			return False # Finaliza o método.

		dir_conn = rpyc.connect(directory_server_address[0], directory_server_address[1]) # Se conecta ao servidor de nomes.

		local_ip = socket.gethostbyname(socket.gethostname()) # Obtém o ip local.
		app_address = (local_ip, port)
		result = dir_conn.root.register(name, app_address) # Tenta se registrar no servidor de nomes.

		if "[ERROR]" not in result: # Caso não retorne um erro...
			print("[INFO] Successfully registered as \"{}\".".format(result))
			self.app_name = result # Salva o nome totalmente qualificado do serviço
			return True

		else: # Caso seja um erro...
			print(result) # Exibe o erro.
			return False

	def unregister(self):
		print("[INFO] Trying to self-unregister...")
		root_conn = rpyc.connect(const.ROOT_IP, const.ROOT_PORT) # Se conecta ao servidor de nomes raiz
		result = root_conn.root.unregister(self.app_name)

		if "[ERROR]" in result:
			print(result)
			print("[INFO] Failed. Server not registered.")
			return False

		else:
			print("[INFO] Sucess! Unregistered from directory server.")
			return True

	def update_address(self, new_name):
		print("[INFO] Atualizando endereço.")
		separator_position = self.app_name.find(':')
		directory_server_name = name[:separator_position]
		root_conn = rpyc.connect(const.ROOT_IP, const.ROOT_PORT) # Se conecta ao servidor de nomes raiz
		directory_server_address = root_conn.root.lookup(directory_server_name) # Encontra o endereço do servidor de diretório.

		if type(directory_server_address) is not tuple: # Caso o retorno não seja o endereço...
			print(directory_server_address) # Exibe a mensagem de erro retornada.
			return False # Finaliza o método.

		dir_conn = rpyc.connect(directory_server_address[0], directory_server_address[1]) # Se conecta ao servidor de nomes.

		local_ip = socket.gethostbyname(socket.gethostname()) # Obtém o ip local.
		app_address = (local_ip, port)
		result = dir_conn.root.re_register(name, app_address) # Tenta se registrar no servidor de nomes.

		if "[ERROR]" not in result: # Caso não retorne um erro...
			print("[INFO] Address updade successful. \"{}\".".format(result))
			return True

		else: # Caso seja um erro...
			print(result) # Exibe o erro.
			return False 
		
	def exposed_run(self):
		pass

class BMIServer(ApplicationServer):
	def exposed_run(self, weigth, height, age):
		print("[INFO] Starting BMI application.")
		bmi = weigth/(height**2)
		result = "Seu IMC é {.2f}. ".format(bmi)

		if age <= 65:
			if bmi < 18.5:
				result += "Você está abaixo do peso normal."
			elif bmi >= 18.5 and bmi < 25:
				result += "Você está dentro do peso normal."
			elif bmi >= 25 and bmi < 30:
				result += "Você está acima do peso normal."
			elif bmi >= 30 and bmi < 35:
				result += "Você está com obesidade Classe 1. Procure acompanhamento médico."
			elif bmi >= 35 and bmi < 40:
				result += "Você está com obesidade Classe 2. Procure acompanhamento médico."
			elif bmi >= 40:
				result += "Você está com obesidade Classe 3. Procure acompanhamento médico."
			else:
				result += "Valores de entrada inválidos."

		else:
			if bmi < 22:
				result += "Você está abaixo do peso normal."
			elif bmi >= 22 and bmi < 27:
				result += "Você está dentro do peso normal."
			elif bmi >= 27:
				result += "Você está acima do peso normal."

		print("[INFO] Finishing BMI application.")
		return result

class DateTimeServer(ApplicationServer):
	def exposed_run(self):
		print("[INFO] Starting DateTime application.")
		result = datetime.now().strftime("%H:%M - %d/%m/%Y")
		print("[INFO] Finishing DateTime application.")
		return result

class MotivationalServer(ApplicationServer):
	def exposed_run(self):
		index = random.random(0, len(const.MOTIVATIONAL_STRINGS))
		return const.MOTIVATIONAL_STRINGS[index]

