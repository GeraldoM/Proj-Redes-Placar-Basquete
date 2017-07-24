import sys
import socket
import time
from PyQt4 import QtCore, QtGui
from PyQt4.uic import loadUiType
from threading import Thread


Ui_MainWindow, QMainWindow = loadUiType('Servidor HD.ui')

#Variaveis de apoio
HOST = socket.gethostbyname('localhost')
PORT = 3000

#Instanciando transporte TCP/IP
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Associacao de porta ao processo servidor
tcp_server_socket.bind((HOST,PORT))
tcp_server_socket.listen(999)

print("Servidor online!")
parado = True
parado_posse = True
zerar_posse = False

class Cronometro_posse(Thread):
	ct_sec = 24
	acabou = False
	def __init__ (self, crono):
                      Thread.__init__(self)
		      self.crono = crono
		
        def run(self):
		global parado_posse
		global zerar_posse
		while True:
			if(self.ct_sec < 10):
				self.crono.cronometro_posse.setText("<font color='red'> " "0" + str(self.ct_sec) + " </font>")
			else:
				self.crono.cronometro_posse.setText("<font color='red'> " + str(self.ct_sec) + " </font>")
			if(zerar_posse == True):
				self.ct_sec = 24
				zerar_posse = False
				self.crono.cronometro_posse.setText("<font color='red'> " + str(self.ct_sec) + " </font>")
			if (parado_posse == False):
				time.sleep(1)
				self.ct_sec-=1
				
				if (self.ct_sec<0):
					zerar_posse = True
					parado_posse = True
class Cronometro(Thread):
	ct_sec = 0
	ct_min = 10
	acabou = False
	periodo = 1
	def __init__ (self, crono):
                      Thread.__init__(self)
		      self.crono = crono
		      self.crono.cronometro_minutos.move(20, 0)
		
        def run(self):
		global parado
		global parado_posse
		while True:
			if (not self.acabou):
				if (parado == False):
					time.sleep(1)
					self.ct_sec-=1
					if (self.ct_sec<0):
					    self.ct_sec=59
					    self.ct_min -= 1
					if (self.ct_sec <10):
						self.crono.cronometro_segundos.setText("<font color='red'> " "0" + str(self.ct_sec) + " </font>")
					else:
						self.crono.cronometro_segundos.setText("<font color='red'> " + str(self.ct_sec) + " </font>")
					self.crono.cronometro_minutos.setText("<font color='red'> " "0" + str(self.ct_min) + " </font>")
					print(str(self.ct_min) + ":" + str(self.ct_sec))
					print parado
					if (self.ct_min <= 0 and self.ct_sec <= 0):
						parado = True
						parado_posse = True
						zerar_posse = True
						self.periodo += 1
						if(self.periodo < 5):
							self.ct_min = 10
							self.ct_sec = 0
							self.crono.cronometro_segundos.setText("<font color='red'> " "0" + str(self.ct_sec) + " </font>")
							self.crono.cronometro_minutos.setText("<font color='red'> " + str(self.ct_min) + " </font>")
							self.crono.periodo.setText("<font color='red'> " + str(self.periodo) + " </font>")
						elif(self.periodo == 5):
							if(self.crono.timeA_total_pts.text() == self.crono.timeB_total_pts.text()):
								self.ct_min = 5
								self.ct_sec = 0
								self.crono.cronometro_segundos.setText("<font color='red'> " "0" + str(self.ct_sec) + " </font>")
								self.crono.cronometro_minutos.setText("<font color='red'> " + str(self.ct_min) + " </font>")
								self.crono.periodo.setText("<font color='red'> " + str(self.periodo) + " </font>")
							else:
								self.acabou = True
								client.close()
								tcp_server_socket.close()
			

		#client.close()
		#tcp_server_socket.close()
		


class Th(Thread):
		

                def __init__ (self, info):
                      Thread.__init__(self)
		      self.info = info
		      #print (teste.time_A_jog1.text())
		      #teste.timeA_nome_centro.setText("AFF")
		
		

                def run(self):
		   #while True:
		   global parado
		   global parado_posse
		   global zerar_posse
		   client, addr = tcp_server_socket.accept()
                   while True:
			#client, addr = tcp_server_socket.accept()
			data = client.recv(2048)
			data = data.decode('utf-8')
			dados = data.split()
			print("Comando recebido: " + data)
			self.info.timeA_nome_centro.setText("<font color='white'> " + dados[0] + " </font>")
			self.info.time_A_nome_painel_direito.setText(dados[0])
			if(int(dados[1]) < 10):
				self.info.timeA_pts_centro.setText("<font color='red'> " "0" + dados[1] + " </font>")
			else:
				self.info.timeA_pts_centro.setText("<font color='red'> " + dados[1] + " </font>")
			self.info.timeA_flt_centro.setText("<font color='gray'> " + dados[2] + " </font>")
			self.info.timeA_total_pts.setText(dados[1])
			self.info.timeA_total_flt.setText(dados[2])
			self.info.time_A_jog1.setText(dados[3])
			self.info.time_A_jog2.setText(dados[4])
			self.info.time_A_jog3.setText(dados[5])
			self.info.time_A_jog4.setText(dados[6])
			self.info.time_A_jog5.setText(dados[7])
			self.info.timeA_jog1_pts.setText(dados[8])
			self.info.timeA_jog2_pts.setText(dados[9])
			self.info.timeA_jog3_pts.setText(dados[10])
			self.info.timeA_jog4_pts.setText(dados[11])
			self.info.timeA_jog5_pts.setText(dados[12])
			self.info.timeA_jog1_flt.setText(dados[13])
			self.info.timeA_jog2_flt.setText(dados[14])
			self.info.timeA_jog3_flt.setText(dados[15])
			self.info.timeA_jog4_flt.setText(dados[16])
			self.info.timeA_jog5_flt.setText(dados[17])
			self.info.timeB_nome_centro.setText("<font color='white'> " + dados[18] + " </font>")
			self.info.time_B_nome_painel_direito.setText(dados[18])
			if (int(dados[19]) < 10):
				self.info.timeB_pts_centro.setText("<font color='red'> " "0" + dados[19] + " </font>")
			else:
				self.info.timeB_pts_centro.setText("<font color='red'> " + dados[19] + " </font>")
			self.info.timeB_flt_centro.setText("<font color='gray'> " + dados[20] + " </font>")
			self.info.timeB_total_pts.setText(dados[19])
			self.info.timeB_total_flt.setText(dados[20])
			self.info.time_B_jog1.setText(dados[21])
			self.info.time_B_jog2.setText(dados[22])
			self.info.time_B_jog3.setText(dados[23])
			self.info.time_B_jog4.setText(dados[24])
			self.info.time_B_jog5.setText(dados[25])
			self.info.timeB_jog1_pts.setText(dados[26])
			self.info.timeB_jog2_pts.setText(dados[27])
			self.info.timeB_jog3_pts.setText(dados[28])
			self.info.timeB_jog4_pts.setText(dados[29])
			self.info.timeB_jog5_pts.setText(dados[30])
			self.info.timeB_jog1_flt.setText(dados[31])
			self.info.timeB_jog2_flt.setText(dados[32])
			self.info.timeB_jog3_flt.setText(dados[33])
			self.info.timeB_jog4_flt.setText(dados[34])
			self.info.timeB_jog5_flt.setText(dados[35])
				
 			#print("\nMensagem de teste")
		   #client.close()
		   #tcp_server_socket.close()


class Main(QMainWindow, Ui_MainWindow) :
    def __init__(self, ) :
        super(Main, self).__init__()
        self.setupUi(self)
	self.timeA_pts_centro.setText("<font color='red'> " + "00" + " </font>")
	self.timeB_pts_centro.setText("<font color='red'> " + "00" + " </font>")
	self.timeA_flt_centro.setText("<font color='gray'> " + "0" + " </font>")
	self.timeB_flt_centro.setText("<font color='gray'> " + "0" + " </font>")
	self.cronometro_minutos.setText("<font color='red'> " + "10" + " </font>")
	self.cronometro_minutos.move(40, 0)
	self.cronometro_segundos.setText("<font color='red'> " "00" + " </font>")
	cronometro = Cronometro(self)
	cronometro.start()
	cronometro_posse = Cronometro_posse(self)
	cronometro_posse.start()
	recebeDados = Th(self)
	recebeDados.start()
	

	


if __name__ == '__main__' :
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    #main.showFullScreen()
    #main.showMaximized()
    sys.exit(app.exec_())


