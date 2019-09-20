
class Robo:
    """Define todas as funcoes desempenhadas pelo robo, garantindo a comunicacao
    entre a interface e o terminal acr1505"""
    
    def __init__(self, passommX=1405.0, passommY=469.17, passommZ=1975.0, 
                 PX = 'P12544', PY = 'P12288', PZ = 'P12800'):
        self.x = 0
        self.y = 0
        self.z = 0

        self.x0 = 0
        self.y0 = 0
        self.z0 = 0

    def connect(self):
        print("connect()")
        return None
    
    def move(self, x='', y='', z='', a='', r=False, sync=False):
        """Inicializa a movimentacao do robo verificando todos os eixos
        
        O parametro s define o comando incremental na linguagem acr"""
        print("move(x={}, y={}, z={}, a={}, r={}, sync={})".format(x, y, z, a, r, sync))
        if r:
            if x != '':
                self.x += x
            if y != '':
                self.y += y
            if z != '':
                self.z += z
        elif a:
            if x != '':
                self.x = x
            if y != '':
                self.y = y
            if z != '':
                self.z = z
        else:
            if x != '':
                self.x = x + self.x0
            if y != '':
                self.y = y + self.y0
            if z != '':
                self.z = z + self.z0
            
        return None
    
    def rmove(self, x='', y='', z='', sync=False):
        """Inicializa a movimentacao incremental do robo verificando todos os eixos"""
        print("move(x={}, y={}, z={}, sync={})".format(x, y, z, sync))
        self.move(x=x, y=y, z=z, a=False, r=True, sync=sync)
        return None
    
        
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
        """
        Indica a posicao atual absoluta do robo de acordo com os
        parametros de posicao definidos inicialmente
        """
        pos = dict(x=self.x, y=self.y, z=self.z)
        print("abs_position() -> x={}, y={}, z={}".format(pos['x'], pos['y'], pos['z']))
        return pos
    
    
    def position(self):
        """Indica a posicao atual do robo de acordo com os parametros de posicao definidos inicialmente"""
        p = self.abs_position()
        pos = dict(x=p['x']-self.x0, y=p['y']-self.y0, z=p['z']-self.z0)
        print("position() -> x={}, y={}, z={}".format(pos['x'], pos['y'], pos['z']))
        return pos
    
    def set_reference(self, xref=0, yref=0, zref=0, eixo=''):
        """Define a posicao de referencia"""

        print("set_reference(xref={}, yref={}, zref={}, eixo={})".format(xref, yref, zref, eixo))
        p = dict(x=self.x, y=self.y, z=self.z)
        if eixo == 'X' or eixo == '':
            self.x0 = p['x'] - xref
        if eixo == 'y' or eixo == '':
            self.y0 = p['y'] - yref
        if eixo == 'Z' or eixo == '':
            self.z0 = p['z'] - zref
        return None
    
    def set_abs_reference(self):
        print("set_abs_reference()")
        self.x0 = 0.0
        self.y0 = 0.0
        self.z0 = 0.0
        return None
        
    def hard_zero(self):
        """Zera o parametro de posicao para os tres eixos"""
        print("hard_zero()")
        self.x = 0
        self.y = 0
        self.z = 0
        return None
    
    def home(self, sinal, eixo):
        """Posiciona o robo no eixo x nos sensores de homing instalados, 
        os valores 0 e 7 passados para a funcao waitHome sao bits de entrada
        definidos pelo hardware da placa ACR1505"""
        eixo = eixo.upper()
        print("home(sinal={}, eixo={}".format(sinal, eixo))
        self.waitHome("HOME", 0, eixo)
        return None
    def homeX(self, sinal='+'):
        return self.home(sinal, 'X')
    
    def homeY(self, sinal='-'):
        return self.home(sinal, 'Y')
    
    def homeZ(self, sinal='+'):
        return self.home('+', 'Z')
    
    def stop(self):
        """Para toda a movimentacao imediatamente"""
        print("stop()")
        return None

    def stopnow(self):
        return self.stop()
    
    def clear(self):
        print("clear()")
        return None
    
    def waitUntilDone(self, dt=0.3, tmax=200):
        print("waitUntilDone()")
        return None
    
    def disconnect(self):
        """Desconecta o programa do terminal"""
        print("disconnect()")
        return None
    
    
    def waitHome(self, msg, bit, axis):
        """Envia a rotina para verificar se o homing referente ao eixo selecionado
        e ao respectivo BIT foi bem sucedido e define como nova referencia de posicionamento"""

        print("waitHome(msg={}, bit={}, axis={})".format(msg, bit, axis))
        if axis == "X":
            self.x0 = 0
            self.x = 0
        if axis == "Y":
            self.y0 = 0
            self.y = 0
        if axis == "Z":
            self.z0 = 0
            self.z = 0
        return None
    def ping(self):
        return 123
    
        
    
