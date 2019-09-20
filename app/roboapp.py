#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:01:55 2017

@author: ipt


Para a execucao do codigo em Android usamos o framework Pydroid 3, junto ao Ministro II.
"""

import sys
from PyQt5.QtWidgets import (QLabel, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QSplashScreen,
                             QGroupBox, QPushButton, QApplication, QSlider, QMainWindow, qApp, QLineEdit, QAction)
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QPixmap, QIcon, QRegExpValidator
import time

class RelativeMove(QWidget):
    """Classe criada a partir da classe QWidget, 
    para gerar a interface responsavel pelos botoes
    de movimentacao relativa"""
    
    def __init__(self, parent=None):
        """Funcao __init__ para definir o layout geral"""
        
        super(RelativeMove, self).__init__(parent)
        column = QVBoxLayout()
        column.addWidget(self.interface())
        
        self.setLayout(column)
        
        
    def interface(self):
        """interface gera os botoes para o movimento relativo e define como serao 
        dispostos de acordo com um *grid layout* dentro do *group box* criado"""
    
        relgroup = QGroupBox('Movimento Relativo')
        
        grid = QGridLayout() 
        
        names = ['', 'Y+', '', '', 'Z+',
                 'X-', '', 'X+', '', '',
                 '', 'Y-', '', '', 'Z-']
        
        position = [(i,j) for i in range(1,4) for j in range(5)]
        
        self.rmoveButtons = []
        
        for position, name in zip(position, names):
            
            if name == '':
                continue
            button = "button" + name
            button = QPushButton(name)
            button.setMaximumWidth(40)
            button.setMinimumHeight(40)
            self.rmoveButtons.append(button)
    
            grid.addWidget(button, *position)

        relgroup.setLayout(grid)
        
        return relgroup

class StepMove(QWidget):
    """Classe criada a partir da classe QWidget, 
    para gerar a interface responsavel pelo passo da
    movimentacao relativa"""
    
    def __init__(self, parent=None):
        """Funcao __init__ para definir o layout geral"""
        
        super(StepMove, self).__init__(parent)
        column = QVBoxLayout()
        column.addWidget(self.interface())
        
        self.setLayout(column)
        
        
    def interface(self):
        """interface gera os botoes para o passo do movimento relativo e define como serao 
        dispostos de acordo com *Box Layouts* dentro do *group box* criado.
        
        Os passos são definidos pelos valores dos *sliders* associados a cada uma das coordenadas
        """
            
        stepgroup = QGroupBox('Step')
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()

        #Definicao do sliderx
        self.sliderx = QSlider(Qt.Horizontal, self)
        self.sliderx.setFocusPolicy(Qt.StrongFocus)

        self.sliderx.setTickPosition(QSlider.TicksBothSides)
        self.sliderx.setTickInterval(50)
        self.sliderx.setSingleStep(10)
        self.sliderx.setValue(10)
        self.sliderx.setMinimum(0)
        self.sliderx.setMaximum(500)

        self.labelx = QLabel('10')
        self.labelx.setMinimumHeight(40)
        self.labelx.setAlignment(Qt.AlignCenter)
        stepx = QLabel("X")
        
        self.entrada_x = QLineEdit(self)
        self.entrada_x.setText('0')
        regex = QRegExp("\d{0,3}(\.\d{0,3})?")
        validator=QRegExpValidator(regex, self.entrada_x)
        
        self.entrada_x.setValidator(validator)
        
        vbox.addWidget(self.labelx)
        vbox.addLayout(hbox1)
        hbox1.addWidget(stepx,0.5)
        hbox1.addWidget(self.sliderx,6)
        hbox1.addWidget(self.entrada_x,1)
        
        self.entrada_x.textChanged[str].connect(lambda text: self.changeCursor(text, self.sliderx))
        self.sliderx.valueChanged[int].connect(lambda value: self.changeValue(value, self.labelx,
                                                                              self.entrada_x))
        self.sliderx.setMinimumHeight(40)
        
        #Definicao do slidery
        self.slidery = QSlider(Qt.Horizontal, self)
        self.slidery.setFocusPolicy(Qt.StrongFocus)
        self.slidery.setTickPosition(QSlider.TicksBothSides)
        self.slidery.setTickInterval(25)
        self.slidery.setSingleStep(10)
        self.slidery.setValue(10)
        self.slidery.setMinimum(0)
        self.slidery.setMaximum(500)

        self.labely = QLabel('10')
        self.labely.setMinimumHeight(30)
        self.labely.setAlignment(Qt.AlignCenter)
        stepy = QLabel("Y")
        
        self.entrada_y = QLineEdit(self)
        self.entrada_y.setText('0')
        validator=QRegExpValidator(regex, self.entrada_y)
        
        vbox.addWidget(self.labely)
        vbox.addLayout(hbox2)
        hbox2.addWidget(stepy,0.5)
        hbox2.addWidget(self.slidery,6)
        hbox2.addWidget(self.entrada_y,1)
        
        self.entrada_y.textChanged[str].connect(lambda text: self.changeCursor(text, self.slidery))
        self.slidery.valueChanged[int].connect(lambda value: self.changeValue(value, self.labely,
                                                                              self.entrada_y))
        self.slidery.setMinimumHeight(40)
        
        
        #Definicao do sliderz
        self.sliderz = QSlider(Qt.Horizontal, self)
        self.sliderz.setFocusPolicy(Qt.StrongFocus)
        self.sliderz.setTickPosition(QSlider.TicksBothSides)
        self.sliderz.setTickInterval(10)
        self.sliderz.setSingleStep(10)
        self.sliderz.setValue(10)
        self.sliderz.setMinimum(0)
        self.sliderz.setMaximum(200)
        
        self.labelz = QLabel('10')
        self.labelz.setMinimumHeight(40)
        self.labelz.setAlignment(Qt.AlignCenter)
        stepz = QLabel("Z")
        
        self.entrada_z = QLineEdit(self)
        self.entrada_z.setText('0')
        validator=QRegExpValidator(regex, self.entrada_z)
        
        vbox.addWidget(self.labelz)
        vbox.addLayout(hbox3)
        hbox3.addWidget(stepz,0.5)
        hbox3.addWidget(self.sliderz,6)
        hbox3.addWidget(self.entrada_z,1)
        
        self.entrada_z.textChanged[str].connect(lambda text: self.changeCursor(text, self.sliderz))
        self.sliderz.valueChanged[int].connect(lambda value: self.changeValue(value, self.labelz,
                                                                              self.entrada_z))
        self.sliderz.setMinimumHeight(40)

        stepgroup.setLayout(vbox)
        self.resize(150, 250)
        return stepgroup
    
    
    def changeCursor(self, text, sliders):
        """changeValue toma os valores dos *line edits* a cada alteracao feita e repassa para o valor
        dos *sliders* respectivas.
        
        Keyword arguments:
        value -- o valor referente ao *line edit* alterado
        sliders -- o *slider* a ser modificado
        """
        
        slider = sliders
        if text:
            slider.setValue(float(text))
        
    def changeValue(self, value, labels):
        """changeValue toma os valores dos *sliders* a cada alteracao feita e repassa para o texto
        das *labels* respectivas.
        
        Keyword arguments:
        value -- o valor referente ao *slider* alterado
        lables -- o *label* a ser modificado
        """
        
        label = labels
        label.setText(str(value))
        
class Reference(QWidget):
    """Classe criada a partir da classe QWidget, 
    para gerar a interface responsavel pela definicao
    das referencias do robo"""
    
    def __init__(self, parent=None):
        """Funcao __init__ para definir o layout geral"""
        
        super(Reference, self).__init__(parent)
        column = QVBoxLayout()
        column.addWidget(self.interface())
        
        self.setLayout(column)
        
        
    def interface(self):
        """interface gera os botoes para a definicao da referencia do robo e define como serao 
        dispostos de acordo com *Box Layouts* dentro do *group box* criado.
        """
        
        refgroup = QGroupBox('Referencia')
        
        vbox = QVBoxLayout()
        
        self.buttonref = QPushButton("Ponto atual como referencia")
        self.buttonabsref = QPushButton("Referencia absoluta")
        vbox.addWidget(self.buttonref)
        vbox.addWidget(self.buttonabsref)
        refgroup.setLayout(vbox)
        
        return refgroup


class Home(QWidget):
    """Classe criada a partir da classe QWidget, 
    para gerar a interface responsavel por ordenar o robo
    a tomar a posição de referencia"""
    
    def __init__(self, parent=None):
        """Funcao __init__ para definir o layout geral"""
        
        super(Home, self).__init__(parent)
        column = QVBoxLayout()
        column.addWidget(self.interface())
        
        self.setLayout(column)
        
    def interface(self):        
        """interface gera os botoes para enviar o robo para a posição de referencia e define como serao 
        dispostos de acordo com *Box Layouts* dentro do *group box* criado.
        """
        
        homegroup = QGroupBox('Home')
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        
        self.buttonx1 = QPushButton("Home X-")
        self.buttonx2 = QPushButton("Home X+")
        self.buttony1 = QPushButton("Home Y-")
        self.buttony2 = QPushButton("Home Y+")
        self.buttonz1 = QPushButton("Home Z-")
        self.buttonz2 = QPushButton("Home Z+")
        self.buttonall1 = QPushButton("Home TODOS-")
        self.buttonall1.setMinimumHeight(50)
        self.buttonall2 = QPushButton("Home TODOS+")
        self.buttonall2.setMinimumHeight(50)
        
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        hbox1.addWidget(self.buttonx1)
        hbox1.addWidget(self.buttonx2)
        hbox2.addWidget(self.buttony1)
        hbox2.addWidget(self.buttony2)
        hbox3.addWidget(self.buttonz1)
        hbox3.addWidget(self.buttonz2)
        hbox4.addWidget(self.buttonall1)
        hbox4.addWidget(self.buttonall2)
        homegroup.setLayout(vbox)
        
        return homegroup


class Move(QWidget):
    """Classe criada a partir da classe QWidget, 
    para gerar a interface responsavel pela
    movimentação do robo para um ponto específico"""
    
    def __init__(self, parent=None):
        """Funcao __init__ para definir o layout geral"""
        
        super(Move, self).__init__(parent) 
        column = QVBoxLayout()
        column.addWidget(self.interface())
        
        self.setLayout(column)
        
        
    def interface(self):
        """interface gera os botoes para enviar o robo para uma posição específica e define como serao 
        dispostos de acordo com *Box Layouts* dentro do *group box* criado.
        
        Os valores dessa posição são definidos por *sliders* referentes a cada coordenada.
        """
        
        movegroup = QGroupBox("Movimento")
        
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        
        self.button = QPushButton("Mover")
        self.button.setMinimumHeight(50)
        vbox.addWidget(self.button)

        #Definicao do sliderx
        self.slidermx = QSlider(Qt.Horizontal, self)
        self.slidermx.setFocusPolicy(Qt.StrongFocus)
        self.slidermx.setSingleStep(10)
        self.slidermx.setValue(0)
        self.slidermx.setMinimum(-1000)
        self.slidermx.setMaximum(1000)
        
        self.move_x = QLineEdit(self)
        self.move_x.setText('0')
        regex = QRegExp("-?\d{0,4}(\.\d{0,4})?")
        validator=QRegExpValidator(regex, self.move_x)
        
        self.move_x.setValidator(validator)
        
        self.posx = QLabel('0')
        self.posx.setAlignment(Qt.AlignCenter)
        labelx = QLabel("X")
        labelx.setMinimumHeight(40)

        vbox.addWidget(self.posx)
        vbox.addLayout(hbox1)
        hbox1.addWidget(labelx,0.5)
        hbox1.addWidget(self.slidermx,6)
        hbox1.addWidget(self.move_x,1)
        
        self.move_x.textChanged[str].connect(lambda text: self.changeCursor(text, self.slidermx))
        self.slidermx.valueChanged[int].connect(lambda value: self.changeValue(value, self.posx))
        self.slidermx.setMinimumHeight(40)
        
        #Definicao do slidery
        self.slidermy = QSlider(Qt.Horizontal, self)
        self.slidermy.setFocusPolicy(Qt.StrongFocus)
        self.slidermy.setSingleStep(10)
        self.slidermy.setValue(0)
        self.slidermy.setMinimum(-2500)
        self.slidermy.setMaximum(2500)
        
        self.move_y = QLineEdit(self)
        self.move_y.setText('0')
        validator=QRegExpValidator(regex, self.move_y)
        
        self.move_y.setValidator(validator)
        
        self.posy = QLabel('0')
        self.posy.setAlignment(Qt.AlignCenter)
        labely = QLabel("Y")
        labely.setMinimumHeight(40)

        vbox.addWidget(self.posy)
        vbox.addLayout(hbox2)
        hbox2.addWidget(labely,0.5)
        hbox2.addWidget(self.slidermy,6)
        hbox2.addWidget(self.move_y,1)
        
        self.move_y.textChanged[str].connect(lambda text: self.changeCursor(text, self.slidermy))
        self.slidermy.valueChanged[int].connect(lambda value: self.changeValue(value, self.posy))
        self.slidermy.setMinimumHeight(40)

        
        #Definicao do sliderz
        self.slidermz = QSlider(Qt.Horizontal, self)
        self.slidermz.setFocusPolicy(Qt.StrongFocus)
        self.slidermz.setSingleStep(10)
        self.slidermz.setValue(0)
        self.slidermz.setMinimum(-250)
        self.slidermz.setMaximum(250)

        self.move_z = QLineEdit(self)
        self.move_z.setText('0')
        validator=QRegExpValidator(regex, self.move_z)
        
        self.move_z.setValidator(validator)
        
        self.posz = QLabel('0')
        self.posz.setAlignment(Qt.AlignCenter)
        labelz = QLabel("Z")
        labelz.setMinimumHeight(40)
        
        vbox.addWidget(self.posz)
        vbox.addLayout(hbox3)
        hbox3.addWidget(labelz,0.5)
        hbox3.addWidget(self.slidermz,6)
        hbox3.addWidget(self.move_z,1)
        
        self.move_z.textChanged[str].connect(lambda text: self.changeCursor(text, self.slidermz))
        self.slidermz.valueChanged[int].connect(lambda value: self.changeValue(value, self.posz))
        self.slidermz.setMinimumHeight(40)
        
        movegroup.setLayout(vbox)
        
        return movegroup
    
    def changeCursor(self, text, sliders):
        """changeValue toma os valores dos *line edits* a cada alteracao feita e repassa para o valor
        dos *sliders* respectivas.
        
        Keyword arguments:
        value -- o valor referente ao *line edit* alterado
        sliders -- o *slider* a ser modificado
        """
        
        slider = sliders
        if text:
            if text[0] == '-' and len(text) >= 2:
                slider.setValue(-float(text[1:]))
            elif text[0] != '-':
                slider.setValue(float(text))
    
    def changeValue(self, value, labels):
        """changeValue toma os valores dos *sliders* a cada alteracao feita e repassa para o texto
        das *labels* respectivas.
        
        Keyword arguments:
        value -- o valor referente ao *slider* alterado
        lables -- o *label* a ser modificado
        """
        
        label = labels
        label.setText(str(value))
    
    
class Position(QWidget):
    """Classe criada a partir da classe QWidget, 
    para gerar a interface responsavel pela
    verificação da posição do robo"""
    
    def __init__(self, parent=None):
        """Funcao __init__ para definir o layout geral"""
        
        super(Position, self).__init__(parent)    
        #groupbox de posicao
        column = QVBoxLayout()
        column.addWidget(self.interface())
        
        self.setLayout(column)
        
        
    def interface(self):
        """interface gera os botoes para verificar a posição do robo e define como serao 
        dispostos de acordo com *Box Layouts* dentro do *group box* criado.
        """
        
        posgroup = QGroupBox('Posicao')
        
        vbox = QVBoxLayout()
        
        self.buttonpos = QPushButton("Posicao")
        self.buttonpos.setMinimumHeight(35)
        self.labelp = QLabel('')
        self.labelp.setAlignment(Qt.AlignCenter)
        
        self.buttonabspos = QPushButton("Posicao absoluta")
        self.buttonabspos.setMinimumHeight(35)
        self.labelabsp = QLabel('')
        self.labelabsp.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.buttonpos)
        vbox.addWidget(self.labelp)
        vbox.addWidget(self.buttonabspos)
        vbox.addWidget(self.labelabsp)
        posgroup.setLayout(vbox)

        return posgroup

class Stop(QWidget):
    """Classe criada a partir da classe QWidget, 
    para gerar a interface responsavel pela
    parada de emergencia"""
    
    def __init__(self, parent=None):
        """Funcao __init__ para definir o layout geral"""
        
        super(Stop, self).__init__(parent)
        column = QVBoxLayout()
        column.addWidget(self.interface())
        
        self.setLayout(column)
        
        
    def interface(self):
        """interface gera o botao para parada de emergencia e define as caracteristicas
        do botao, colocando-o dentro do *group box*.
        """
        
        stopgroup = QGroupBox("Parada")
        
        vbox = QVBoxLayout()
        
        self.buttons = QPushButton("PARADA IMEDIATA")
        self.buttons.setMinimumHeight(70)
        self.buttons.setStyleSheet("background-color: red")
        
        
        vbox.addWidget(self.buttons)
        stopgroup.setLayout(vbox)
    
        return stopgroup
    
class Clear(QWidget):
    """Classe criada a partir da classe QWidget, 
    para gerar a interface responsavel pela
    limpeza dos dados"""
    
    def __init__(self, parent=None):
        """Funcao __init__ para definir o layout geral"""
        
        super(Clear, self).__init__(parent)
        column = QVBoxLayout()
        column.addWidget(self.interface())
        
        self.setLayout(column)
        
        
    def interface(self):        
        """interface gera o botao para limpar os dados e define as caracteristicas
        do botao, colocando-o dentro do *group box*.
        """
        
        cleargroup = QGroupBox("Limpar")
        
        vbox = QVBoxLayout()
        
        self.buttonc = QPushButton("Limpar")
        vbox.addWidget(self.buttonc)
        cleargroup.setLayout(vbox)
        
        return cleargroup
        
class client_setting(QWidget):
    """client_setting exibe as entradas de texto para a definicao do endereço e porta utilizados
    pela comunicação XMLRPC"""
    
    def __init__(self):
        """Funcao __init__ para definir o layout geral"""
        
        super().__init__()
        self.title = "Configuracoes do cliente"
        
        self.textboxip = QLineEdit(self)
        self.labelip = QLabel('Endereço do Server:')
        
        self.textboxport = QLineEdit(self)
        self.labelport = QLabel('Porta:')
        
        self.button_end = QPushButton('Sair')
        self.button_conf = QPushButton('Configurar')
                
        column = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        
        column.addLayout(row1)
        row1.addWidget(self.labelip)
        row1.addWidget(self.textboxip)
        
        column.addLayout(row2)
        row2.addWidget(self.labelport)
        row2.addWidget(self.textboxport)
        
        column.addWidget(self.button_conf)
 
        column.addStretch(1)
        column.addWidget(self.button_end)
       
        self.setLayout(column)
    
class Tab1(QWidget):
    """Tab1 e responsavel pela juncao e disposicao das *Group Boxes* necessarias na primeira
    aba da interface final"""
    
    def __init__(self):
        """Funcao __init__ para definir o layout geral"""
        
        super().__init__()
        
        column1 = QVBoxLayout()
        self.relativo = RelativeMove()
        self.step = StepMove()
        self.position = Position()
        self.stop = Stop()
        
        column1.addWidget(self.relativo,1)
        column1.addWidget(self.step,2)
        column1.addWidget(self.stop,1)
        column1.addWidget(self.position,1)
        
        
        self.setLayout(column1)

class Tab2(QWidget):
    """Tab2 e responsavel pela juncao e disposicao das *Group Boxes* necessarias na segunda
    aba da interface final"""
    
    def __init__(self):
        """Funcao __init__ para definir o layout geral"""
        
        super().__init__()
        column2 = QVBoxLayout()
        self.home = Home()
        self.position = Position()
        self.stop = Stop()
        self.clear = Clear()
        
        column2.addWidget(self.home)
        column2.addWidget(self.stop)
        column2.addWidget(self.clear)
        column2.addWidget(self.position)
        

        self.setLayout(column2)
    
class Tab3(QWidget):
    """Tab3 e responsavel pela juncao e disposicao das *Group Boxes* necessarias na terceira
    aba da interface final"""
    
    def __init__(self):
        """Funcao __init__ para definir o layout geral"""
        
        super().__init__()
        
        column3 = QVBoxLayout()
        self.move = Move()
        self.position = Position()
        self.stop = Stop()
        self.clear = Clear()
                
        column3.addWidget(self.move)
        column3.addWidget(self.stop)
        column3.addWidget(self.clear)
        column3.addWidget(self.position)
        
        self.move.setMinimumSize(300,250)
        self.setLayout(column3)
        
class Tab4(QWidget):
    """Tab4 e responsavel pela juncao e disposicao das *Group Boxes* necessarias na quarta
    aba da interface final"""
    
    def __init__(self):
        """Funcao __init__ para definir o layout geral"""
        
        super().__init__()
    
        column4 = QVBoxLayout()
        self.ref = Reference()
        self.position = Position()
        self.stop = Stop()
        self.clear = Clear()
        
        column4.addWidget(self.ref)
        column4.addWidget(self.stop)
        column4.addWidget(self.clear)
        column4.addWidget(self.position)
        
        self.setLayout(column4)


class Welcome(QMainWindow):
    """Classe implementada a partir da classe QMainWindow e gera a tela inicial,
    responsavel pela configuracao inicial dos argumentos utilizados pelo XMLRPC"""
    
    def __init__(self, parent=None):
        """Funcao __init__ para definir o layout geral
        
        Keyword argumets:
        robo -- arquivo do qual chamam-se os comandos enviados ao robo
        """
        super().__init__(parent)
        self.setWindowTitle("Configurações Iniciais")
        self.setGeometry(50, 50, 350, 400)
        
        self.widget = client_setting()
        self.setCentralWidget(self.widget)
        
        self.widget.button_conf.clicked.connect(self.configurar)
        self.widget.button_end.clicked.connect(self.sair)
        
        self.setWindowIcon(QIcon('ipt.jpg'))
        
        self.show()

    def configurar(self):
        """Essa funcao e chamada pelo botao *Configurar* e toma os valores das entradas de texto
        como os novos valores de endereco e porta"""
        if self.widget.textboxip.text():
            self.ip = self.widget.textboxip.text()
        else:
            self.ip = "10.5.37.38"
            
        if self.widget.textboxport.text():
            self.port = self.widget.textboxport.text()
        else:
            self.port = 9595
            
        self.initUI(self.ip, self.port)
        self.widget.textboxip.setText('')
        self.widget.textboxport.setText('')
        

    def initUI(self, ip, port):
        """initUI fecha a janela atual e abre a interface reponsável pelos comandos ao robo,
        definindo a nova comunicação com o servidor"""
        
        global pr
        if pr:
            pr.terminate()
            time.sleep(1)

        pr = Process(target=roboxmlrpc.start_server, args=(ip, port))
        pr.start()

        self.robo = xmlrpc.client.ServerProxy("http://"+str(ip)+":"+str(port))
        self.new_wind()
        
    def new_wind(self):
        """Fecha a janela de boas vindas e inicia a janela principal"""
        self.close()
        self.win = MainWindow(self.robo)
        self.win.show()
    
    def sair(self):
        """Finaliza o processo de comunicação e encerra o aplicativo"""
        global pr
        if pr:
            pr.terminate()
        qApp.quit()
        
class MainWindow(QMainWindow):
    """Classe implementada sobre a partir da classe QMainWindow e gera a tela de comandos,
    responsavel pela disposicao final das guias"""
    
    def __init__(self, robo, parent=None):
        """Funcao __init__ para definir o layout geral
        
        Keyword argumets:
        robo -- arquivo do qual chamam-se os comandos enviados ao robo
        """
        
        self.robo = robo
        
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Movimentador do Tunel")
        self.setGeometry(50, 50, 500, 550)
        self.tab = Welcome
        
        self.table_widget = MyTableWidget(self.robo, self)
        self.setCentralWidget(self.table_widget)
        
        exitAct = QAction(QIcon('exit.png'), '&Sair', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Sair do Programa')
        exitAct.triggered.connect(self.tab.sair)
        
        configAct = QAction(QIcon('configura.jpg'), '&Configurar', self)
        configAct.setStatusTip('Configurar endereço')
        configAct.triggered.connect(self.new_wind)
       
        self.toolbar = self.addToolBar('&Configurações')
        self.toolbar.addAction(configAct)
        self.toolbar.addAction(exitAct)
        
        self.setWindowIcon(QIcon('ipt.jpg'))
        self.show()
        
    def new_wind(self):
        """Fecha a janela de boas vindas e inicia a janela principal"""
        self.close()
        self.win = Welcome()
        self.win.show()

class MyTableWidget(QWidget):        
    """Classe que cria o *layout* de guias e preenche com as classes anteriores,
    definindo tambem a funcionalidade de cada um dos botoes"""
    
    def __init__(self, robo, parent):
        """Funcao __init__ para definir o layout geral
        
        Keyword argumets:
        robo -- arquivo do qual chamam-se os comandos enviados ao robo
        """
        
        self.robo = robo
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
                
        self.tabs = QTabWidget()
        self.tab1 = Tab1()
        self.tab2 = Tab2()
        self.tab3 = Tab3()
        self.tab4 = Tab4()
        
        self.tabs.resize(350,300)  
 
        # Add tabs
        self.tabs.addTab(self.tab1,"Relativo")
        self.tabs.addTab(self.tab2,"Home")
        self.tabs.addTab(self.tab3,"Movimento")
        self.tabs.addTab(self.tab4,"Referência")
        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
        for rmoveButtons in self.tab1.relativo.rmoveButtons:
            rmoveButtons.clicked.connect(self.rmoveClicked)
        self.tab4.ref.buttonref.clicked.connect(self.refClicked)
        self.tab4.ref.buttonabsref.clicked.connect(self.absrefClicked)
        
        self.tab2.home.buttonx1.clicked.connect(self.homexClicked)
        self.tab2.home.buttonx2.clicked.connect(self.homexClicked)
        self.tab2.home.buttony1.clicked.connect(self.homeyClicked)
        self.tab2.home.buttony2.clicked.connect(self.homeyClicked)
        self.tab2.home.buttonz1.clicked.connect(self.homezClicked)
        self.tab2.home.buttonz2.clicked.connect(self.homezClicked)
        self.tab2.home.buttonall1.clicked.connect(self.homeallClicked)
        self.tab2.home.buttonall2.clicked.connect(self.homeallClicked)
        self.tab3.move.button.clicked.connect(self.moveClicked)
        
        select = [self.tab1, self.tab2, self.tab3, self.tab4]
        for tab in select:
            tab.position.buttonpos.clicked.connect(self.posClicked)
            tab.position.buttonabspos.clicked.connect(self.absposClicked)
            tab.stop.buttons.clicked.connect(self.stopClicked)
            if tab != self.tab1:
                tab.clear.buttonc.clicked.connect(self.clearClicked)
        
    def rmoveClicked(self):
        """Utiliza o metodo sender dos botoes para a movimentacao relativa de cada uma das coordenadas,
        levando os valores do respectivo passo em consideração.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        
        clickedButton = self.sender()
        digitFunction = clickedButton.text()
        
        if digitFunction[1] == '+':
            if digitFunction[0] == "X":
                self.robo.rmoveX(float(self.tab1.step.labelx.text()))
            elif digitFunction[0] == "Y":
                self.robo.rmoveY(float(self.tab1.step.labely.text()))
            elif digitFunction[0] == "Z":
                self.robo.rmoveZ(float(self.tab1.step.labelz.text()))
        else:
            if digitFunction[0] == "X":
                self.robo.rmoveX(-float(self.tab1.step.labelx.text()))
            elif digitFunction[0] == "Y":
                self.robo.rmoveY(-float(self.tab1.step.labely.text()))
            elif digitFunction[0] == "Z":
                self.robo.rmoveZ(-float(self.tab1.step.labelz.text()))
        self.posClicked(True)
        self.absposClicked(True)
        
    def moveClicked(self):
        """Envia o robo a posição indicada pelos *sliders* da classe Move.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        
        self.robo.moveX(float(self.tab3.move.posx.text()))
        self.robo.moveY(float(self.tab3.move.posy.text()))
        self.robo.moveZ(float(self.tab3.move.posz.text()))
        self.posClicked(True)
        self.absposClicked(True)
        
    def homexClicked(self):
        """Envia o robo a posição de referencia em X.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        clickedButton = self.sender()
        signalFunction = clickedButton.text()
        self.robo.homeX(signalFunction[-1])
        self.posClicked(True)
        self.absposClicked(True)
        
    def homeyClicked(self):
        """Envia o robo a posição de referencia em Y.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        
        clickedButton = self.sender()
        signalFunction = clickedButton.text()
        self.robo.homeY(signalFunction[-1])
        self.posClicked(True)
        self.absposClicked(True)
        
    def homezClicked(self):
        """Envia o robo a posicao de referencia em Z.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        
        clickedButton = self.sender()
        signalFunction = clickedButton.text()
        self.robo.homeZ(signalFunction[-1])
        self.posClicked(True)
        self.absposClicked(True)
        
    def homeallClicked(self):
        """Envia o robo a posicao de referencia em todas as coordenadas.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        
        self.homexClicked()
        self.homeyClicked()
        self.homezClicked()
        self.posClicked(True)
        self.absposClicked(True)
        
    def posClicked(self, changed = False):
        """Obtem a posicao do robo e a imprime.
        
        Chamando o comando por meio do arquivo passado por *self.robo*
        
        Keyword arguments:
        changed -- indica alteracao na posicao, para valor verdadeiro apaga a posicao da interface"""
        
        p = self.robo.position()
        if changed:
            self.text1 = ''
            self.changed = False
        else:
            self.text1 = "X = {} Y = {} Z = {}".format(format(p['x'], '.3f'),format(p['y'], '.3f'), format(p['z'], '.3f'))
        select = [self.tab1, self.tab2, self.tab3, self.tab4]
        for tab in select:
            tab.position.labelp.setText(self.text1)
        
    def absposClicked(self, changed = False):
        """Obtem a posicao absoluta do robo e a imprime.
        
        Chamando o comando por meio do arquivo passado por *self.robo*
        
        Keyword arguments:
        changed -- indica alteracao na posicao, para valor verdadeiro apaga a posicao da interface"""
        
        p = self.robo.abs_position()
        if changed:
            self.text2 = ''
            self.changed = False
        else:
            self.text2 = "X = {} Y = {} Z = {}".format(format(p['x'], '.2f'),format(p['y'], '.2f'), format(p['z'], '.2f'))
        select = [self.tab1, self.tab2, self.tab3, self.tab4]
        for tab in select:
            tab.position.labelabsp.setText(self.text2)
        
    def refClicked(self):
        """Define a posicao atual como referencia para o robo.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        
        self.posClicked(True)
        self.absposClicked(True)
        self.robo.set_reference()
        
    def absrefClicked(self):
        """Define a posicao atual como referencia absoluta para o robo.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        
        self.posClicked(True)
        self.absposClicked(True)
        self.robo.set_abs_reference()
        
    def stopClicked(self):
        """Parada emergencial da movimentacao.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        
        self.robo.stop()
        self.posClicked(True)
        self.absposClicked(True)
        
    def clearClicked(self):
        """Limpa os dados enviados.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        
        self.robo.clear()
        self.posClicked(True)
        self.absposClicked(True)
        
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCRequestHandler
    
from multiprocessing import Process
import roboxmlrpc

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

if __name__ == '__main__':  
    #robo = roboteste.Robo()
    app = QApplication(sys.argv)
    global pr
    pr = ''
    global inicial
    inicial = True
    # Create and display the splash screen
    splash_pix = QPixmap('ipt.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    # Simulate something that takes time
    time.sleep(1)
    
    win = Welcome()
    win.show()
    splash.finish(win)

    sys.exit(app.exec_())
    
    pr.terminate()
