# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QLabel, QWidget, QVBoxLayout, QHBoxLayout, QSplashScreen, QGridLayout, QComboBox,
                             QGroupBox, QPushButton, QApplication, QSlider, QMainWindow, qApp, QLineEdit, QAction)
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QPixmap, QIcon, QRegExpValidator, QIntValidator, QPainter, QColor, QFont, QPen
import time


def ip4addr(addlocalhost=True):
    import netifaces

    xinterf = netifaces.interfaces()
    
    addr = []

    for x in xinterf:
        net = netifaces.ifaddresses(x)
        if 2 in net:
            ip = net[2][0]['addr']
            addr.append(ip)
    if addlocalhost:
        if "localhost" not in addr and "127.0.0.1" not in addr:
            addr.append("localhost")
    
    return addr

        
    

class IPConfig(QWidget):
    """
    Janela para configurar um servidor XML-RPC server

    Basically sets an IP and a port number
    """
    
    def __init__(self, title, server=False, ip="localhost", port=9500, lock=[], parent=None):
        super(IPConfig, self).__init__(parent=parent)
        ip = ip.strip().lower()
        self.server = server
        #if server:
        import netifaces
        addr = [x if x != "127.0.0.1" else "localhost" for x in ip4addr()]

        
        self.iptext = QComboBox(self)
        for a in addr:
            self.iptext.addItem(a)

        if "localhost" not in addr:
            self.iptext.addItem("localhost")
            addr.append("localhost")
        
        if ip in addr:
            self.iptext.setCurrentIndex(addr.index(ip))
        else:
            if not server:
                addr.append(ip)
                self.iptext.addItem(ip)
                self.iptext.setCurrentIndex(addr.index(ip))
                

        if not server:
            self.iptext.setEditable(True)
        
        iplab = QLabel("IP:")

        
        self.porttext = QLineEdit(self)
        self.porttext.setValidator(QIntValidator(1000, 65535, self.porttext))
        self.porttext.setText(str(port))
        portlab = QLabel("Port: ")

        r1 = QHBoxLayout()
        r2 = QHBoxLayout()

        r1.addWidget(iplab)
        r1.addWidget(self.iptext)

        r2.addWidget(portlab)
        r2.addWidget(self.porttext)

        ver = QVBoxLayout()
        ver.addLayout(r1)
        ver.addLayout(r2)
                
        col0 = QVBoxLayout()
        group = QGroupBox(title)
        group.setLayout(ver)
        col0.addWidget(group)

        if "ip" in lock:
            self.iptext.setEnabled(False)
        if "port" in lock:
            self.porttext.setEnabled(False)
        
        self.setLayout(col0)
        
    def ipaddr(self):
        return self.iptext.currentText()
    def port(self):
        return self.porttext.text()




if __name__ == '__main__':
    
    #robo = roboteste.mesa()
    import argparse
    app = QApplication(sys.argv)

    parser = argparse.ArgumentParser(description="ipportconfig")
    parser.add_argument("-i", "--ip", help="IP Address of the TCP/IP server", default="localhost")
    parser.add_argument("-p", "--port", help="Port of the TCP/IP server", default=9596, type=int)
    parser.add_argument("-s", "--server", help="Configure server (instead of client)", action="store_true")
    parser.add_argument("-t", "--title", help="Type of server", default="XML-RPC")
    parser.add_argument("lock", nargs="*")
    
    args = parser.parse_args()


    win = IPConfig(args.title, args.server, args.ip, args.port, args.lock)
    win.show()
    r = app.exec_()

    print(win.ipaddr())
    print(win.port())
    sys.exit(r)

