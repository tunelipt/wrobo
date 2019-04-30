# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:51:03 2017

@author: felipenanini
"""

import sys
from PyQt5.QtWidgets import (QLabel, QWidget, QVBoxLayout, QHBoxLayout, QSplashScreen, QGridLayout, QComboBox,
                             QGroupBox, QPushButton, QApplication, QSlider, QMainWindow, qApp,
                             QLineEdit, QAction, QCheckBox, QMessageBox)
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QPixmap, QIcon, QRegExpValidator, QPainter, QColor, QFont, QPen
import time

import ipportconfig

import pyqtrobo

import xmlrpc.client
   
from multiprocessing import Process, freeze_support
import roboxmlrpc
import argparse

class WRoboServer(QMainWindow):
    """Classe implementada a partir da classe QMainWindow e gera a tela inicial,
    responsavel pela configuracao inicial dos argumentos utilizados pelo XMLRPC"""
    
    def __init__(self, test=False,  srvip="localhost", srvport=9595, initserver=True, client=False, parent=None):
        """Funcao __init__ para definir o layout geral
        
        Keyword argumets:
        robo -- arquivo do qual chamam-se os comandos enviados ao robo
        """
        
        super(WRoboServer, self).__init__(parent=parent)
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.initvals = dict(test=test, ip=srvip, port=srvport, initserver=initserver, client=client)
        self.test = test
        self.client = client

        if client:
            self.initserver = False
        else:
            self.initserver = initserver
        
        self.draw_gui()
        #quit = QAction("Quit", self)
        #quit.triggered.connect(self.sair)
        
        self.process = None
        self.robo = None
        
        self.setWindowIcon(QIcon('ipt-wrobo.ico'))
        self.show()
    
    def draw_gui(self):
        self.setWindowTitle("Interface do robô do túnel")
        #self.setGeometry(50, 50, 350, 400)
        vbox = QVBoxLayout()
        brow = QHBoxLayout()
        
        if not self.client:
            self.rpc = ipportconfig.IPConfig(server=True, title="XML-RPC", ip=self.initvals['ip'],
                                             port=self.initvals['port'], parent=self)
            self.check_rpc = QCheckBox("Usar XML-RPC")
            self.check_rpc.stateChanged.connect(self.rpc_check_changed)
            if self.initserver:
                self.check_rpc.setChecked(True)
            else:
                self.check_rpc.setChecked(False)
            
            vbox.addWidget(self.check_rpc)
            vbox.addWidget(self.rpc)
            
            self.config_button = QPushButton("Config")
            self.sair_button = QPushButton("Sair")
            vbox.addLayout(brow)
            brow.addWidget(self.config_button)
            brow.addWidget(self.sair_button)
            self.config_button.clicked.connect(self.init_server)
            self.sair_button.clicked.connect(self.sair)

            self.widget.setLayout(vbox)
        else: # cliente
            self.check_rpc = None
            self.rpc = ipportconfig.IPConfig("XML-RPC Server", False, self.initvals['ip'],
                                             self.initvals['port'], parent=self)
            vbox.addWidget(self.rpc)
            
            self.config_button = QPushButton("Config")
            self.sair_button = QPushButton("Sair")
            vbox.addLayout(brow)
            brow.addWidget(self.config_button)
            brow.addWidget(self.sair_button)
            self.config_button.clicked.connect(self.init_client)
            self.sair_button.clicked.connect(self.sair)

            self.widget.setLayout(vbox)
                
        return
    
    def rpc_check_changed(self):
        if self.check_rpc.isChecked():
            self.rpc.setEnabled(True)
        else:
            self.rpc.setEnabled(False)
            
    def init_client(self):
        xaddr = self.rpc.ipaddr().strip()
        xport = self.rpc.port()
        time.sleep(1)
        serv = "http://{}:{}".format(xaddr, xport)
        self.robo = xmlrpc.client.ServerProxy(serv)
        err = False
        msg = "http://{}:{}".format(xaddr, xport)
        for ntries in range(10):
            time.sleep(2)
            try:
                if self.robo.ping() == 123:
                    self.close()
                    self.win = pyqtrobo.RoboWindow(self.robo, msg, self.process)
                    self.win.show()
                    return
                else:
                    print("Não conseguiu conectar com o robo. Tentando novamente ...")
                    err = True
            except:
                print("Não conseguiu conectar com o robo. Tentando novamente ...")
                err = True
        
        if err:
            QMessageBox.critical(self, 'Erro', "Não foi possível encontrar o servidor XML-RPC. Tente outro IP ou porta", QMessageBox.Ok)
          
        
                
        
    def init_server(self):
        pr = None
        m = None
        self.process = None
        self.initserver = self.check_rpc.isChecked()
        msg = ''
        
        if self.initserver:
            xaddr = self.rpc.ipaddr().strip()
            xport = self.rpc.port()

            msg = "http://{}:{}".format(xaddr, xport)
            pr = Process(target=roboxmlrpc.start_server, args=(self.test, xaddr, xport))
            pr.start()
            serv = "http://{}:{}".format(xaddr, xport)
            time.sleep(8)
            self.process = pr
            return self.init_client()
            
        else:
            if self.test:
                import roboteste as robo
                msg = "TESTE"
            else:
                import robo
                msg = ""
            
            m = robo.Robo()
            success = True
            for ntries in range(20):
                time.sleep(1)
                try:
                    if m.ping() == 123:
                        success = True
                        break
                except:
                    print("Não conseguiu conectar. Tentando novamente ...")
                    success = False
            if not success:
                QMessage.critical(self, 'Erro', "Não foi possível iniciar o robô",  MessageBox.Ok)
                m = None
            
        self.process = pr
        self.robo = m
        if m is not None:
            self.close()
            self.win = pyqtrobo.RoboWindow(self.robo, msg, self.process)
            self.win.show()
            return
        else:
            QMessage.critical(self, 'Erro', "Não foi possível criar uma interface com a Mesa",
                              QMessageBox.Ok)
            
    def sair(self):
        """Finaliza o processo de comunicação e encerra o aplicativo"""
        qApp.quit()


if __name__ == '__main__':  
    freeze_support()
    
    parser = argparse.ArgumentParser(description="wmesa")
    parser.add_argument("-t", "--test", help="Interface teste do robô cartesiano do túnel de vento",
                        action="store_true")
    parser.add_argument("-i", "--ip", help="Endereço IP do servidor XML-RPC", default="localhost")
    parser.add_argument("-p", "--port", help="Porta XML-RPC do servidor XML-RPC", default=9595, type=int)
    parser.add_argument("-n", "--serverless", help="Não inicie o servidor XML-RPC", action="store_true")
    parser.add_argument("-c", "--client", help="Criar interface para cliente de servidor XML-RPC", action="store_true")
    
    app = QApplication([]) # sys.argv

    args = parser.parse_args()
    
    # Create and display the splash screen
    splash_pix = QPixmap('ipt.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    # Simulate something that takes time
    time.sleep(1)
    
    win = WRoboServer(args.test, args.ip, args.port, not args.serverless, args.client)
    win.show()
    splash.finish(win)

    sys.exit(app.exec_())
