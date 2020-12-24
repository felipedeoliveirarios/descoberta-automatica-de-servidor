import rpyc
import const

class Client:

	def run(self):
		root_conn = rpyc.connect(const.ROOT_IP, const.ROOT_PORT)

		print("[INFO] Procurando o serviço \"A:1\"...")
		app_address = root_conn.root.lookup("A:1")
		print("[INFO] Encontrado. Endereço: {}".format(app_address))
		print("[INFO] Estabelecendo conexão com o serviço...")
		app_conn = rpyc.connect(app_address)
		print("[INFO] Feito. Chamando o serviço com os parâmetros (45, 1.6, 20)...")
		result = app_conn.root.run(45, 1.6, 20)
		print("[INFO] Feito. Resultado: \"{}\".".format(result))

		print("[INFO] Procurando o serviço \"A:2\"...")
		app_address = root_conn.root.lookup("A:2")
		print("[INFO] Encontrado. Endereço: {}".format(app_address))
		print("[INFO] Estabelecendo conexão com o serviço...")
		app_conn = rpyc.connect(app_address)
		print("[INFO] Feito. Chamando o serviço...")
		result = app_conn.root.run()
		print("[INFO] Feito. Resultado: \"{}\".".format(result))

		print("[INFO] Procurando o serviço \"A:3\"...")
		app_address = root_conn.root.lookup("A:3")
		print("[INFO] Encontrado. Endereço: {}".format(app_address))
		print("[INFO] Estabelecendo conexão com o serviço...")
		app_conn = rpyc.connect(app_address)
		print("[INFO] Feito. Chamando o serviço...")
		result = app_conn.root.run()
		print("[INFO] Feito. Resultado: \n\"{}\".".format(result))

		print("[INFO] Procurando o serviço \"B:1\"...")
		app_address = root_conn.root.lookup("B:1")
		print("[INFO] Encontrado. Endereço: {}".format(app_address))
		print("[INFO] Estabelecendo conexão com o serviço...")
		app_conn = rpyc.connect(app_address)
		print("[INFO] Feito. Chamando o serviço com os parâmetros (45, 1.6, 20)...")
		result = app_conn.root.run(45, 1.6, 20)
		print("[INFO] Feito. Resultado: \"{}\".".format(result))

		print("[INFO] Procurando o serviço \"B:2\"...")
		app_address = root_conn.root.lookup("B:2")
		print("[INFO] Encontrado. Endereço: {}".format(app_address))
		print("[INFO] Estabelecendo conexão com o serviço...")
		app_conn = rpyc.connect(app_address)
		print("[INFO] Feito. Chamando o serviço...")
		result = app_conn.root.run()
		print("[INFO] Feito. Resultado: \"{}\".".format(result))

		print("[INFO] Procurando o serviço \"B:3\"...")
		app_address = root_conn.root.lookup("B:3")
		print("[INFO] Encontrado. Endereço: {}".format(app_address))
		print("[INFO] Estabelecendo conexão com o serviço...")
		app_conn = rpyc.connect(app_address)
		print("[INFO] Feito. Chamando o serviço...")
		result = app_conn.root.run()
		print("[INFO] Feito. Resultado: \n\"{}\".".format(result))
	
if __name__ == "__main__":
	instance = Client()
	instance.run()
