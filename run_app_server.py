from rpyc.utils.server import ForkingServer
import argparse

from applications import BMIServer, DateTimeServer, MotivationalServer
import const

parser = argparse.ArgumentParser(description="Inicia um servidor de aplicação.")
parser.add_argument("application", metavar="app", type=str, help="Escolha a aplicação cujo servidor deve ser iniciado, entre \"imc\", \"datahora\" e \"motivacional\"." )
parser.add_argument("server", type=str, help="Escolha entre os dois servidores de nomes com \"A\" ou \"B\".")
args = parser.parse_args()

server_name = ''
if args.server == 'A':
	server_name = const.DIR_NAME_A
elif args.server == 'B':
	server_name = const.DIR_NAME_B
else:
	raise ValueError("Argumento \"{}\" inválido.".format(args.server))

if args.app == "imc":
	app_server = ForkingServer(BMIServer, const.APP_1_PORT)
	app_server.register(const.APP_1_NAME, const.APP_1_PORT, server_name)
	app_server.start()

elif args.app == "datahora":
	app_server = ForkingServer(DateTimeServer, const.APP_2_PORT)
	app_server.register(const.APP_2_NAME, const.APP_2_PORT, server_name)
	app_server.start()

elif args.app == "motivacional":
	app_server = ForkingServer(MotivationalServer, const.APP_3_PORT)
	app_server.register(const.APP_3_NAME, const.APP_3_PORT, server_name)
	app_server.start()

else:
	raise ValueError("Argumento \"{}\" inválido.".format(args.app))