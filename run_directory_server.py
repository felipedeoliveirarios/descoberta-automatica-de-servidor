import rpyc
from rpyc.utils.server import ThreadedServer
import socket
import argparse

from directory_server import DirectoryServer
import const

parser = argparse.ArgumentParser(description="Inicia um servidor de nomes.")
parser.add_argument("name", type=str, help="Nome a ser usado pelo servidor ao se registrar.")
parser.add_argument("port", type=int, help="Porta a ser usada na conexão com o servidor.")
args = parser.parse_args()

server = DirectoryServer()
server.server_name = args.name # Define o nome do servidor de nomes.
server = ThreadedServer(server, port=args.port) # Define a porta para o servidor.

local_ip = socket.gethostbyname(socket.gethostname()) # Encontra o IP local.
address = (local_ip, args.port) # Empacota endereço ip e porta em uma tupla.

root_conn = rpyc.connect(const.ROOT_IP, const.ROOT_PORT) # Estabelece conexão com o servidor de nomes raiz.
root_conn.root.register(args.name, address) # Se registra no servidor raiz.

print("[INFO] Iniciando servidor de nomes na porta {}.".format(args.port))
server.start() # Inicia o servidor.