
import argparse
from xmlrpc.server import SimpleXMLRPCServer

def start_server(test=False, ip = "localhost", port  = "9595"):
    """Inicializa o servidor relacionando-o a uma instancia importada de um arquivo externo
    
    Keyword arguments:
    ip -- endereco do servidor
    port -- porta do servidor"""
    if test:
        import roboteste as robo
    else:
        import robo
    
    r = robo.Robo()
    ip = ip
    port = port
    print("Connecting to ACR1505...")
    r.connect()
    print("Starting XML-RPC server: IP={}, Port={} ...".format(ip, port))
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
    parser = argparse.ArgumentParser(description="wrobo")
    parser.add_argument("-t", "--test", help="Interface teste do robo cartesiano do túnel de vento",
                        action="store_true")
    parser.add_argument("-i", "--ip", help="Endereço IP do servidor XML-RPC", default="localhost")
    parser.add_argument("-p", "--port", help="Porta XML-RPC do servidor XML-RPC", default=9595, type=int)
    parser.add_argument("-n", "--serverless", help="Não inicie o servidor XML-RPC", action="store_true")
    parser.add_argument("-c", "--client", help="Criar interface para cliente de servidor XML-RPC",
                        action="store_true")

    args = parser.parse_args()
    start_server(args.test, args.ip, args.port)   
