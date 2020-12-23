import rpyc
from rpyc.utils.server import ThreadedServer
import argparse
import socket

from directory_server import DirectoryServer

parser = argparse.ArgumentParser(description="Inicia o servidor de nomes raiz.")
parser.add_argument("port", type=int, help="Porta na qual o servidor deve ouvir.")

args = parser.parse_args()
local_ip = socket.gethostbyname(socket.gethostname())
newText = ''

with open("const_original.py", "r") as f:
	newText = f.read()
	newText = newText.replace('<root_ip_placeholder>', local_ip)
	newText = newText.replace('\'<root_port_placeholder>\'', str(args.port))

with open("const.py", "w") as f:
	f.write(newText)


import const

root_server = ThreadedServer(DirectoryServer, port=int(const.ROOT_PORT))
root_server.start()
