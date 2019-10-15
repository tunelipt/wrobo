# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:51:03 2017

@author: felipenanini
"""

import sys
from PyQt5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
import time


   
from multiprocessing import Process, freeze_support
import argparse
import os.path

from wrobolib import robostart


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
    
    win = robostart.WRoboServer(args.test, args.ip, args.port, not args.serverless, args.client)
    # Create and display the splash screen
    splash_pix = QPixmap(os.path.join("wrobolib", 'ipt.jpg'))
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    # Simulate something that takes time
    for i in range(15):
        time.sleep(0.1)
        app.processEvents()

    
    win.show()
    splash.finish(win)

    sys.exit(app.exec_())
