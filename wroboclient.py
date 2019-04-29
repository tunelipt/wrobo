# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 11:30:00 2019

@author: pjabardo
"""

import sys

from PyQt5.QtWidgets import (QSplashScreen, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import argparse
import time
import wrobo


if __name__ == '__main__':  
    
    parser = argparse.ArgumentParser(description="wrobo")
    parser.add_argument("-i", "--ip", help="Endereço IP do servidor XML-RPC", default="localhost")
    parser.add_argument("-p", "--port", help="Porta XML-RPC do servidor XML-RPC", default=9595, type=int)

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
    
    win = wrobo.WRoboServer(False, args.ip, args.port, False, True)
    win.show()
    splash.finish(win)

    sys.exit(app.exec_())
