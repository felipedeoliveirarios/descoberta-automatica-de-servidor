import rpyc
from rpyc.utils.server import ThreadedServer

from directory_server import DirectoryServer
import const

root_server = ThreadedServer(DirectoryServer, port=const.ROOT_PORT)
root_server.start()
