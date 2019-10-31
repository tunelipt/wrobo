import time


import xmlrpc.client



class RoboClient:
    """Define todas as funcoes desempenhadas pelo robo, garantindo a comunicacao
    entre a interface e o terminal acr1505"""
    
    def __init__(self):
        self.url = None
        self.robo = None
        self.connected = False
        

    def connect(self, ip='localhost', port=9595):
        self.url = 'http://{}:{}'.format(ip, port)
        self.robo = xmlrpc.client.ServerProxy(self.url)

        try:
            if self.robo.ping() == 123:
                self.connected = True
                return True
            else:
                return False
        except:
            return False
        
        return False
    
    def move(self, x='', y='', z='', a=False, r=False, sync=False):
        """Inicializa a movimentacao do robo verificando todos os eixos
        
        O parametro s define o comando incremental na linguagem acr"""
        self.robo.move(x, y, z, a, r, sync)
        
    def rmove(self, x='', y='', z='', sync=False):
        return self.move(x=x, y=y, z=z, r=True, sync=sync)
    
    def moveX(self, x, a=False, r=False, sync=False):
        return self.move(x, '', '', a, r, sync)

    def moveY(self, y, a=False, r=False, sync=False):
        return self.move('', y, '', a, r, sync)

    def moveZ(self, z, a=False, r=False, sync=False):
        return self.move('', '', z, a, r, sync)

    def rmoveX(self, x, sync=False):
        return self.move(x, '', '', False, True, sync)
    
    def rmoveY(self, y, sync=False):
        return self.move('', y, '', False, True, sync)
    
    def rmoveZ(self, z, sync=False):
        return self.move('', '', z, False, True, sync)
        
    def abs_position(self, pulses=False):
        """Indica a posicao atual absoluta do robo de acordo com os parametros de posicao definidos inicialmente"""
        return self.robo.abs_position(pulses)
    
    
    def position(self):
        """Indica a posicao atual do robo de acordo com os parametros de posicao definidos inicialmente"""
        return self.robo.position()
    
    def set_reference(self, xref=0, yref=0, zref=0, eixo=''):

        self.robo.set_reference(xref, yref, zref, eixo)
        return
    def set_abs_reference(self):
        """Define a posicao de referencia absoluta"""
        self.robo.set_abs_reference()
        return
        
    def hard_zero(self, axis=None):
        """Zera o parametro de posicao para os tres eixos"""
        self.robo.hard_zero(axis)
        return None
    
    def home(self, sinal, eixo):
        """Posiciona o robo no eixo x nos sensores de homing instalados, 
        os valores 0 e 7 passados para a funcao waitHome sao bits de entrada
        definidos pelo hardware da placa ACR1505"""

        self.robo.home(sinal, eixo)
        return None

    def homeX(self, sinal='+'):
        self.robo.homeX(sinal)
        return None
    
    def homeY(self, sinal='-'):
        self.robo.homeY(sinal)
        return None
    
    def homeZ(self, sinal='+'):
        self.robo.homeZ(sinal)
        return None
    
    def stop(self):
        """Para toda a movimentacao imediatamente"""
        self.robo.stop()
        return None
    
    def stopnow(self):
        return self.stop()
    
    def clear(self):
        r = self.robo.clear()
        return r
    
    def waitUntilDone(self, dt=0.3, tmax=200):
        """Aguarda a execucao do comando ate a posicao indicada no ultimo comando"""
        return self.robo.waitUntilDone(dt, tmax)
    
    def ping(self):
        
        return self.robo.ping()
    
    
