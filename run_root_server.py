import rpyc
from rpyc.utils.server import ThreadedServer

import directory_server

root_server = ThreadedServer(DirectoryServer, port=const.DIR_PORT)
root_server.start()
