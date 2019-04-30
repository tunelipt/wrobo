import acr1505
import time
import re
import roboxmlrpc

class AcrException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)



class Eixo:
    """Define um eixo geral para a sua identificacao e configuracao"""
    def __init__(self, nome, passo, parametro):
        self.nome = nome
        self._id = nome
        self._passo = passo
        self._parametro = parametro
        self.lim_i = ''
        self.lim_s = ''


class Robo:
    """Define todas as funcoes desempenhadas pelo robo, garantindo a comunicacao
    entre a interface e o terminal acr1505"""
    
    def __init__(self, passommX=1405.0, passommY=469.17, passommZ=1975.0, 
                 PX = 'P12544', PY = 'P12288', PZ = 'P12800'):
        """Define as variaveis de posicao de cada um dos eixos do robo
       
        Keyword arguments:
            passommX -- numero de calibracao para eixo X (passos/mm)
            passommY -- numero de calibracao para eixo Y (passos/mm)
            passommZ -- numero de calibracao para eixo Z (passos/mm)
        
        Inicia o terminal para a passagem dos comandos por acr1505.Terminal()
        Define os parametros de posicao referentes aos eixos de acordo com a linguagem acr"""
        self.con = acr1505.Terminal()
        self.eixo1 = Eixo('X', passommX, PX)
        self.eixo2 = Eixo('Y', passommY, PY)
        self.eixo3 = Eixo('Z', passommZ, PZ)
        self.SX = self.eixo1._passo
        self.SY = self.eixo2._passo
        self.SZ = self.eixo3._passo
        self.PX = self.eixo1._parametro
        self.PY = self.eixo2._parametro
        self.PZ = self.eixo3._parametro
        self.x0 = 0.0
        self.y0 = 0.0
        self.z0 = 0.0
        self.connect()
        self.initHome()
        
    def initHome(self):
        home = self.sendData("""JOG VEL X15 Y15 Z15\r
        JOG ACC X20 Y20 Z20\r
        JOG DEC X30 Y30 Z30\r
        """)
        return home
    
    def connect(self, transp=1, board=0):
        """Estabelece a conexao a partir do terminal e inicializa o canal pelo prompt do programa"""
        self.con.Connect(transp, board)
        self.isconnected = True
        reply = self.sendData("PROG 0\r")
        reply = self.sendData("ECHO 0\r")
        self.initHome()
        p = self.abs_position()
        self.x0 = p['x']
        self.y0 = p['y']
        self.z0 = p['z']
        
        return reply
    
    def get_reply(self, wait=0.3):
        """Executa a leitura do terminal"""
        if not self.isconnected:
            raise AcrException("Python interface not connected")
        reply = ''
        while True:
            time.sleep(wait)
            tmp = self.con.Read()
            if tmp == '':
                break
            reply += tmp
        return reply
        
    def move(self, x='', y='', z='', a='', r=False, sync=False):
        """Inicializa a movimentacao do robo verificando todos os eixos
        
        O parametro s define o comando incremental na linguagem acr"""
        if not self.isconnected:
            raise AcrException("Python interface not connected")
        bit = ''
        msg = ''
        if r:
            s = '/'
        else:
            s = ''
            if self.eixo1.lim_s and self.eixo2.lim_s and self.eixo3.lim_s:
                if x > self.eixo1.lim_s or x < self.eixo1.lim_i:
                    print('Fora dos limites definidos para o eixo ' + self.eixo1.nome)
                    return None
                if y > self.eixo2.lim_s or y < self.eixo2.lim_i:
                    print('Fora dos limites definidos para o eixo ' + self.eixo2.nome)
                    return None
                if z > self.eixo3.lim_s or z < self.eixo3.lim_i:
                    print('Fora dos limites definidos para o eixo ' + self.eixo3.nome)
                    return None
        if a:
            x0 = 0.0
            y0 = 0.0
            z0 = 0.0	
        else:
            x0 = self.x0
            y0 = self.y0
            z0 = self.z0
        
        if x != '':
            xx = x
            if not r:
                xx += x0
            bit_x = self.bit("X", xx, x0, r)
            bit += bit_x
            msg += ' X' + s + str(-xx)
		
        if y != '':
            yy = y
            if not r:
                yy += y0
            bit_y = self.bit("Y", -yy, y0, r)
            bit += "OR " + bit_y
            msg += ' Y' + s + str(-yy)
		
        if z != '':
            zz = z
            if not r:
                zz += z0
            bit_z = self.bit("Z", zz, z0, r)
            bit += "OR " + bit_z
            msg += ' Z' + s + str(-zz)

        msg += "\r"
        bit = re.search(r"B.*$", bit)
        bit = bit.group(0)
        
        rep = self.EOT(msg, bit)
        
        if sync:
            self.waitUntilDone()
        return rep
    
    def rmove(self, x='', y='', z='', sync=False):
        """Inicializa a movimentacao incremental do robo verificando todos os eixos"""
        p = self.position()
        if self.eixo1.lim_s and self.eixo2.lim_s and self.eixo3.lim_s:
            if p['x']+x > self.eixo1.lim_s or p['x']+x < self.eixo1.lim_i:
                print('Fora dos limites definidos para o eixo ' + self.eixo1.nome)
                return None
            if p['y']+y > self.eixo2.lim_s or p['y']+y < self.eixo2.lim_i:
                print('Fora dos limites definidos para o eixo ' + self.eixo2.nome)
                return None
            if p['z']+z > self.eixo3.lim_s or p['z']+z < self.eixo3.lim_i:
                print('Fora dos limites definidos para o eixo ' + self.eixo3.nome)
                return None
        return self.move(x=x, y=y, z=z, r=True, sync=sync)
    
        
    def abs_position(self, pulses=False):
        """Indica a posicao atual absoluta do robo de acordo com os parametros de posicao definidos inicialmente"""
        
        if not self.isconnected:
            raise AcrException("Python interface not connected")
        
        charfound = True
        while charfound:
            try:
                self.con.Write("PRINT " + self.PX + ", " + self.PY + ", " + self.PZ + "\r")
                r = self.get_reply()
                pts = [int(x) for x in r.splitlines()[0].split()]
                charfound = False
            except:
                while self.get_reply() != '':
                    time.sleep(0.1)
                charfound = True
            
        if pulses:
            return pts
        else:
            return dict(x=-pts[0]/self.SX, y=-pts[1]/self.SY, z=-pts[2]/self.SZ)
    
    def position(self):
        """Indica a posicao atual do robo de acordo com os parametros de posicao definidos inicialmente"""
        p = self.abs_position()
        return dict(x=p['x']-self.x0, y=p['y']-self.y0, z=p['z']-self.z0)
    
    def set_reference(self, xref=0, yref=0, zref=0, eixo=''):
        """Define a posicao de referencia"""
        
        if self.eixo1.lim_i and self.eixo1.lim_s:
            self.eixo1.lim_i -= self.position['x'] 
            self.eixo1.lim_s -= self.position['x']
        if self.eixo2.lim_i and self.eixo2.lim_s:
            self.eixo2.lim_i -= self.position['y'] 
            self.eixo2.lim_s -= self.position['y']
        if self.eixo3.lim_i and self.eixo3.lim_s:
            self.eixo3.lim_i -= self.position['z'] 
            self.eixo3.lim_s -= self.position['z']
        p = self.abs_position()
        if eixo == 'X' or eixo == '':
            self.x0 = p['x'] - xref
        if eixo == 'y' or eixo == '':
            self.y0 = p['y'] - yref
        if eixo == 'Z' or eixo == '':
            self.z0 = p['z'] - zref
    def set_abs_reference(self):
        """Define a posicao de referencia absoluta"""
        
        if self.eixo1.lim_i and self.eixo1.lim_s:
            self.eixo1.lim_i -= self.position['x'] 
            self.eixo1.lim_s -= self.position['x']
        if self.eixo2.lim_i and self.eixo2.lim_s:
            self.eixo2.lim_i -= self.position['y'] 
            self.eixo2.lim_s -= self.position['y']
        if self.eixo3.lim_i and self.eixo3.lim_s:
            self.eixo3.lim_i -= self.position['z'] 
            self.eixo3.lim_s -= self.position['z']
        self.x0 = 0.0
        self.y0 = 0.0
        self.z0 = 0.0
            
        
    def hard_zero(self):
        """Zera o parametro de posicao para os tres eixos"""
        
        self.con.Write(self.PX + '= 0')
        self.con.Write(self.PY + '= 0')
        self.con.Write(self.PZ + '= 0')
        
        return self.get_reply()
    
    def home(self, sinal, eixo):
        """Posiciona o robo no eixo x nos sensores de homing instalados, 
        os valores 0 e 7 passados para a funcao waitHome sao bits de entrada
        definidos pelo hardware da placa ACR1505"""
        eixo = eixo.upper()
        if sinal == "+":
            bit = self.bit(axis = eixo, side = sinal)
            bit = bit.replace('BIT', '')
            rep = self.waitHome("JOG REV "+eixo+"\r", bit, eixo)
        elif sinal == "-":
            if eixo == "Z":
                return None
            elif eixo == "X" or eixo == "Y":
                bit = self.bit(axis = eixo, side = sinal)
                bit = bit.replace('BIT', '')
                rep = self.waitHome("JOG FWD "+eixo+"\r", bit, eixo)
        return rep
    
    def stop(self):
        """Para toda a movimentacao imediatamente"""
        
        r = self.sendData("HALT ALL\r")
        r = self.sendData("JOG OFF X Y Z\r")
        time.sleep(1)
        self.clear()
        return r
    
    def clear(self):
        r = self.sendData("CLEAR\r")
        return r
    
    def waitUntilDone(self):
        """Aguarda a execucao do comando ate a posicao indicada no ultimo comando"""
        if not self.isconnected:
            raise AcrException("Python interface not connected")
        self.sendData("INH -516\r")
    
    def disconnect(self):
        """Desconecta o programa do terminal"""
        if self.isconnected:
            self.con.Disconnect()

        return None
    
    def sendData(self, message):
        """Envia os comandos para ACR1505"""
        self.con.Write(message)
        reply = self.get_reply()
        
        return reply
    
    def waitHome(self, msg, bit, axis):
        """Envia a rotina para verificar se o homing referente ao eixo selecionado
        e ao respectivo BIT foi bem sucedido e define como nova referencia de posicionamento"""
        rep = self.sendData("""PROGRAM\r
		                IF (NOT BIT"""+ bit + """)\r
                        """ + msg + """
		                PRINT "Homing "\r
                        INH +""" + bit + """
						JOG OFF X Y Z\r
                        ENDIF\r
                        PRINT " Home Found"\r
						ENDP\r
                        """)
        self.sendData("RUN\r")
        if axis == "X":
            self.sendData("IF (" + bit + ") THEN"+ self.PX +"= 0\r")
            self.x0 = 0.0
            self.set_reference(eixo='X')
            if bit == '0':
                self.eixo1.lim_i = -5300
                self.eixo1.lim_s = 0
            elif bit == '7':
                self.eixo1.lim_i = 0
                self.eixo1.lim_s = 5300
        if axis == "Y":
            self.sendData("IF (" + bit + ") THEN"+ self.PY +"= 0\r")
            self.y0 = 0.0
            self.set_reference(eixo='Y')
            if bit == '3':
                self.eixo1.lim_i = -2600
                self.eixo1.lim_s = 0
            elif bit == '13':
                self.eixo1.lim_i = 0
                self.eixo1.lim_s = 2600
        if axis == "Z":
            self.sendData("IF (" + bit + ") THEN"+ self.PZ +"= 0\r")
            self.z0 = 0.0
            self.set_reference(eixo='Z')
            if bit == '5':
                self.eixo1.lim_i = -500
                self.eixo1.lim_s = 0
        return rep
        
    def EOT(self, distance, bit):
        """Envia a rotina para verificar se o fim de curso referente ao eixo em movimento
        e ao respectivo BIT foi acionado, encerrando o movimento em caso positivo"""
        self.sendData("""PROGRAM\r
		          IF (NOT """ + bit + """)\r
				  """ + distance +"""
				  ENDIF\r
				  WHILE (BIT516)\r
				  PRINT "ON MOVE "\r
				  IF (""" + bit + """)\r
				  PRINT " Stop Moving"\r
				  HALT ALL\r
				  BREAK\r
				  ENDIF\r
				  PRINT " Dwell for .1 second"\r
				  DWL 0.1\r
				  WEND\r
				  ENDP\r
				  """)
        self.sendData("RUN\r")

    def bit(self, axis, x = 0, x0 = 0, r = False, side = ''):
        """Retorna o BIT que deverá ser analisado pelo programa de acordo com o eixo e
        o tipo de movimento a ser executado"""
        if r:
            x0 = 0.0
        if side:
            if side == '+':
                bit = {"X": "BIT0", "Y": "BIT13", "Z": "BIT5"}
            else: #side == '-':
                bit = {"X": "BIT7", "Y": "BIT3", "Z": "BIT14"}
        else:
            if x >= x0:
                bit = {"X": "BIT0", "Y": "BIT3", "Z": "BIT5"}
            else: # x < x0:
                bit = {"X": "BIT7", "Y": "BIT13", "Z": "BIT14"}
        return bit[axis]
    def ping(self):
        return 123
    
    
if __name__ == "__main__":
    print("Creating server ...")
    
    roboxmlrpc.start_server(ip = 'localhost', port = '9595')
