import rpyc
import const

class Client:

	def run(self):
		run = True
		while run:
			print(const.CLIENT_MENU)
			app_selection = int(input())

			if not app_selection:
				print("\nOpção inválida!\n")
				continue

			if app_selection == 0:
				print("#"*80 + "\n")
				run = False
				break

			elif app_selection == 1:
				print("#"*80 + "\n")
				self.bmi_app()

			elif app_selection == 2:
				print("#"*80 + "\n")
				self.date_time_app()

			elif app_selection == 3:
				print("#"*80 + "\n")
				self.motivational_app()

			else:
				print("#"*80 + "\n")
				print("\nOpção Inválida!\n")

	def bmi_app(self):
		peso = float(input("Por favor, insira seu peso em quilogramas. "))
		altura = float(input("Por favor, insira sua altura em metros. "))
		idade = int(input("Por favor, insira sua idade. "))

		if peso and altura and idade:
			root_conn = rpyc.connect(const.ROOT_IP, const.ROOT_PORT)
			application_address = root_conn.root.lookup(const.DIR_NAME_A + ":" + const.APP_1_NAME)
			print(application_address)
			app_conn = rpyc.connect(application_address[0], application_address[1])
			result = app_conn.root.run(peso, altura, idade)
			print("\n"+ result + "\n")

	def date_time_app(self):
		root_conn = rpyc.connect(const.ROOT_IP, const.ROOT_PORT)
		application_address = root_conn.root.lookup(const.DIR_NAME_B + ":" + const.APP_2_NAME)
		app_conn = rpyc.connect(application_address[0], application_address[1])
		result = app_conn.root.run()
		print("\nHora - Data: "+ result + "\n")
		
	def motivational_app(self):
		root_conn = rpyc.connect(const.ROOT_IP, const.ROOT_PORT)
		application_address = root_conn.root.lookup(const.DIR_NAME_B + ":" + const.APP_3_NAME)
		app_conn = rpyc.connect(application_address[0], application_address[1])
		result = app_conn.root.run()
		print('\n' + result + '\n')
	
if __name__ == "__main__":
	instance = Client()
	instance.run()
