import rpyc
from rpyc.utils.server import ThreadedServer
import socket

from directory_server import DirectoryServer
import const

server = DirectoryServer()
server.server_name = const.DIR_NAME_A # Define o nome do servidor de nomes.
server = ThreadedServer(server, port=const.DIR_PORT_A) # Define a porta para o servidor.

local_ip = socket.gethostbyname(socket.gethostname()) # Encontra o IP local.
address = (local_ip, const.DIR_PORT_A) # Empacota endereço ip e porta em uma tupla.

root_conn = rpyc.connect(const.ROOT_IP, const.ROOT_PORT) # Estabelece conexão com o servidor de nomes raiz.
root_conn.root.register(const.DIR_NAME_A, address) # Se registra no servidor raiz.

server.start() # Inicia o servidor.