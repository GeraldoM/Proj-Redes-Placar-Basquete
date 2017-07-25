import sys
import socket
import time
from PyQt4 import QtCore, QtGui
from PyQt4.uic import loadUiType
from PyQt4.QtGui import QSound
from threading import Thread
#from PyQt4.QtMultimedia import QAudioOutput, QAudioFormat
#from PyQt4.QtGui import QApplication

HOST = socket.gethostbyname('localhost')
PORT = 3000
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Estrutura inicial do client TCP/IP
#tcp_client_socket.connect((HOST,PORT))

Ui_MainWindow, QMainWindow = loadUiType('Cliente.ui')

 
class Main(QMainWindow, Ui_MainWindow) :
    dados = ""
    dadosAnt = ""
    nome_time_A = ""
    time_A_pts = 0
    time_A_flt_total = 0
    time_A_tt_total = 0
    jog1a = ""
    jog2a = ""
    jog3a = ""
    jog4a = ""
    jog5a = ""
    jog1a_pts = 0
    jog2a_pts = 0
    jog3a_pts = 0
    jog4a_pts = 0
    jog5a_pts = 0
    jog1a_flt = 0
    jog2a_flt = 0
    jog3a_flt = 0
    jog4a_flt = 0
    jog5a_flt = 0
    reserva1a = ""
    reserva2a = ""
    reserva3a = ""
    reserva4a = ""
    reserva5a = ""
    reserva6a = ""
    reserva7a = ""
    reserva1a_pts = 0
    reserva2a_pts = 0
    reserva3a_pts = 0
    reserva4a_pts = 0
    reserva5a_pts = 0
    reserva6a_pts = 0
    reserva7a_pts = 0
    reserva1a_flt = 0
    reserva2a_flt = 0
    reserva3a_flt = 0
    reserva4a_flt = 0
    reserva5a_flt = 0
    reserva6a_flt = 0
    reserva7a_flt = 0
    nome_time_B = 0
    time_B_pts = 0
    time_B_flt_total = 0
    time_B_tt_total = 0
    jog1b = ""
    jog2b = ""
    jog3b = ""
    jog4b = ""
    jog5b = ""
    jog1b_pts = 0
    jog2b_pts = 0
    jog3b_pts = 0
    jog4b_pts = 0
    jog5b_pts = 0
    jog1b_flt = 0
    jog2b_flt = 0
    jog3b_flt = 0
    jog4b_flt = 0
    jog5b_flt = 0
    reserva1b = ""
    reserva2b = ""
    reserva3b = ""
    reserva4b = ""
    reserva5b = ""
    reserva6b = ""
    reserva7b = ""
    reserva1b_pts = 0
    reserva2b_pts = 0
    reserva3b_pts = 0
    reserva4b_pts = 0
    reserva5b_pts = 0
    reserva6b_pts = 0
    reserva7b_pts = 0
    reserva1b_flt = 0
    reserva2b_flt = 0
    reserva3b_flt = 0
    reserva4b_flt = 0
    reserva5b_flt = 0
    reserva6b_flt = 0
    reserva7b_flt = 0
    arbitro = ""
    pontotemp = 0
    faltatemp = 0

    def __init__(self, ) :
        super(Main, self).__init__()
        self.setupUi(self)

        self.botao_avancar.clicked.connect(self.avancar)
	self.botao_timeA_1pt.clicked.connect(self.timeA_1pt)
	self.botao_timeA_2pt.clicked.connect(self.timeA_2pt)
	self.botao_timeA_3pt.clicked.connect(self.timeA_3pt)
	self.botao_timeA_falta.clicked.connect(self.timeA_falta)
	self.botao_timeB_1pt.clicked.connect(self.timeB_1pt)
	self.botao_timeB_2pt.clicked.connect(self.timeB_2pt)
	self.botao_timeB_3pt.clicked.connect(self.timeB_3pt)
	self.botao_timeB_falta.clicked.connect(self.timeB_falta)
	tcp_client_socket.connect((HOST,PORT))
	
    def atualizarDados(self):
	self.dados = (str(self.nome_time_A) + " " + str(self.time_A_pts) + " " + str(self.time_A_flt_total) + " " + str(self.jog1a) + " " + str(self.jog2a) + " " + str(self.jog3a) + " " + str(self.jog4a) + " " + str(self.jog5a) + " " + str(self.jog1a_pts) + " " + str(self.jog2a_pts) + " " + str(self.jog3a_pts) + " " + str(self.jog4a_pts) + " " + str(self.jog5a_pts) + " " + str(self.jog1a_flt) + " " + str(self.jog2a_flt) + " " + str(self.jog3a_flt) + " " + str(self.jog4a_flt) + " " + str(self.jog5a_flt) + " " + str(self.nome_time_B) + " " + str(self.time_B_pts) + " " + str(self.time_B_flt_total) + " " + str(self.jog1b) + " " + str(self.jog2b) + " " + str(self.jog3b) + " " + str(self.jog4b) + " " + str(self.jog5b) + " " + str(self.jog1b_pts) + " " + str(self.jog2b_pts) + " " + str(self.jog3b_pts) + " " + str(self.jog4b_pts) + " " + str(self.jog5b_pts) + " " + str(self.jog1b_flt) + " " + str(self.jog2b_flt) + " " + str(self.jog3b_flt) + " " + str(self.jog4b_flt) + " " + str(self.jog5b_flt))
	

    def atualizarDadosCliente(self):
	if (self.time_A_pts < 10):
		self.ponto_centro_timeA.setText("<font color='red'> " + "0" + str(self.time_A_pts) + " </font>")
	else:
		self.ponto_centro_timeA.setText("<font color='red'> " + str(self.time_A_pts) + " </font>")
	self.falta_centro_timeA.setText("<font color='gray'> " + str(self.time_A_flt_total) + " </font>")
	if (self.time_B_pts < 10):
		self.ponto_centro_timeB.setText("<font color='red'> " + "0" + str(self.time_B_pts) + " </font>")
	else:
		self.ponto_centro_timeB.setText("<font color='red'> " + "0" + str(self.time_B_pts) + " </font>")
	self.falta_centro_timeB.setText("<font color='gray'> " + str(self.time_B_flt_total) + " </font>")



	

    def ok_pt_flt_A(self):
	if (self.pt_flt_jog1.isChecked()):
		self.time_A_pts += self.pontotemp
		self.jog1a_pts += self.pontotemp
		self.time_A_flt_total += self.faltatemp
		self.jog1a_flt += self.faltatemp
		self.pt_flt_jog1.setChecked(False)
		self.pt_flt_jog1.setCheckState(False)
		self.painel_substituicao.hide()
	elif (self.pt_flt_jog2.isChecked()):
		self.time_A_pts += self.pontotemp
		self.jog2a_pts += self.pontotemp
		self.time_A_flt_total += self.faltatemp
		self.jog2a_flt += self.faltatemp
		self.pt_flt_jog2.setChecked(False)
		self.painel_substituicao.hide()
	elif (self.pt_flt_jog3.isChecked()):
		self.time_A_pts += self.pontotemp
		self.jog3a_pts += self.pontotemp
		self.time_A_flt_total += self.faltatemp
		self.jog3a_flt += self.faltatemp
		self.pt_flt_jog3.setChecked(False)
		self.painel_substituicao.hide()
	elif (self.pt_flt_jog4.isChecked()):
		self.time_A_pts += self.pontotemp
		self.jog4a_pts += self.pontotemp
		self.time_A_flt_total += self.faltatemp
		self.jog4a_flt += self.faltatemp
		self.pt_flt_jog4.setChecked(False)
		self.painel_substituicao.hide()
	elif (self.pt_flt_jog5.isChecked()):
		self.time_A_pts += self.pontotemp
		self.jog5a_pts += self.pontotemp
		self.time_A_flt_total += self.faltatemp
		self.jog5a_flt += self.faltatemp
		self.pt_flt_jog5.setChecked(False)
	self.pontotemp = 0
	self.faltatemp = 0
	self.atualizarDados()
	print(self.dados)
	byte_msg = self.dados.encode('utf-8')
	tcp_client_socket.send(byte_msg)
	self.botao_timeA_1pt.setEnabled(True)
	self.botao_timeA_2pt.setEnabled(True)
	self.botao_timeA_3pt.setEnabled(True)
	self.botao_timeA_falta.setEnabled(True)
	self.botao_timeA_substituicao.setEnabled(True)
	self.botao_timeB_1pt.setEnabled(True)
	self.botao_timeB_2pt.setEnabled(True)
	self.botao_timeB_3pt.setEnabled(True)
	self.botao_timeB_falta.setEnabled(True)
	self.botao_timeB_substituicao.setEnabled(True)
	self.botao_desfazer.setEnabled(True)
	self.atualizarDadosCliente()
	self.botao_ok_pt_flt_A.hide()
	self.botao_ok_pt_flt_B.hide()
	self.painel_pt_flt.close()

    def ok_pt_flt_B(self):
	if (self.pt_flt_jog1.isChecked()):
		self.time_B_pts += self.pontotemp
		self.jog1b_pts += self.pontotemp
		self.time_B_flt_total += self.faltatemp
		self.jog1b_flt += self.faltatemp
		self.pt_flt_jog1.setChecked(False)
	elif (self.pt_flt_jog2.isChecked()):
		self.time_B_pts += self.pontotemp
		self.jog2b_pts += self.pontotemp
		self.time_B_flt_total += self.faltatemp
		self.jog2b_flt += self.faltatemp
		self.pt_flt_jog2.setChecked(False)
	elif (self.pt_flt_jog3.isChecked()):
		self.time_B_pts += self.pontotemp
		self.jog3b_pts += self.pontotemp
		self.time_B_flt_total += self.faltatemp
		self.jog3b_flt += self.faltatemp
		self.pt_flt_jog3.setChecked(False)
	elif (self.pt_flt_jog4.isChecked()):
		self.time_B_pts += self.pontotemp
		self.jog4b_pts += self.pontotemp
		self.time_B_flt_total += self.faltatemp
		self.jog4b_flt += self.faltatemp
		self.pt_flt_jog4.setChecked(False)
	elif (self.pt_flt_jog5.isChecked()):
		self.time_B_pts += self.pontotemp
		self.jog5b_pts += self.pontotemp
		self.time_B_flt_total += self.faltatemp
		self.jog5b_flt += self.faltatemp
		self.pt_flt_jog5.setChecked(False)
	self.pontotemp = 0
	self.faltatemp = 0
	self.atualizarDados()
	self.botao_timeB_falta.setEnabled(True)
	print(self.dados)
	byte_msg = self.dados.encode('utf-8')
	tcp_client_socket.send(byte_msg)
	self.botao_timeA_1pt.setEnabled(True)
	self.botao_timeA_2pt.setEnabled(True)
	self.botao_timeA_3pt.setEnabled(True)
	self.botao_timeA_falta.setEnabled(True)
	self.botao_timeA_substituicao.setEnabled(True)
	self.botao_timeB_1pt.setEnabled(True)
	self.botao_timeB_2pt.setEnabled(True)
	self.botao_timeB_3pt.setEnabled(True)
	self.botao_timeB_falta.setEnabled(True)
	self.botao_timeB_substituicao.setEnabled(True)
	self.botao_desfazer.setEnabled(True)
	self.atualizarDadosCliente()
	self.botao_ok_pt_flt_A.hide()
	self.botao_ok_pt_flt_B.hide()
	self.painel_pt_flt.close()


    def timeA_1pt (self):
	self.botao_timeA_1pt.setEnabled(False)
	self.botao_timeA_2pt.setEnabled(False)
	self.botao_timeA_3pt.setEnabled(False)
	self.botao_timeA_falta.setEnabled(False)
	self.botao_timeA_substituicao.setEnabled(False)
	self.botao_timeB_1pt.setEnabled(False)
	self.botao_timeB_2pt.setEnabled(False)
	self.botao_timeB_3pt.setEnabled(False)
	self.botao_timeB_falta.setEnabled(False)
	self.botao_timeB_substituicao.setEnabled(False)
	self.botao_desfazer.setEnabled(False)
	self.pt_flt_jog1.setText(self.jog1a)
	self.pt_flt_jog2.setText(self.jog2a)
	self.pt_flt_jog3.setText(self.jog3a)
	self.pt_flt_jog4.setText(self.jog4a)
	self.pt_flt_jog5.setText(self.jog5a)
	self.dadosAnt = self.dados
	self.pontotemp = 1
	self.faltatemp = 0
	self.painel_pt_flt.move(320, 210)
	self.painel_pt_flt.show()
	self.botao_ok_pt_flt_A.show()
	

    def timeA_2pt (self):
	self.botao_timeA_1pt.setEnabled(False)
	self.botao_timeA_2pt.setEnabled(False)
	self.botao_timeA_3pt.setEnabled(False)
	self.botao_timeA_falta.setEnabled(False)
	self.botao_timeA_substituicao.setEnabled(False)
	self.botao_timeB_1pt.setEnabled(False)
	self.botao_timeB_2pt.setEnabled(False)
	self.botao_timeB_3pt.setEnabled(False)
	self.botao_timeB_falta.setEnabled(False)
	self.botao_timeB_substituicao.setEnabled(False)
	self.botao_desfazer.setEnabled(False)
	self.pt_flt_jog1.setText(self.jog1a)
	self.pt_flt_jog2.setText(self.jog2a)
	self.pt_flt_jog3.setText(self.jog3a)
	self.pt_flt_jog4.setText(self.jog4a)
	self.pt_flt_jog5.setText(self.jog5a)
	self.dadosAnt = self.dados
	self.pontotemp = 2
	self.faltatemp = 0
	self.painel_pt_flt.move(320, 210)
	self.painel_pt_flt.show()
	self.botao_ok_pt_flt_A.show()
    
    def timeA_3pt (self):
	self.botao_timeA_1pt.setEnabled(False)
	self.botao_timeA_2pt.setEnabled(False)
	self.botao_timeA_3pt.setEnabled(False)
	self.botao_timeA_falta.setEnabled(False)
	self.botao_timeA_substituicao.setEnabled(False)
	self.botao_timeB_1pt.setEnabled(False)
	self.botao_timeB_2pt.setEnabled(False)
	self.botao_timeB_3pt.setEnabled(False)
	self.botao_timeB_falta.setEnabled(False)
	self.botao_timeB_substituicao.setEnabled(False)
	self.botao_desfazer.setEnabled(False)
	self.pt_flt_jog1.setText(self.jog1a)
	self.pt_flt_jog2.setText(self.jog2a)
	self.pt_flt_jog3.setText(self.jog3a)
	self.pt_flt_jog4.setText(self.jog4a)
	self.pt_flt_jog5.setText(self.jog5a)
	self.dadosAnt = self.dados
	self.pontotemp = 3
	self.faltatemp = 0
	self.painel_pt_flt.move(320, 210)
	self.painel_pt_flt.show()
	self.botao_ok_pt_flt_A.show()

    def timeA_falta (self):
	self.botao_timeA_1pt.setEnabled(False)
	self.botao_timeA_2pt.setEnabled(False)
	self.botao_timeA_3pt.setEnabled(False)
	self.botao_timeA_falta.setEnabled(False)
	self.botao_timeA_substituicao.setEnabled(False)
	self.botao_timeB_1pt.setEnabled(False)
	self.botao_timeB_2pt.setEnabled(False)
	self.botao_timeB_3pt.setEnabled(False)
	self.botao_timeB_falta.setEnabled(False)
	self.botao_timeB_substituicao.setEnabled(False)
	self.botao_desfazer.setEnabled(False)
	self.pt_flt_jog1.setText(self.jog1a)
	self.pt_flt_jog2.setText(self.jog2a)
	self.pt_flt_jog3.setText(self.jog3a)
	self.pt_flt_jog4.setText(self.jog4a)
	self.pt_flt_jog5.setText(self.jog5a)
	self.dadosAnt = self.dados
	self.pontotemp = 0
	self.faltatemp = 1
	self.painel_pt_flt.move(320, 210)
	self.painel_pt_flt.show()
	self.botao_ok_pt_flt_A.show()

    def timeB_1pt (self):
	self.botao_timeA_1pt.setEnabled(False)
	self.botao_timeA_2pt.setEnabled(False)
	self.botao_timeA_3pt.setEnabled(False)
	self.botao_timeA_falta.setEnabled(False)
	self.botao_timeA_substituicao.setEnabled(False)
	self.botao_timeB_1pt.setEnabled(False)
	self.botao_timeB_2pt.setEnabled(False)
	self.botao_timeB_3pt.setEnabled(False)
	self.botao_timeB_falta.setEnabled(False)
	self.botao_timeB_substituicao.setEnabled(False)
	self.botao_desfazer.setEnabled(False)
	self.pt_flt_jog1.setText(self.jog1b)
	self.pt_flt_jog2.setText(self.jog2b)
	self.pt_flt_jog3.setText(self.jog3b)
	self.pt_flt_jog4.setText(self.jog4b)
	self.pt_flt_jog5.setText(self.jog5b)
	self.dadosAnt = self.dados
	self.pontotemp = 1
	self.faltatemp = 0
	self.painel_pt_flt.move(800, 210)
	self.painel_pt_flt.show()
	self.botao_ok_pt_flt_B.show()
    
    def timeB_2pt (self):
	self.botao_timeA_1pt.setEnabled(False)
	self.botao_timeA_2pt.setEnabled(False)
	self.botao_timeA_3pt.setEnabled(False)
	self.botao_timeA_falta.setEnabled(False)
	self.botao_timeA_substituicao.setEnabled(False)
	self.botao_timeB_1pt.setEnabled(False)
	self.botao_timeB_2pt.setEnabled(False)
	self.botao_timeB_3pt.setEnabled(False)
	self.botao_timeB_falta.setEnabled(False)
	self.botao_timeB_substituicao.setEnabled(False)
	self.botao_desfazer.setEnabled(False)
	self.pt_flt_jog1.setText(self.jog1b)
	self.pt_flt_jog2.setText(self.jog2b)
	self.pt_flt_jog3.setText(self.jog3b)
	self.pt_flt_jog4.setText(self.jog4b)
	self.pt_flt_jog5.setText(self.jog5b)
	self.dadosAnt = self.dados
	self.pontotemp = 2
	self.faltatemp = 0
	self.painel_pt_flt.move(800, 210)
	self.painel_pt_flt.show()
	self.botao_ok_pt_flt_B.show()
    
    def timeB_3pt (self):
	self.botao_timeA_1pt.setEnabled(False)
	self.botao_timeA_2pt.setEnabled(False)
	self.botao_timeA_3pt.setEnabled(False)
	self.botao_timeA_falta.setEnabled(False)
	self.botao_timeA_substituicao.setEnabled(False)
	self.botao_timeB_1pt.setEnabled(False)
	self.botao_timeB_2pt.setEnabled(False)
	self.botao_timeB_3pt.setEnabled(False)
	self.botao_timeB_falta.setEnabled(False)
	self.botao_timeB_substituicao.setEnabled(False)
	self.botao_desfazer.setEnabled(False)
	self.pt_flt_jog1.setText(self.jog1b)
	self.pt_flt_jog2.setText(self.jog2b)
	self.pt_flt_jog3.setText(self.jog3b)
	self.pt_flt_jog4.setText(self.jog4b)
	self.pt_flt_jog5.setText(self.jog5b)
	self.dadosAnt = self.dados
	self.pontotemp = 3
	self.faltatemp = 0
	self.painel_pt_flt.move(800, 210)
	self.painel_pt_flt.show()
	self.botao_ok_pt_flt_B.show()

    def timeB_falta (self):
	self.botao_timeA_1pt.setEnabled(False)
	self.botao_timeA_2pt.setEnabled(False)
	self.botao_timeA_3pt.setEnabled(False)
	self.botao_timeA_falta.setEnabled(False)
	self.botao_timeA_substituicao.setEnabled(False)
	self.botao_timeB_1pt.setEnabled(False)
	self.botao_timeB_2pt.setEnabled(False)
	self.botao_timeB_3pt.setEnabled(False)
	self.botao_timeB_falta.setEnabled(False)
	self.botao_timeB_substituicao.setEnabled(False)
	self.botao_desfazer.setEnabled(False)
	self.pt_flt_jog1.setText(self.jog1b)
	self.pt_flt_jog2.setText(self.jog2b)
	self.pt_flt_jog3.setText(self.jog3b)
	self.pt_flt_jog4.setText(self.jog4b)
	self.pt_flt_jog5.setText(self.jog5b)
	self.dadosAnt = self.dados
	self.pontotemp = 0
	self.faltatemp = 1
	self.painel_pt_flt.move(800, 210)
	self.painel_pt_flt.show()
	self.botao_ok_pt_flt_B.show()

    def avancar (self):
	

	self.nome_time_A = self.nome_time_A.text()
	self.time_A_pts = 0
	self.time_A_flt_total = 0
	self.jog1a = self.jog1_A.toPlainText()
	self.jog2a = self.jog2_A.toPlainText()
	self.jog3a = self.jog3_A.toPlainText()
	self.jog4a = self.jog4_A.toPlainText()
	self.jog5a = self.jog5_A.toPlainText()
	self.jog1a_pts = 0
	self.jog2a_pts = 0
	self.jog3a_pts = 0
	self.jog4a_pts = 0
	self.jog5a_pts = 0
	self.jog1a_flt = 0
	self.jog2a_flt = 0
	self.jog3a_flt = 0
	self.jog4a_flt = 0
	self.jog5a_flt = 0
	self.reserva1a = self.reserva1_A.toPlainText()
	self.reserva2a = self.reserva2_A.toPlainText()
	self.reserva3a = self.reserva3_A.toPlainText()
	self.reserva4a = self.reserva4_A.toPlainText()
	self.reserva5a = self.reserva5_A.toPlainText()
	self.reserva6a = self.reserva6_A.toPlainText()
	self.reserva7a = self.reserva7_A.toPlainText()
	self.reserva1a_pts = 0
	self.reserva2a_pts = 0
	self.reserva3a_pts = 0
	self.reserva4a_pts = 0
	self.reserva5a_pts = 0
	self.reserva6a_pts = 0
	self.reserva7a_pts = 0
	self.reserva1a_flt = 0
	self.reserva2a_flt = 0
	self.reserva3a_flt = 0
	self.reserva4a_flt = 0
	self.reserva5a_flt = 0
	self.reserva6a_flt = 0
	self.reserva7a_flt = 0

	self.nome_time_B = self.nome_time_B.text()
	self.time_B_pts = 0
	self.time_B_flt_total = 0
	self.jog1b = self.jog1_B.toPlainText()
	self.jog2b = self.jog2_B.toPlainText()
	self.jog3b = self.jog3_B.toPlainText()
	self.jog4b = self.jog4_B.toPlainText()
	self.jog5b = self.jog5_B.toPlainText()
	self.jog1b_pts = 0
	self.jog2b_pts = 0
	self.jog3b_pts = 0
	self.jog4b_pts = 0
	self.jog5b_pts = 0
	self.jog1b_flt = 0
	self.jog2b_flt = 0
	self.jog3b_flt = 0
	self.jog4b_flt = 0
	self.jog5b_flt = 0
	self.reserva1b = self.reserva1_B.toPlainText()
	self.reserva2b = self.reserva2_B.toPlainText()
	self.reserva3b = self.reserva3_B.toPlainText()
	self.reserva4b = self.reserva4_B.toPlainText()
	self.reserva5b = self.reserva5_B.toPlainText()
	self.reserva6b = self.reserva6_B.toPlainText()
	self.reserva7b = self.reserva7_B.toPlainText()
	self.reserva1b_flt = 0
	self.reserva2b_flt = 0
	self.reserva3b_flt = 0
	self.reserva4b_flt = 0
	self.reserva5b_flt = 0
	self.reserva6b_flt = 0
	self.reserva7b_flt = 0
	self.arbitro = self.nome_arbitro.text()
	self.nome_timeA.setText("<font color='white'> " + self.nome_time_A + " </font>")
	self.nome_timeB.setText("<font color='white'> " + self.nome_time_B + " </font>")
	self.nome_arbitro_controle.setText("<font color='white'> " + self.arbitro + " </font>")

	self.atualizarDados()	
	#tcp_client_socket.connect((HOST,PORT))
	message = self.dados
	byte_msg = message.encode('utf-8')
	tcp_client_socket.send(byte_msg)
	#tcp_client_socket.close()
        self.Cadastro.hide()
	self.painel_substituicao.hide()
	self.painel_pt_flt.hide()
	self.botao_ok_pt_flt_A.hide()
	self.botao_ok_pt_flt_B.hide()
	self.botao_ok_substituicao_A.hide()
	self.botao_ok_substituicao_B.hide()
	self.botao_timeA_1pt.setEnabled(False)
	self.botao_timeA_2pt.setEnabled(False)
	self.botao_timeA_3pt.setEnabled(False)
	self.botao_timeA_falta.setEnabled(False)
	self.botao_timeB_1pt.setEnabled(False)
	self.botao_timeB_2pt.setEnabled(False)
	self.botao_timeB_3pt.setEnabled(False)
	self.botao_timeB_falta.setEnabled(False)
	self.botao_pausar.setEnabled(False)
	self.botao_desfazer.setEnabled(False)
	self.botao_iniciar.setEnabled(True)
	self.Controle.show()
	
        


if __name__ == '__main__' :
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
