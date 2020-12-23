import rpyc
import const

class Client:

	def run(self):
		run = True
		while run:
			print(const.CLIENT_MENU)
			app_selection = int(input())

			if not app_selection:
				print("Opção inválida!\n")
				continue

			if app_selection == 0:
				print("#"*80)
				run = False
				break

			elif app_selection == 1:
				print("#\n"*80)
				self.bmi_app()

			elif app_selection == 2:
				print("#\n"*80)
				self.date_time_app()

			elif app_selection == 3:
				print("#\n"*80)
				self.motivational_app()

	def bmi_app(self):
		peso = float(input("Por favor, insira seu peso em quilogramas."))
		altura = float(input("Por favor, insira sua altura em metros. "))
		idade = int(input("Por favor, insira sua idade. "))

		if peso and altura and idade:
			root_conn = rpyc.conn(ROOT_IP, ROOT_PORT)
			application_address = root_conn.lookup(const.APP_1_NAME)
			app_conn = rpyc.conn(application_address)
			result = app_conn.root.run(peso, altura, idade)
			print("\n"+ result + "\n")

	def date_time_app(self):
		root_conn = rpyc.conn(ROOT_IP, ROOT_PORT)
		application_address = root_conn.lookup(const.APP_2_NAME)
		app_conn = rpyc.conn(application_address)
		result = app_conn.root.run()
		print("\nHora - Data: "+ result + "\n")
		
	def motivational_app(self):
		root_conn = rpyc.conn(ROOT_IP, ROOT_PORT)
		application_address = root_conn.lookup(const.APP_2_NAME)
		app_conn = rpyc.conn(application_address)
		result = app_conn.root.run()
		print('\n' + result + '\n')
	
if __name__ == "__main__":
	instance = Client()
	instance.run()
