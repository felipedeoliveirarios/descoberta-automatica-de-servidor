from rpyc.utils.server import ForkingServer
import argparse

from applications import *
import const

parser = argparse.ArgumentParser(description="Inicia um servidor de aplicação.")
parser.add_argument("app", type=str, help="Escolha a aplicação cujo servidor deve ser iniciado, entre \"imc\", \"datahora\" e \"motivacional\"." )
parser.add_argument("name", type=str, help="Nome usado pela aplicação ao se registrar no servidor de nomes.")
parser.add_argument("server", type=str, help="Servidor de segundo nível no qual a aplicação deve se registrar.")
parser.add_argument("port", type=int, help="Porta usada na conexão com a aplicação.")
args = parser.parse_args()

app_server_name = args.name
app_server_port = args.port
dir_server_name = args.server

root_conn = rpyc.connect(const.ROOT_IP, const.ROOT_PORT) # Estabelece conexão com o servidor de nomes raiz.
response = root_conn.root.lookup(dir_server_name)

if type(response) is tuple:
	if args.app == "imc":
		app_server = BMIServer()

	elif args.app == "datahora":
		app_server = DateTimeServer()

	elif args.app == "motivacional":
		app_server = MotivationalServer()

	else:
		raise ValueError("Argumento \"{}\" inválido.".format(args.app))

	local_ip = socket.gethostbyname(socket.gethostname())

	app_server.register(app_server_name, app_server_port, dir_server_name)
	app_server = ForkingServer(app_server, port=app_server_port)
	app_server.start()

else:
	print("[ERRO] Não foi possível localizar o servidor de nomes \"{}\"".format(dir_server_name))