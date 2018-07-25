import robo

from xmlrpc.server import SimpleXMLRPCServer

def start_server(ip = "localhost", port  = "9595"):
    """Inicializa o servidor relacionando-o a uma instancia importada de um arquivo externo
    
    Keyword arguments:
    ip -- endereco do servidor
    port -- porta do servidor"""
    
    r = robo.Robo()
    ip = ip
    port = port
    print("Connecting to ACR1505...")
    r.connect()
    print("Starting XML-RPC server...")
    srvr = RoboServer(r, ip, port)
    srvr.start()

class RoboServer:
    """Cria a instancia do servidor responsavel pela comunicacao XML-RPC com o robo"""
    
    def __init__(self, robo, ip, port):
        self.robo=robo
        self.ip=ip
        self.port=int(port)
        
    def start(self):
        print("Starting XML-RPC Server...")
        #self.server = SimpleXMLRPCServer(("192.168.0.103", 9595), allow_none=True)
        self.server = SimpleXMLRPCServer((self.ip, self.port), allow_none=True)
        self.server.register_instance(self.robo)
        print("Serving XML-RPC...")
        self.server.serve_forever()


if __name__ == "__main__":
    print("Creating interface ...")
    start_server()   
