import rpyc
import const


"""
"""
class Client:

	application_server = None
	app_conn = None

	def get_server(self):
		dir_conn = rpyc.connect(const.DIR_IP, const.DIR_PORT)
		application_server = dir_conn.root.fetch_server(const.APP_NAME)

	def application_connect(self):
		app_conn = rpyc.connect(application_server)

	def call_application(self):
		height = input("Insira sua altura: ")
		width = input("Insira seu peso: ")
		age = input("Insira sua idade: ")
		bmi = app_conn.root.run_application(width, height)

		if age <= 65:
			if bmi < 18.5:
				print("Você está abaixo do peso normal.")
			elif bmi >= 18.5 and bmi < 25:
				print("Você está dentro do peso normal.")
			elif bmi >= 25 and bmi < 30:
				print("Você está acima do peso normal.")
			elif bmi >= 30 and bmi < 35:
				print("Você está com obesidade Classe 1. Procure tratamento médico.")
			elif bmi >= 35 and bmi < 40:
				print("Você está com obesidade Classe 2. Procure tratamento médico.")
			elif bmi >= 40:
				print("Você está com obesidade Classe 3. Procure tratamento médico.")
			else:
				print("Valores de entrada inválidos.")

		else:
			if bmi < 22:
				print("Você está abaixo do peso normal.")
			elif bmi >= 22 and bmi < 27:
				print("Você está dentro do peso normal.")
			elif bmi >= 27:
				print("Você está acima do peso normal.")

if __name__ == "__main__":
	instance = Client()
	instance.get_server()
	instance.application_connect()
	instance.call_application()
