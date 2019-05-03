#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 07:07:43 2017

@author: ipt

Codigo utilizando PyQt5 para a movimentacao do robo no tunel de vento

Contem uma classe Robotk para testar o funcionamento da GUI
"""

import sys
from PyQt5.QtWidgets import (QLabel, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, qApp, QMenu,
                             QGroupBox, QPushButton, QApplication, QSlider, QMainWindow, QSplashScreen, QAction)
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QPixmap, QIcon, QRegExpValidator, QDoubleValidator
import time
        
class RoboWindow(QMainWindow):
    """Classe implementada a partir da classe QWidget, gera a tela inicial dispondo
    os grupos criados em um *grid layout*"""
    
    def __init__(self, robo, msg, process, parent=None):
        """Define os grupos dentro do *grid layout*"""

        self.process = process
        self.robo = robo

        super(RoboWindow, self).__init__(parent)
        
        #Layout Geral
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        
        grid = QGridLayout()
        
        grid.addWidget(self.createRelativeGroup(), 0, 0)
        grid.addWidget(self.createStepGroup(), 1, 0)
        grid.addWidget(self.createReferenceGroup(), 2, 0)
        grid.addWidget(self.createHomeGroup(), 0, 1)
        grid.addWidget(self.createMoveGroup(), 1, 1)
        grid.addWidget(self.createPositionGroup(), 2, 1)
        grid.addWidget(self.createStopGroup(), 0, 2, 2, 1)
        grid.addWidget(self.createClearGroup(), 2, 2)
        
        menubar = self.menuBar()
        configMenu = menubar.addMenu('Configurações')
        
        exitAct = QAction(QIcon('exit.png'), 'Sair', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Sair do Programa')
        exitAct.triggered.connect(self.sair)
        
        configAct = QAction(QIcon('configura.jpg'), 'Configurar', self)
        configAct.setStatusTip('Configurar endereço')
        configAct.triggered.connect(self.new_wind)
        
        configMenu.addAction(configAct)
        configMenu.addAction(exitAct)
        self.setWindowIcon(QIcon('ipt.jpg'))
        
        self.widget.setLayout(grid)
        
        self.setWindowTitle("Movimentador do Tunel - {}".format(msg))
        self.resize(640, 480)
        
    
    def new_wind(self):
        """Fecha a janela de boas vindas e inicia a janela principal"""
        self.close()
        self.win = Welcome()
        self.win.show()
        
    def createRelativeGroup(self):    
        """Gera os botoes para o movimento relativo e define como serao 
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
            button.clicked.connect(self.rmoveClicked)
    
            grid.addWidget(button, *position)

        relgroup.setLayout(grid)
        
        return relgroup
    
    
            
    def createStepGroup(self):
        """Gera os botoes para o passo do movimento relativo e define como serao 
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
        self.sliderx.setMaximum(1000)

        self.labelx = QLabel('10')
        self.labelx.setMinimumHeight(40)
        self.labelx.setAlignment(Qt.AlignCenter)
        stepx = QLabel("X")
        
        self.entrada_x = QLineEdit(self)
        self.entrada_x.setText('10')
        regex = QRegExp("\d{0,3}(\.\d{0,3})?")
        validator=QRegExpValidator(regex, self.entrada_x)
        
        self.entrada_x.setValidator(validator)
        
        vbox.addWidget(self.labelx)
        vbox.addLayout(hbox1)
        hbox1.addWidget(stepx,0.5)
        hbox1.addWidget(self.sliderx,6)
        hbox1.addWidget(self.entrada_x,1)
        
        self.entrada_x.textChanged[str].connect(lambda text: self.changeCursor(text, self.sliderx))
        self.sliderx.valueChanged[int].connect(lambda value: self.changeValue(value, self.labelx, self.entrada_x))
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
        self.entrada_y.setText('10')
        validator=QRegExpValidator(regex, self.entrada_y)
        
        vbox.addWidget(self.labely)
        vbox.addLayout(hbox2)
        hbox2.addWidget(stepy,0.5)
        hbox2.addWidget(self.slidery,6)
        hbox2.addWidget(self.entrada_y,1)
        
        self.entrada_y.textChanged[str].connect(lambda text: self.changeCursor(text, self.slidery))
        self.slidery.valueChanged[int].connect(lambda value: self.changeValue(value, self.labely, self.entrada_y))
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
        self.entrada_z.setText('10')
        validator=QRegExpValidator(regex, self.entrada_z)
        
        vbox.addWidget(self.labelz)
        vbox.addLayout(hbox3)
        hbox3.addWidget(stepz,0.5)
        hbox3.addWidget(self.sliderz,6)
        hbox3.addWidget(self.entrada_z,1)
        
        self.entrada_z.textChanged[str].connect(lambda text: self.changeCursor(text, self.sliderz))
        self.sliderz.valueChanged[int].connect(lambda value: self.changeValue(value, self.labelz, self.entrada_z))
        self.sliderz.setMinimumHeight(40)

        stepgroup.setLayout(vbox)
        return stepgroup
        
    def createReferenceGroup(self):
        """Gera os botoes para a definicao da referencia do robo e define como serao 
        dispostos de acordo com *Box Layouts* dentro do *group box* criado.
        """
        
        refgroup = QGroupBox('Referencia')

        
        vbox = QVBoxLayout()
        hbox_x = QHBoxLayout()
        hbox_y = QHBoxLayout()
        hbox_z = QHBoxLayout()

        labx = QLabel("Xref")
        laby = QLabel("Yref")
        labz = QLabel("Zref")

        self.refxtext = QLineEdit(self)
        self.refxtext.setText("0")
        validatorx = QDoubleValidator()
        self.refxtext.setValidator(validatorx)
        hbox_x.addWidget(labx)
        hbox_x.addWidget(self.refxtext)

        self.refytext = QLineEdit(self)
        self.refytext.setText("0")
        validatory = QDoubleValidator()
        self.refytext.setValidator(validatory)
        hbox_y.addWidget(laby)
        hbox_y.addWidget(self.refytext)

        self.refztext = QLineEdit(self)
        self.refztext.setText("0")
        validatorz = QDoubleValidator()
        self.refztext.setValidator(validatorz)
        hbox_z.addWidget(labz)
        hbox_z.addWidget(self.refztext)
        
        
        self.buttonref = QPushButton("Ponto atual como referencia")
        self.buttonref.clicked.connect(self.refClicked)
        self.buttonabsref = QPushButton("Referencia absoluta")
        self.buttonabsref.clicked.connect(self.absrefClicked)

        vbox.addLayout(hbox_x)
        vbox.addLayout(hbox_y)
        vbox.addLayout(hbox_z)
        
        vbox.addWidget(self.buttonref)
        vbox.addWidget(self.buttonabsref)
        refgroup.setLayout(vbox)
        
        return refgroup
    
    def createHomeGroup(self):
        """Gera os botoes para enviar o robo para a posição de referencia e define como serao 
        dispostos de acordo com *Box Layouts* dentro do *group box* criado.
        """
        
        homegroup = QGroupBox('Home')
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        
        self.buttonx1 = QPushButton("Home X-")
        self.buttonx1.clicked.connect(self.homeClicked)
        self.buttonx2 = QPushButton("Home X+")
        self.buttonx2.clicked.connect(self.homeClicked)
        self.buttony1 = QPushButton("Home Y-")
        self.buttony1.clicked.connect(self.homeClicked)
        self.buttony2 = QPushButton("Home Y+")
        self.buttony2.clicked.connect(self.homeClicked)
        self.buttonz1 = QPushButton("Home Z-")
        self.buttonz1.clicked.connect(self.homeClicked)
        self.buttonz2 = QPushButton("Home Z+")
        self.buttonz2.clicked.connect(self.homeClicked)
        self.buttonall1 = QPushButton("Home TODOS-")
        self.buttonall1.clicked.connect(self.homeallClicked)
        self.buttonall1.setMinimumHeight(50)
        self.buttonall2 = QPushButton("Home TODOS+")
        self.buttonall2.clicked.connect(self.homeallClicked)
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
    
    def createMoveGroup(self):
        """Gera os botoes para enviar o robo para uma posição específica e define como serao 
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
        
        self.button.clicked.connect(self.moveClicked)
        #Definicao do sliderx
        self.slidermx = QSlider(Qt.Horizontal, self)
        self.slidermx.setFocusPolicy(Qt.StrongFocus)
        self.slidermx.setSingleStep(10)
        self.slidermx.setValue(0)
        self.slidermx.setMinimum(-5000)
        self.slidermx.setMaximum(5000)
        
        self.move_x = QLineEdit(self)
        self.move_x.setText('0')
        regex = QRegExp("-?\d{0,4}(\.\d{0,4})?")
        validator=QRegExpValidator(regex, self.move_x)
        
        self.move_x.setValidator(validator)
        
        self.posx = QLabel('0')
        self.posx.setAlignment(Qt.AlignCenter)
        self.labelxbutton = QPushButton("X")
        self.labelxbutton.clicked.connect(self.moveXClicked)
        
        #labelx.setMinimumHeight(40)

        vbox.addWidget(self.posx)
        vbox.addLayout(hbox1)
        hbox1.addWidget(self.labelxbutton,0.5)
        hbox1.addWidget(self.slidermx,7)
        hbox1.addWidget(self.move_x,1)
        
        self.move_x.textChanged[str].connect(lambda text: self.changeCursor(text, self.slidermx))
        self.slidermx.valueChanged[int].connect(lambda value: self.changeValue(value, self.posx, self.move_x))
        self.slidermx.setMinimumHeight(40)
        
        #Definicao do slidery
        self.slidermy = QSlider(Qt.Horizontal, self)
        self.slidermy.setFocusPolicy(Qt.StrongFocus)
        self.slidermy.setSingleStep(10)
        self.slidermy.setValue(0)
        self.slidermy.setMinimum(-2600)
        self.slidermy.setMaximum(2600)
        
        self.move_y = QLineEdit(self)
        self.move_y.setText('0')
        validator=QRegExpValidator(regex, self.move_y)
        
        self.move_y.setValidator(validator)
        
        self.posy = QLabel('0')
        self.posy.setAlignment(Qt.AlignCenter)
        self.labelybutton = QPushButton("Y")
        self.labelybutton.clicked.connect(self.moveYClicked)
        #labely.setMinimumHeight(40)

        vbox.addWidget(self.posy)
        vbox.addLayout(hbox2)
        hbox2.addWidget(self.labelybutton,0.5)
        hbox2.addWidget(self.slidermy,7)
        hbox2.addWidget(self.move_y,1)
        
        self.move_y.textChanged[str].connect(lambda text: self.changeCursor(text, self.slidermy))
        self.slidermy.valueChanged[int].connect(lambda value: self.changeValue(value, self.posy, self.move_y))
        self.slidermy.setMinimumHeight(40)

        
        #Definicao do sliderz
        self.slidermz = QSlider(Qt.Horizontal, self)
        self.slidermz.setFocusPolicy(Qt.StrongFocus)
        self.slidermz.setSingleStep(10)
        self.slidermz.setValue(0)
        self.slidermz.setMinimum(-600)
        self.slidermz.setMaximum(600)

        self.move_z = QLineEdit(self)
        self.move_z.setText('0')
        validator=QRegExpValidator(regex, self.move_z)
        
        self.move_z.setValidator(validator)
        
        self.posz = QLabel('0')
        self.posz.setAlignment(Qt.AlignCenter)
        self.labelzbutton = QPushButton("Z")
        self.labelzbutton.clicked.connect(self.moveZClicked)
        #labelz.setMinimumHeight(40)
        
        vbox.addWidget(self.posz)
        vbox.addLayout(hbox3)
        hbox3.addWidget(self.labelzbutton,0.5)
        hbox3.addWidget(self.slidermz,7)
        hbox3.addWidget(self.move_z,1)
        
        self.move_z.textChanged[str].connect(lambda text: self.changeCursor(text, self.slidermz))
        self.slidermz.valueChanged[int].connect(lambda value: self.changeValue(value, self.posz, self.move_z))
        self.slidermz.setMinimumHeight(40)
        
        movegroup.setLayout(vbox)
        
        return movegroup
    
       
    def createPositionGroup(self):
        """Gera os botoes para verificar a posição do robo e define como serao 
        dispostos de acordo com *Box Layouts* dentro do *group box* criado.
        """
        
        posgroup = QGroupBox('Posicao')
        
        vbox = QVBoxLayout()
        
        self.buttonpos = QPushButton("Posicao")
        self.buttonpos.setMinimumHeight(35)
        self.buttonpos.clicked.connect(self.posClicked)
        self.labelp = QLabel('')
        self.labelp.setAlignment(Qt.AlignCenter)
        
        self.buttonabspos = QPushButton("Posicao absoluta")
        self.buttonabspos.setMinimumHeight(35)
        self.buttonabspos.clicked.connect(self.absposClicked)
        self.labelabsp = QLabel('')
        self.labelabsp.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.buttonpos)
        vbox.addWidget(self.labelp)
        vbox.addWidget(self.buttonabspos)
        vbox.addWidget(self.labelabsp)
        posgroup.setLayout(vbox)

        return posgroup
    
    def createStopGroup(self):
        """Gera o botao para parada de emergencia e define as caracteristicas
        do botao, colocando-o dentro do *group box*.
        """
        
        stopgroup = QGroupBox("Parada")
        
        vbox = QVBoxLayout()
        
        button = QPushButton("PARADA IMEDIATA")
        button.setMinimumWidth(150)
        button.setMinimumHeight(400)
        button.setStyleSheet("background-color: red; border-style: outset; border-width: 2px; border-radius: 10px; border-color: black;")
        button.clicked.connect(self.stopClicked)
        
        vbox.addWidget(button)
        stopgroup.setLayout(vbox)
    
        return stopgroup
    
    def createClearGroup(self):
        """Gera o botao para limpar os dados e define as caracteristicas
        do botao, colocando-o dentro do *group box*.
        """
        
        cleargroup = QGroupBox("Limpar")
        
        vbox = QVBoxLayout()
        
        button = QPushButton("Limpar")
        button.clicked.connect(self.clearClicked)
        vbox.addWidget(button)
        cleargroup.setLayout(vbox)

        return cleargroup
    
    
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
    
    def changeValue(self, value, *labels):
        """changeValue toma os valores dos *sliders* a cada alteracao feita e repassa para o texto
        das *labels* respectivas.
        
        Keyword arguments:
        value -- o valor referente ao *slider* alterado
        lables -- o *label* a ser modificado
        """
        for label in labels:
            if label is not None:
                label.setText(str(value))
            
    
    def rmoveClicked(self):
        """Utiliza o metodo sender dos botoes para a movimentacao relativa de cada uma das coordenadas,
        levando os valores do respectivo passo em consideração.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        
        clickedButton = self.sender()
        digitFunction = clickedButton.text()
        x, y, z = '', '', ''
        if digitFunction[1] == '+':
            if digitFunction[0] == "X":
                x=float(self.sliderx.value())
            elif digitFunction[0] == "Y":
                y=float(self.slidery.value())
            elif digitFunction[0] == "Z":
                z=float(self.sliderz.value())
        else:
            if digitFunction[0] == "X":
                x=-float(self.sliderx.value())
            elif digitFunction[0] == "Y":
                y=-float(self.slidery.value())
            elif digitFunction[0] == "Z":
                z=-float(self.sliderz.value())
        self.robo.rmove(x, y, z)
        self.posClicked(True)
        self.absposClicked(True)
        
    def moveClicked(self):
        """Envia o robo a posição indicada pelos *sliders* da classe Move.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        
        self.robo.move(float(self.slidermx.value()), float(self.slidermy.value()), float(self.slidermz.value()))
        self.posClicked(True)
        self.absposClicked(True)

    def moveXClicked(self):
        x = float(self.slidermx.value())
        self.robo.move(x)
        self.posClicked(True)
        self.absposClicked(True)
        return None

    def moveYClicked(self):
        y = float(self.slidermy.value())
        self.robo.move('', y)
        self.posClicked(True)
        self.absposClicked(True)
        return None

    def moveZClicked(self):
        z = float(self.slidermz.value())
        self.robo.move('', '', z)
        self.posClicked(True)
        self.absposClicked(True)
        return None
        
    def homeClicked(self, sinal = None, eixo = None):
        """Envia o robo a posição de referencia em X.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        if not sinal and not eixo:    
            clickedButton = self.sender()
            signalFunction = clickedButton.text()[-1]
            axisFunction = clickedButton.text()[-2]
        else:
            signalFunction = sinal
            axisFunction = eixo
        self.robo.home(signalFunction, axisFunction)
        self.clearpos()
        #self.posClicked(True)
        #self.absposClicked(True)
        
    def homeallClicked(self):
        """Envia o robo a posicao de referencia em todas as coordenadas.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""
        clickedButton = self.sender()
        sinal = clickedButton.text()[-1]
        self.homeClicked(sinal, 'X')
        self.homeClicked(sinal, 'Y')
        self.homeClicked(sinal, 'Z')
        self.clearpos()
        #self.posClicked(True)
        #self.absposClicked(True)

    def clearpos(self):
        self.labelp.setText('')
        self.labelabsp.setText('')
        return None
    
    def posClicked(self, changed = False):
        """Obtem a posicao do robo e a imprime.
        
        Chamando o comando por meio do arquivo passado por *self.robo*
        
        Keyword arguments:
        changed -- indica alteracao na posicao, para valor verdadeiro apaga a posicao da interface"""
        
        p = self.robo.position()
        if changed:
            self.text1 = ''
            self.changed = False
            self.labelp.setText(self.text1)
        else:
            self.text1 = "X = {} Y = {} Z = {}".format(format(p['x'], '.1f'),format(p['y'], '.1f'), format(p['z'], '.1f'))
            self.labelp.setText(self.text1)
        
    def absposClicked(self, changed = False):
        """Obtem a posicao absoluta do robo e a imprime.
        
        Chamando o comando por meio do arquivo passado por *self.robo*
        
        Keyword arguments:
        changed -- indica alteracao na posicao, para valor verdadeiro apaga a posicao da interface"""
        
        p = self.robo.abs_position()
        if changed:
            self.text2 = ''
            self.changed = False
            self.labelabsp.setText('')
        else:
            self.text2 = "X = {} Y = {} Z = {}".format(format(p['x'], '.1f'),format(p['y'], '.1f'), format(p['z'], '.1f'))
            self.labelabsp.setText(self.text2)
        
    def refClicked(self):
        """Define a posicao atual como referencia para o robo.
        
        Chamando o comando por meio do arquivo passado por *self.robo*"""

        xref = float(self.refxtext.text())
        yref = float(self.refytext.text())
        zref = float(self.refztext.text())
        
        self.posClicked(True)
        self.absposClicked(True)

        self.robo.set_reference(xref, yref, zref)

        self.refxtext.setText("0")
        self.refytext.setText("0")
        self.refztext.setText("0")
        
        
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
        
    def sair(self):
        if self.process is not None:
            self.process.terminate()
        qApp.quit()
        
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
    
    # Create and display the splash screen
    splash_pix = QPixmap('ipt.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    # Simulate something that takes time
    time.sleep(2)

    win = Welcome()
    win.show()
    splash.finish(win)
    sys.exit(app.exec_())
    
    pr.terminate()
