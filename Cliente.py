#coding=utf-8
import sys
import socket
import time
from PyQt4 import QtCore, QtGui
from PyQt4.uic import loadUiType
from PyQt4.QtGui import QSound
from threading import Thread

Ui_MainWindow, QMainWindow = loadUiType('Cliente.ui')

#Estrutura inicial do client TCP/IP
HOST = socket.gethostbyname('localhost')
PORT = 3000
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


parado = True
parado_posse = True
zerar_posse = False

""" Cria a classe referente ao cronometro da posse de bola. Nela, é implementado uma Thread com um loop
que roda durante todo o programa, modificando valores e setando os valores do cronometro da posse de bola
na tela de controle do cliente. """
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
					self.crono.botao_continuar_posse.setText("Iniciar")
					self.crono.botao_zerar_posse.setEnabled(False)
			

""" Cria a classe referente ao cronometro do tempo de partida. Nela, é implementado uma Thread com um loop
que roda durante todo o programa, modificando valores e setando os valores do cronometro do tempo da partida na
tela de controle do cliente. """
class Cronometro(Thread):
	ct_sec = 0
	ct_min = 10
	acabou = False
	periodo = 1
	def __init__ (self, crono):
                      Thread.__init__(self)
		      self.crono = crono
		
        def run(self):
		global parado
		while True:
			if (not self.acabou):
				if (parado == False):
					time.sleep(1)
					self.ct_sec-=1
					if (self.ct_sec<0):
					    self.ct_sec=59
					    self.ct_min -= 1
					if(self.ct_sec <10):
						self.crono.cronometro_segundos.setText("<font color='red'> " "0" + str(self.ct_sec) + " </font>")
					else:
						self.crono.cronometro_segundos.setText("<font color='red'> " + str(self.ct_sec) + " </font>")
					self.crono.cronometro_minutos.setText("<font color='red'> " "0" + str(self.ct_min) + " </font>")
					#print(str(self.ct_min) + ":" + str(self.ct_sec))
			
					if (self.ct_min <= 0 and self.ct_sec <= 0):
						parado = True
						parado_posse = True
						zerar_posse = True
						self.periodo+=1
						self.crono.botao_timeA_1pt.setEnabled(False)
						self.crono.botao_timeA_2pt.setEnabled(False)
						self.crono.botao_timeA_3pt.setEnabled(False)
						self.crono.botao_timeA_falta.setEnabled(False)
						self.crono.botao_timeB_1pt.setEnabled(False)
						self.crono.botao_timeB_2pt.setEnabled(False)
						self.crono.botao_timeB_3pt.setEnabled(False)
						self.crono.botao_timeB_falta.setEnabled(False)
						self.crono.botao_pausar.setEnabled(False)
						self.crono.botao_desfazer.setEnabled(False)
						self.crono.botao_iniciar.setEnabled(True)
						self.crono.botao_continuar_posse.setEnabled(False)
						self.crono.botao_zerar_posse.setEnabled(False)
						self.crono.botao_continuar_posse.setText("Continuar")
						if(self.periodo < 5):
							self.ct_min = 10
							self.ct_sec = 0
							self.crono.cronometro_segundos.setText("<font color='red'> " "0" + str(self.ct_sec) + " </font>")
							self.crono.cronometro_minutos.setText("<font color='red'> " + str(self.ct_min) + " </font>")
						elif(self.periodo == 5):
							self.ct_min = 15
							self.ct_sec = 0
							self.crono.cronometro_segundos.setText("<font color='red'> " "0" + str(self.ct_sec) + " </font>")
							self.crono.cronometro_minutos.setText("<font color='red'> " + str(self.ct_min) + " </font>")
						else:
							self.acabou = True
							tcp_client_socket.close()
							break
						self.crono.periodo.setText("<font color='red'> " + str(self.periodo) + " </font>")
						

		

""" Classe main, define todas as variáveis referente aos dados dos times, jogadores e da partida. """
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
    pontoTemp = 0
    faltatemp = 0
    pausado = False
    periodo = 1

    """ A função __init__ é uma função inicial que instancia um objeto da classe Cronometro e Cronometro_posse e os inicia, 
    define a conexão entre os elementos da interface gráfica e as funções associadas a eles e gerencia as telas de exibição, 
    inicialmente exibindo a tela de conexão com o servidor. """
    def __init__(self, ) :
        super(Main, self).__init__()
        self.setupUi(self)
	cronometro = Cronometro(self)
   	cronometro.start()
	cronometro_posse = Cronometro_posse(self)
   	cronometro_posse.start()
	self.Cadastro.hide()
	self.Controle.hide()
	self.botao_conectar.clicked.connect(self.conectar)
        self.botao_avancar.clicked.connect(self.avancar)
        self.botao_iniciar.clicked.connect(self.iniciar)
	self.botao_pausar.clicked.connect(self.pausar_continuar)
	self.botao_desfazer.clicked.connect(self.desfazer)
	self.botao_timeA_1pt.clicked.connect(self.timeA_1pt)
	self.botao_timeA_2pt.clicked.connect(self.timeA_2pt)
	self.botao_timeA_3pt.clicked.connect(self.timeA_3pt)
	self.botao_timeA_falta.clicked.connect(self.timeA_falta)
	self.botao_timeA_substituicao.clicked.connect(self.substituicao_A)
	self.botao_timeB_substituicao.clicked.connect(self.substituicao_B)
	self.botao_timeB_1pt.clicked.connect(self.timeB_1pt)
	self.botao_timeB_2pt.clicked.connect(self.timeB_2pt)
	self.botao_timeB_3pt.clicked.connect(self.timeB_3pt)
	self.botao_timeB_falta.clicked.connect(self.timeB_falta)
	self.botao_ok_substituicao_A.clicked.connect(self.ok_substituicao_A)
	self.botao_ok_substituicao_B.clicked.connect(self.ok_substituicao_B)
	self.botao_timeA_tt.clicked.connect(self.timeA_tt)
	self.botao_timeB_tt.clicked.connect(self.timeB_tt)
	self.botao_cancelar_substituicao.clicked.connect(self.cancelar_substituicao)
	self.botao_ok_pt_flt_A.clicked.connect(self.ok_pt_flt_A)
	self.botao_ok_pt_flt_B.clicked.connect(self.ok_pt_flt_B)
	self.botao_continuar_posse.clicked.connect(self.pausar_continuar_posse)
	self.botao_zerar_posse.clicked.connect(self.zerar_cronometro_posse)
	
    """ A função 'conectar' é referente ao botão 'Conectar' da tela de conexão com o servidor (tela inicial). Ao clicar,
    é armazenado os dados do campo preenchido com o IP e feito a conexão TCP utilizando o IP passado pelo campo. Após
    a conexão bem sucedida, é feito gerenciamento de tela ocultando a tela de conexão e exibindo a tela de cadastro."""
    def conectar(self):
	global HOST
	global PORT
	ip_servidor = str(self.ip_servidor.text())
	HOST = socket.gethostbyname(ip_servidor)
	tcp_client_socket.connect((HOST,PORT))
	self.A_Inicial.hide()
	self.Cadastro.show()

    """ A função 'atualizarDados' tem como objetivo pegar todos os valores de dados atualizados referente aos time, 
    jogadores e partida e colocá-los na variável 'dados', que armazena em String todos os dados em um padrão que
    é interpretado pelo servidor. """
    def atualizarDados(self):
	self.dados = (str(self.nome_time_A) + " " + str(self.time_A_pts) + " " + str(self.time_A_flt_total) + " " + str(self.jog1a) + " " + str(self.jog2a) + " " + str(self.jog3a) + " " + str(self.jog4a) + " " + str(self.jog5a) + " " + str(self.jog1a_pts) + " " + str(self.jog2a_pts) + " " + str(self.jog3a_pts) + " " + str(self.jog4a_pts) + " " + str(self.jog5a_pts) + " " + str(self.jog1a_flt) + " " + str(self.jog2a_flt) + " " + str(self.jog3a_flt) + " " + str(self.jog4a_flt) + " " + str(self.jog5a_flt) + " " + str(self.nome_time_B) + " " + str(self.time_B_pts) + " " + str(self.time_B_flt_total) + " " + str(self.jog1b) + " " + str(self.jog2b) + " " + str(self.jog3b) + " " + str(self.jog4b) + " " + str(self.jog5b) + " " + str(self.jog1b_pts) + " " + str(self.jog2b_pts) + " " + str(self.jog3b_pts) + " " + str(self.jog4b_pts) + " " + str(self.jog5b_pts) + " " + str(self.jog1b_flt) + " " + str(self.jog2b_flt) + " " + str(self.jog3b_flt) + " " + str(self.jog4b_flt) + " " + str(self.jog5b_flt))
	
    """ A função 'atualizarDadosCliente' tem como objetivo atualizar todos os dados que possuem exibição na tela do 
    cliente (tela de controle), tais como: total de pontos e total de faltas. """
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

    """ A função 'iniciar' é acionada ao clicar no botão 'Iniciar' na tela do cliente (tela de controle). Ela
    tem como objetivo iniciar os cronometros, alterando as variáveis que modificam seu comportamento (parado ou rodando),
    ativar/desativar os botões de funcionamento da partida e enviar o comando para o servidor também iniciar. """
    def iniciar (self):
	global parado
	global parado_posse
	message = "#iniciar" 
	byte_msg = message.encode('utf-8')
	tcp_client_socket.send(byte_msg)
	parado = False
	parado_posse = False
	self.botao_timeA_1pt.setEnabled(True)
	self.botao_timeA_2pt.setEnabled(True)
	self.botao_timeA_3pt.setEnabled(True)
	self.botao_timeA_falta.setEnabled(True)
	self.botao_timeB_1pt.setEnabled(True)
	self.botao_timeB_2pt.setEnabled(True)
	self.botao_timeB_3pt.setEnabled(True)
	self.botao_timeB_falta.setEnabled(True)
	self.botao_pausar.setEnabled(True)
	self.botao_desfazer.setEnabled(False)
	self.botao_continuar_posse.setEnabled(True)
	self.botao_zerar_posse.setEnabled(True)
	self.botao_continuar_posse.setText("Pausar")
	if (self.time_A_tt_total < 2):
		self.botao_timeA_tt.setEnabled(True)
	if (self.time_B_tt_total < 2):
		self.botao_timeB_tt.setEnabled(True)
	self.botao_iniciar.setEnabled(False)

    """ A função 'timeA_tt' é acionada ao clicar no botão do tempo técnico do time A. Ela conta a quantidade de tempo
    técnico utilizado pelo time A e realiza seu funcionamento, enviando para o servidor o comando que informa que
    um tempo técnico foi utilizado. """
    def timeA_tt(self):
	self.time_A_tt_total += 1
	print(self.time_A_tt_total)
	if (self.time_A_tt_total == 1):
		message = "#tt_A1"
		byte_msg = message.encode('utf-8')
		tcp_client_socket.send(byte_msg)
	elif(self.time_A_tt_total == 2):
		message = "#tt_A2"
		byte_msg = message.encode('utf-8')
		tcp_client_socket.send(byte_msg)
		self.botao_timeA_tt.setEnabled(False)

    """ A função 'timeB_tt' é acionada ao clicar no botão do tempo técnico do time B. Ela conta a quantidade de tempo
    técnico utilizado pelo time B e realiza seu funcionamento, enviando para o servidor o comando que informa que
    um tempo técnico foi utilizado. """
    def timeB_tt(self):
	self.time_B_tt_total += 1
	if (self.time_B_tt_total == 1):
		message = "#tt_B1"
		byte_msg = message.encode('utf-8')
		tcp_client_socket.send(byte_msg)
	elif(self.time_B_tt_total == 2):
		message = "#tt_B2"
		byte_msg = message.encode('utf-8')
		tcp_client_socket.send(byte_msg)
		self.botao_timeB_tt.setEnabled(False)

    """ A função 'pausar_continuar' é acionada ao clicar no botão "Pausar/Continuar" na tela de controle e realiza a 
    parada e a retomada da partida, alterando as variáveis de controle dos cronometros, alguns botões e enviando o 
    comando para o servidor parar ou continuar a partida, dependendo do caso. """
    def pausar_continuar (self):
	global parado
	global parado_posse
	if(self.pausado == False):
		self.pausado = True
		parado = True
		parado_posse = True
		self.botao_continuar_posse.setEnabled(False)
		self.botao_pausar.setText("Continuar")
		message = "#pausar"
		byte_msg = message.encode('utf-8')
		tcp_client_socket.send(byte_msg)
	else:
		self.pausado = False
		parado = False
		parado_posse = False
		self.botao_pausar.setText("Pausar")
		self.botao_continuar_posse.setText("Pausar")
		self.botao_continuar_posse.setEnabled(True)
		message = "#continuar"
		byte_msg = message.encode('utf-8')
		tcp_client_socket.send(byte_msg)

    """ A função 'pausar_continuar_posse' é acionada ao clicar no botão 'Pausar' da posse de bola, na tela de controle e
    realiza a parada ou retomada do cronometro da posse de bola, dependendo da situação, altera o texto no botão de acordo
    com a estado do cronometro e envia o comando para o servidor. """
    def pausar_continuar_posse (self):
	global parado_posse
	if(parado_posse == False):
		parado_posse = True
		self.botao_continuar_posse.setText("Continuar")
		message = "#pausar_posse"
		byte_msg = message.encode('utf-8')
		tcp_client_socket.send(byte_msg)
	else:
		parado_posse = False
		self.botao_continuar_posse.setText("Pausar")
		self.botao_zerar_posse.setEnabled(True)
		message = "#continuar_posse"
		byte_msg = message.encode('utf-8')
		tcp_client_socket.send(byte_msg)

    """ A função 'zerar_cronometro_posse' é acionada ao clicar no botão 'Zerar' na tela de controle e como o próprio nome já sugere, 
    realiza o 'reset' no contador do cronometro da posse de bola e envia uma mensagem para o servidor com o comando. """
    def zerar_cronometro_posse (self):
	global zerar_posse
	zerar_posse = True
	message = "#zerar_posse"
	byte_msg = message.encode('utf-8')
	tcp_client_socket.send(byte_msg)

    """ A função 'substituicao_A' é acionada ao clicar no botão 'Substituição' no painel do time A e exibe uma tela ao lado do painel do 
    time A com todos os jogadores titulares e reservas do respectivo time com um checkbox em cada um, permitindo o usuário marcar somente
    UM titular e somente UM reserva para realizar a substituição. """
    def substituicao_A(self):
	self.botao_ok_substituicao_A.show()
	self.painel_substituicao.move(70, 210)
	self.sub_jog1.setText(self.jog1a)
	self.sub_jog2.setText(self.jog2a)
	self.sub_jog3.setText(self.jog3a)
	self.sub_jog4.setText(self.jog4a)
	self.sub_jog5.setText(self.jog5a)
	self.sub_res1.setText(self.reserva1a)
	self.sub_res2.setText(self.reserva2a)
	self.sub_res3.setText(self.reserva3a)
	self.sub_res4.setText(self.reserva4a)
	self.sub_res5.setText(self.reserva5a)
	self.sub_res6.setText(self.reserva6a)
	self.sub_res7.setText(self.reserva7a)
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
	self.painel_substituicao.show()
		
    """ A função 'substituicao_B' é acionada ao clicar no botão 'Substituição' no painel do time B e exibe uma tela ao lado do painel do 
    time B com todos os jogadores titulares e reservas do respectivo time com um checkbox em cada um, permitindo o usuário marcar somente
    UM titular e somente UM reserva para realizar a substituição. """
    def substituicao_B(self):
	self.botao_ok_substituicao_B.show()
	self.painel_substituicao.move(900, 210)
	self.sub_jog1.setText(self.jog1b)
	self.sub_jog2.setText(self.jog2b)
	self.sub_jog3.setText(self.jog3b)
	self.sub_jog4.setText(self.jog4b)
	self.sub_jog5.setText(self.jog5b)
	self.sub_res1.setText(self.reserva1b)
	self.sub_res2.setText(self.reserva2b)
	self.sub_res3.setText(self.reserva3b)
	self.sub_res4.setText(self.reserva4b)
	self.sub_res5.setText(self.reserva5b)
	self.sub_res6.setText(self.reserva6b)
	self.sub_res7.setText(self.reserva7b)
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
	self.painel_substituicao.show()

    """ A função 'cancelar_substituicao' é acionada ao clicar no botão 'Cancelar' no painel de substituição. Como
    o próprio nome sugere, realiza o cancelamento da substituição, fechando o painel de substituição. """
    def cancelar_substituicao(self):
	self.botao_ok_substituicao_A.hide()
	self.botao_ok_substituicao_B.hide()
	self.painel_substituicao.hide()
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

    """ A função 'ok_substituicao_A' é acionada ao clicar no botão 'Ok' no painel de substituição do time A. Ou seja,
    é a função responsável por realizar de fato a substituição após o usuário confirmar a mesma. A função testa caso
    por caso qual checkbox estar marcado nos jogadores TITULARES e nos RESERVAS e realiza a substituição, transferindo
    valores de ponto e faltas individuais de cada jogador pra suas novas variáveis. Após isso, chama a função 'atualizarDados'
    e envia os dados atualizados para o servidor atualizar, fechando o painel de substituição em seguida. """
    def ok_substituicao_A(self):
	self.botao_ok_substituicao_A.hide()
	self.botao_ok_substituicao_B.hide()
	self.painel_substituicao.hide()
	if (self.sub_jog1.isChecked()):
		novoreserva_nome = self.jog1a
		novoreserva_pts = self.jog1a_pts
		novoreserva_flt = self.jog1a_flt
		self.sub_jog1.setChecked(False)
		if (self.sub_res1.isChecked()):
			self.jog1a = self.reserva1a
			self.jog1a_pts = self.reserva1a_pts
			self.jog1a_flt = self.reserva1a_flt
			self.reserva1a = novoreserva_nome
			self.reserva1a_pts = novoreserva_pts
			self.reserva1a_flt = novoreserva_flt
		elif (self.sub_res2.isChecked()):
			self.jog1a = self.reserva2a
			self.jog1a_pts = self.reserva2a_pts
			self.jog1a_flt = self.reserva2a_flt
			self.reserva2a = novoreserva_nome
			self.reserva2a_pts = novoreserva_pts
			self.reserva2a_flt = novoreserva_flt
		elif (self.sub_res3.isChecked()):
			self.jog1a = self.reserva3a
			self.jog1a_pts = self.reserva3a_pts
			self.jog1a_flt = self.reserva3a_flt
			self.reserva3a = novoreserva_nome
			self.reserva3a_pts = novoreserva_pts
			self.reserva3a_flt = novoreserva_flt
		elif (self.sub_res4.isChecked()):
			self.jog1a = self.reserva4a
			self.jog1a_pts = self.reserva4a_pts
			self.jog1a_flt = self.reserva4a_flt
			self.reserva4a = novoreserva_nome
			self.reserva4a_pts = novoreserva_pts
			self.reserva4a_flt = novoreserva_flt
		elif (self.sub_res5.isChecked()):
			self.jog1a = self.reserva5a
			self.jog1a_pts = self.reserva5a_pts
			self.jog1a_flt = self.reserva5a_flt
			self.reserva5a = novoreserva_nome
			self.reserva5a_pts = novoreserva_pts
			self.reserva5a_flt = novoreserva_flt
		elif (self.sub_res6.isChecked()):
			self.jog1a = self.reserva6a
			self.jog1a_pts = self.reserva6a_pts
			self.jog1a_flt = self.reserva6a_flt
			self.reserva6a = novoreserva_nome
			self.reserva6a_pts = novoreserva_pts
			self.reserva6a_flt = novoreserva_flt
		else:
			self.jog1a = self.reserva7a
			self.jog1a_pts = self.reserva7a_pts
			self.jog1a_flt = self.reserva7a_flt
			self.reserva7a = novoreserva_nome
			self.reserva7a_pts = novoreserva_pts
			self.reserva7a_flt = novoreserva_flt
	elif (self.sub_jog2.isChecked()):
		novoreserva_nome = self.jog2a
		novoreserva_pts = self.jog2a_pts
		novoreserva_flt = self.jog2a_flt
		self.pt_flt_jog2.setChecked(False)
		if (self.sub_res1.isChecked()):
			self.jog2a = self.reserva1a
			self.jog2a_pts = self.reserva1a_pts
			self.jog2a_flt = self.reserva1a_flt
			self.reserva1a = novoreserva_nome
			self.reserva1a_pts = novoreserva_pts
			self.reserva1a_flt = novoreserva_flt
		elif (self.sub_res2.isChecked()):
			self.jog2a = self.reserva2a
			self.jog2a_pts = self.reserva2a_pts
			self.jog2a_flt = self.reserva2a_flt
			self.reserva2a = novoreserva_nome
			self.reserva2a_pts = novoreserva_pts
			self.reserva2a_flt = novoreserva_flt
		elif (self.sub_res3.isChecked()):
			self.jog2a = self.reserva3a
			self.jog2a_pts = self.reserva3a_pts
			self.jog2a_flt = self.reserva3a_flt
			self.reserva3a = novoreserva_nome
			self.reserva3a_pts = novoreserva_pts
			self.reserva3a_flt = novoreserva_flt
		elif (self.sub_res4.isChecked()):
			self.jog2a = self.reserva4a
			self.jog2a_pts = self.reserva4a_pts
			self.jog2a_flt = self.reserva4a_flt
			self.reserva4a = novoreserva_nome
			self.reserva4a_pts = novoreserva_pts
			self.reserva4a_flt = novoreserva_flt
		elif (self.sub_res5.isChecked()):
			self.jog2a = self.reserva5a
			self.jog2a_pts = self.reserva5a_pts
			self.jog2a_flt = self.reserva5a_flt
			self.reserva5a = novoreserva_nome
			self.reserva5a_pts = novoreserva_pts
			self.reserva5a_flt = novoreserva_flt
		elif (self.sub_res6.isChecked()):
			self.jog2a = self.reserva6a
			self.jog2a_pts = self.reserva6a_pts
			self.jog2a_flt = self.reserva6a_flt
			self.reserva6a = novoreserva_nome
			self.reserva6a_pts = novoreserva_pts
			self.reserva6a_flt = novoreserva_flt
		else:
			self.jog2a = self.reserva7a
			self.jog2a_pts = self.reserva7a_pts
			self.jog2a_flt = self.reserva7a_flt
			self.reserva7a = novoreserva_nome
			self.reserva7a_pts = novoreserva_pts
			self.reserva7a_flt = novoreserva_flt
	elif (self.sub_jog3.isChecked()):
		novoreserva_nome = self.jog3a
		novoreserva_pts = self.jog3a_pts
		novoreserva_flt = self.jog3a_flt
		self.pt_flt_jog3.setChecked(False)
		if (self.sub_res1.isChecked()):
			self.jog3a = self.reserva1a
			self.jog3a_pts = self.reserva1a_pts
			self.jog3a_flt = self.reserva1a_flt
			self.reserva1a = novoreserva_nome
			self.reserva1a_pts = novoreserva_pts
			self.reserva1a_flt = novoreserva_flt
		elif (self.sub_res2.isChecked()):
			self.jog3a = self.reserva2a
			self.jog3a_pts = self.reserva2a_pts
			self.jog3a_flt = self.reserva2a_flt
			self.reserva2a = novoreserva_nome
			self.reserva2a_pts = novoreserva_pts
			self.reserva2a_flt = novoreserva_flt
		elif (self.sub_res3.isChecked()):
			self.jog3a = self.reserva3a
			self.jog3a_pts = self.reserva3a_pts
			self.jog3a_flt = self.reserva3a_flt
			self.reserva3a = novoreserva_nome
			self.reserva3a_pts = novoreserva_pts
			self.reserva3a_flt = novoreserva_flt
		elif (self.sub_res4.isChecked()):
			self.jog3a = self.reserva4a
			self.jog3a_pts = self.reserva4a_pts
			self.jog3a_flt = self.reserva4a_flt
			self.reserva4a = novoreserva_nome
			self.reserva4a_pts = novoreserva_pts
			self.reserva4a_flt = novoreserva_flt
		elif (self.sub_res5.isChecked()):
			self.jog3a = self.reserva5a
			self.jog3a_pts = self.reserva5a_pts
			self.jog3a_flt = self.reserva5a_flt
			self.reserva5a = novoreserva_nome
			self.reserva5a_pts = novoreserva_pts
			self.reserva5a_flt = novoreserva_flt
		elif (self.sub_res6.isChecked()):
			self.jog3a = self.reserva6a
			self.jog3a_pts = self.reserva6a_pts
			self.jog3a_flt = self.reserva6a_flt
			self.reserva6a = novoreserva_nome
			self.reserva6a_pts = novoreserva_pts
			self.reserva6a_flt = novoreserva_flt
		else:
			self.jog3a = self.reserva7a
			self.jog3a_pts = self.reserva7a_pts
			self.jog3a_flt = self.reserva7a_flt
			self.reserva7a = novoreserva_nome
			self.reserva7a_pts = novoreserva_pts
			self.reserva7a_flt = novoreserva_flt
	elif (self.sub_jog4.isChecked()):
		novoreserva_nome = self.jog4a
		novoreserva_pts = self.jog4a_pts
		novoreserva_flt = self.jog4a_flt
		self.pt_flt_jog4.setChecked(False)
		if (self.sub_res1.isChecked()):
			self.jog4a = self.reserva1a
			self.jog4a_pts = self.reserva1a_pts
			self.jog4a_flt = self.reserva1a_flt
			self.reserva1a = novoreserva_nome
			self.reserva1a_pts = novoreserva_pts
			self.reserva1a_flt = novoreserva_flt
		elif (self.sub_res2.isChecked()):
			self.jog4a = self.reserva2a
			self.jog4a_pts = self.reserva2a_pts
			self.jog4a_flt = self.reserva2a_flt
			self.reserva2a = novoreserva_nome
			self.reserva2a_pts = novoreserva_pts
			self.reserva2a_flt = novoreserva_flt
		elif (self.sub_res3.isChecked()):
			self.jog4a = self.reserva3a
			self.jog4a_pts = self.reserva3a_pts
			self.jog4a_flt = self.reserva3a_flt
			self.reserva3a = novoreserva_nome
			self.reserva3a_pts = novoreserva_pts
			self.reserva3a_flt = novoreserva_flt
		elif (self.sub_res4.isChecked()):
			self.jog4a = self.reserva4a
			self.jog4a_pts = self.reserva4a_pts
			self.jog4a_flt = self.reserva4a_flt
			self.reserva4a = novoreserva_nome
			self.reserva4a_pts = novoreserva_pts
			self.reserva4a_flt = novoreserva_flt
		elif (self.sub_res5.isChecked()):
			self.jog4a = self.reserva5a
			self.jog4a_pts = self.reserva5a_pts
			self.jog4a_flt = self.reserva5a_flt
			self.reserva5a = novoreserva_nome
			self.reserva5a_pts = novoreserva_pts
			self.reserva5a_flt = novoreserva_flt
		elif (self.sub_res6.isChecked()):
			self.jog4a = self.reserva6a
			self.jog4a_pts = self.reserva6a_pts
			self.jog4a_flt = self.reserva6a_flt
			self.reserva6a = novoreserva_nome
			self.reserva6a_pts = novoreserva_pts
			self.reserva6a_flt = novoreserva_flt
		else:
			self.jog4a = self.reserva7a
			self.jog4a_pts = self.reserva7a_pts
			self.jog4a_flt = self.reserva7a_flt
			self.reserva7a = novoreserva_nome
			self.reserva7a_pts = novoreserva_pts
			self.reserva7a_flt = novoreserva_flt
	else:
		novoreserva_nome = self.jog5a
		novoreserva_pts = self.jog5a_pts
		novoreserva_flt = self.jog5a_flt
		self.pt_flt_jog5.setChecked(False)
		if (self.sub_res1.isChecked()):
			self.jog5a = self.reserva1a
			self.jog5a_pts = self.reserva1a_pts
			self.jog5a_flt = self.reserva1a_flt
			self.reserva1a = novoreserva_nome
			self.reserva1a_pts = novoreserva_pts
			self.reserva1a_flt = novoreserva_flt
		elif (self.sub_res2.isChecked()):
			self.jog5a = self.reserva2a
			self.jog5a_pts = self.reserva2a_pts
			self.jog5a_flt = self.reserva2a_flt
			self.reserva2a = novoreserva_nome
			self.reserva2a_pts = novoreserva_pts
			self.reserva2a_flt = novoreserva_flt
		elif (self.sub_res3.isChecked()):
			self.jog5a = self.reserva3a
			self.jog5a_pts = self.reserva3a_pts
			self.jog5a_flt = self.reserva3a_flt
			self.reserva3a = novoreserva_nome
			self.reserva3a_pts = novoreserva_pts
			self.reserva3a_flt = novoreserva_flt
		elif (self.sub_res4.isChecked()):
			self.jog5a = self.reserva4a
			self.jog5a_pts = self.reserva4a_pts
			self.jog5a_flt = self.reserva4a_flt
			self.reserva4a = novoreserva_nome
			self.reserva4a_pts = novoreserva_pts
			self.reserva4a_flt = novoreserva_flt
		elif (self.sub_res5.isChecked()):
			self.jog5a = self.reserva5a
			self.jog5a_pts = self.reserva5a_pts
			self.jog5a_flt = self.reserva5a_flt
			self.reserva5a = novoreserva_nome
			self.reserva5a_pts = novoreserva_pts
			self.reserva5a_flt = novoreserva_flt
		elif (self.sub_res6.isChecked()):
			self.jog5a = self.reserva6a
			self.jog5a_pts = self.reserva6a_pts
			self.jog5a_flt = self.reserva6a_flt
			self.reserva6a = novoreserva_nome
			self.reserva6a_pts = novoreserva_pts
			self.reserva6a_flt = novoreserva_flt
		else:
			self.jog5a = self.reserva7a
			self.jog5a_pts = self.reserva7a_pts
			self.jog5a_flt = self.reserva7a_flt
			self.reserva7a = novoreserva_nome
			self.reserva7a_pts = novoreserva_pts
			self.reserva7a_flt = novoreserva_flt
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
	self.botao_desfazer.setEnabled(False)
	self.atualizarDados()
	byte_msg = self.dados.encode('utf-8')
	tcp_client_socket.send(byte_msg)
	self.painel_substituicao.hide()

    """ A função 'ok_substituicao_B' é acionada ao clicar no botão 'Ok' no painel de substituição do time B. Ou seja,
    é a função responsável por realizar de fato a substituição após o usuário confirmar a mesma. A função testa caso
    por caso qual checkbox estar marcado nos jogadores TITULARES e nos RESERVAS e realiza a substituição, transferindo
    valores de ponto e faltas individuais de cada jogador pra suas novas variáveis. Após isso, chama a função 'atualizarDados'
    e envia os dados atualizados para o servidor atualizar, fechando o painel de substituição em seguida. """
    def ok_substituicao_B(self):
	self.botao_ok_substituicao_A.hide()
	self.botao_ok_substituicao_B.hide()
	self.painel_substituicao.hide()
	if (self.sub_jog1.isChecked()):
		novoreserva_nome = self.jog1b
		novoreserva_pts = self.jog1b_pts
		novoreserva_flt = self.jog1b_flt
		self.sub_jog1.setChecked(False)
		if (self.sub_res1.isChecked()):
			self.jog1b = self.reserva1b
			self.jog1b_pts = self.reserva1b_pts
			self.jog1b_flt = self.reserva1b_flt
			self.reserva1b = novoreserva_nome
			self.reserva1b_pts = novoreserva_pts
			self.reserva1b_flt = novoreserva_flt
		elif (self.sub_res2.isChecked()):
			self.jog1b = self.reserva2b
			self.jog1b_pts = self.reserva2b_pts
			self.jog1b_flt = self.reserva2b_flt
			self.reserva2b = novoreserva_nome
			self.reserva2b_pts = novoreserva_pts
			self.reserva2b_flt = novoreserva_flt
		elif (self.sub_res3.isChecked()):
			self.jog1b = self.reserva3b
			self.jog1b_pts = self.reserva3b_pts
			self.jog1b_flt = self.reserva3b_flt
			self.reserva3b = novoreserva_nome
			self.reserva3b_pts = novoreserva_pts
			self.reserva3b_flt = novoreserva_flt
		elif (self.sub_res4.isChecked()):
			self.jog1b = self.reserva4b
			self.jog1b_pts = self.reserva4b_pts
			self.jog1b_flt = self.reserva4b_flt
			self.reserva4b = novoreserva_nome
			self.reserva4b_pts = novoreserva_pts
			self.reserva4b_flt = novoreserva_flt
		elif (self.sub_res5.isChecked()):
			self.jog1b = self.reserva5b
			self.jog1b_pts = self.reserva5b_pts
			self.jog1b_flt = self.reserva5b_flt
			self.reserva5b = novoreserva_nome
			self.reserva5b_pts = novoreserva_pts
			self.reserva5b_flt = novoreserva_flt
		elif (self.sub_res6.isChecked()):
			self.jog1b = self.reserva6b
			self.jog1b_pts = self.reserva6b_pts
			self.jog1a_flt = self.reserva6b_flt
			self.reserva6b = novoreserva_nome
			self.reserva6b_pts = novoreserva_pts
			self.reserva6b_flt = novoreserva_flt
		else:
			self.jog1b = self.reserva7b
			self.jog1b_pts = self.reserva7b_pts
			self.jog1b_flt = self.reserva7b_flt
			self.reserva7b = novoreserva_nome
			self.reserva7b_pts = novoreserva_pts
			self.reserva7b_flt = novoreserva_flt
	elif (self.sub_jog2.isChecked()):
		novoreserva_nome = self.jog2b
		novoreserva_pts = self.jog2b_pts
		novoreserva_flt = self.jog2b_flt
		self.pt_flt_jog2.setChecked(False)
		if (self.sub_res1.isChecked()):
			self.jog2b = self.reserva1b
			self.jog2b_pts = self.reserva1b_pts
			self.jog2b_flt = self.reserva1b_flt
			self.reserva1b = novoreserva_nome
			self.reserva1b_pts = novoreserva_pts
			self.reserva1b_flt = novoreserva_flt
		elif (self.sub_res2.isChecked()):
			self.jog2b = self.reserva2b
			self.jog2b_pts = self.reserva2b_pts
			self.jog2b_flt = self.reserva2b_flt
			self.reserva2b = novoreserva_nome
			self.reserva2b_pts = novoreserva_pts
			self.reserva2b_flt = novoreserva_flt
		elif (self.sub_res3.isChecked()):
			self.jog2b = self.reserva3b
			self.jog2b_pts = self.reserva3b_pts
			self.jog2b_flt = self.reserva3b_flt
			self.reserva3b = novoreserva_nome
			self.reserva3b_pts = novoreserva_pts
			self.reserva3b_flt = novoreserva_flt
		elif (self.sub_res4.isChecked()):
			self.jog2b = self.reserva4b
			self.jog2b_pts = self.reserva4b_pts
			self.jog2b_flt = self.reserva4b_flt
			self.reserva4b = novoreserva_nome
			self.reserva4b_pts = novoreserva_pts
			self.reserva4b_flt = novoreserva_flt
		elif (self.sub_res5.isChecked()):
			self.jog2b = self.reserva5b
			self.jog2b_pts = self.reserva5b_pts
			self.jog2b_flt = self.reserva5b_flt
			self.reserva5b = novoreserva_nome
			self.reserva5b_pts = novoreserva_pts
			self.reserva5b_flt = novoreserva_flt
		elif (self.sub_res6.isChecked()):
			self.jog2b = self.reserva6b
			self.jog2b_pts = self.reserva6b_pts
			self.jog2b_flt = self.reserva6b_flt
			self.reserva6b = novoreserva_nome
			self.reserva6b_pts = novoreserva_pts
			self.reserva6b_flt = novoreserva_flt
		else:
			self.jog2b = self.reserva7b
			self.jog2b_pts = self.reserva7b_pts
			self.jog2b_flt = self.reserva7b_flt
			self.reserva7b = novoreserva_nome
			self.reserva7b_pts = novoreserva_pts
			self.reserva7b_flt = novoreserva_flt
	elif (self.sub_jog3.isChecked()):
		novoreserva_nome = self.jog3b
		novoreserva_pts = self.jog3b_pts
		novoreserva_flt = self.jog3b_flt
		self.pt_flt_jog3.setChecked(False)
		if (self.sub_res1.isChecked()):
			self.jog3b = self.reserva1b
			self.jog3b_pts = self.reserva1b_pts
			self.jog3b_flt = self.reserva1b_flt
			self.reserva1b = novoreserva_nome
			self.reserva1b_pts = novoreserva_pts
			self.reserva1b_flt = novoreserva_flt
		elif (self.sub_res2.isChecked()):
			self.jog3b = self.reserva2b
			self.jog3b_pts = self.reserva2b_pts
			self.jog3b_flt = self.reserva2b_flt
			self.reserva2b = novoreserva_nome
			self.reserva2b_pts = novoreserva_pts
			self.reserva2b_flt = novoreserva_flt
		elif (self.sub_res3.isChecked()):
			self.jog3b = self.reserva3b
			self.jog3b_pts = self.reserva3b_pts
			self.jog3b_flt = self.reserva3b_flt
			self.reserva3b = novoreserva_nome
			self.reserva3b_pts = novoreserva_pts
			self.reserva3b_flt = novoreserva_flt
		elif (self.sub_res4.isChecked()):
			self.jog3b = self.reservaba
			self.jog3b_pts = self.reservaba_pts
			self.jog3b_flt = self.reservaba_flt
			self.reserva4b = novoreserva_nome
			self.reserva4b_pts = novoreserva_pts
			self.reserva4b_flt = novoreserva_flt
		elif (self.sub_res5.isChecked()):
			self.jog3b = self.reserva5b
			self.jog3b_pts = self.reserva5b_pts
			self.jog3b_flt = self.reserva5b_flt
			self.reserva5b = novoreserva_nome
			self.reserva5b_pts = novoreserva_pts
			self.reserva5b_flt = novoreserva_flt
		elif (self.sub_res6.isChecked()):
			self.jog3b = self.reserva6b
			self.jog3b_pts = self.reserva6b_pts
			self.jog3b_flt = self.reserva6b_flt
			self.reserva6b = novoreserva_nome
			self.reserva6b_pts = novoreserva_pts
			self.reserva6b_flt = novoreserva_flt
		else:
			self.jog3b = self.reserva7b
			self.jog3b_pts = self.reserva7b_pts
			self.jog3b_flt = self.reserva7b_flt
			self.reserva7b = novoreserva_nome
			self.reserva7b_pts = novoreserva_pts
			self.reserva7b_flt = novoreserva_flt
	elif (self.sub_jog4.isChecked()):
		novoreserva_nome = self.jog4b
		novoreserva_pts = self.jog4b_pts
		novoreserva_flt = self.jog4b_flt
		self.pt_flt_jog4.setChecked(False)
		if (self.sub_res1.isChecked()):
			self.jog4b = self.reserva1b
			self.jog4b_pts = self.reserva1b_pts
			self.jog4b_flt = self.reserva1b_flt
			self.reserva1b = novoreserva_nome
			self.reserva1b_pts = novoreserva_pts
			self.reserva1b_flt = novoreserva_flt
		elif (self.sub_res2.isChecked()):
			self.jog4b = self.reserva2b
			self.jog4b_pts = self.reserva2b_pts
			self.jog4b_flt = self.reserva2b_flt
			self.reserva2b = novoreserva_nome
			self.reserva2b_pts = novoreserva_pts
			self.reserva2b_flt = novoreserva_flt
		elif (self.sub_res3.isChecked()):
			self.jog4b = self.reserva3b
			self.jog4b_pts = self.reserva3b_pts
			self.jog4b_flt = self.reserva3b_flt
			self.reserva3b = novoreserva_nome
			self.reserva3b_pts = novoreserva_pts
			self.reserva3b_flt = novoreserva_flt
		elif (self.sub_res4.isChecked()):
			self.jog4b = self.reserva4b
			self.jog4b_pts = self.reserva4b_pts
			self.jog4b_flt = self.reserva4b_flt
			self.reserva4b = novoreserva_nome
			self.reserva4b_pts = novoreserva_pts
			self.reserva4b_flt = novoreserva_flt
		elif (self.sub_res5.isChecked()):
			self.jog4b = self.reserva5b
			self.jog4b_pts = self.reserva5b_pts
			self.jog4b_flt = self.reserva5b_flt
			self.reserva5b = novoreserva_nome
			self.reserva5b_pts = novoreserva_pts
			self.reserva5b_flt = novoreserva_flt
		elif (self.sub_res6.isChecked()):
			self.jog4b = self.reserva6b
			self.jog4b_pts = self.reserva6b_pts
			self.jog4b_flt = self.reserva6b_flt
			self.reserva6b = novoreserva_nome
			self.reserva6b_pts = novoreserva_pts
			self.reserva6b_flt = novoreserva_flt
		else:
			self.jog4b = self.reserva7b
			self.jog4b_pts = self.reserva7b_pts
			self.jog4b_flt = self.reserva7b_flt
			self.reserva7b = novoreserva_nome
			self.reserva7b_pts = novoreserva_pts
			self.reserva7b_flt = novoreserva_flt
	else:
		novoreserva_nome = self.jog5b
		novoreserva_pts = self.jog5b_pts
		novoreserva_flt = self.jog5b_flt
		self.pt_flt_jog5.setChecked(False)
		if (self.sub_res1.isChecked()):
			self.jog5b = self.reserva1b
			self.jog5b_pts = self.reserva1b_pts
			self.jog5b_flt = self.reserva1b_flt
			self.reserva1b = novoreserva_nome
			self.reserva1b_pts = novoreserva_pts
			self.reserva1b_flt = novoreserva_flt
		elif (self.sub_res2.isChecked()):
			self.jog5b = self.reserva2b
			self.jog5b_pts = self.reserva2b_pts
			self.jog5b_flt = self.reserva2b_flt
			self.reserva2b = novoreserva_nome
			self.reserva2b_pts = novoreserva_pts
			self.reserva2b_flt = novoreserva_flt
		elif (self.sub_res3.isChecked()):
			self.jog5b = self.reserva3b
			self.jog5b_pts = self.reserva3b_pts
			self.jog5b_flt = self.reserva3b_flt
			self.reserva3b = novoreserva_nome
			self.reserva3b_pts = novoreserva_pts
			self.reserva3b_flt = novoreserva_flt
		elif (self.sub_res4.isChecked()):
			self.jog5b = self.reserva4b
			self.jog5b_pts = self.reserva4b_pts
			self.jog5b_flt = self.reserva4b_flt
			self.reserva4b = novoreserva_nome
			self.reserva4b_pts = novoreserva_pts
			self.reserva4b_flt = novoreserva_flt
		elif (self.sub_res5.isChecked()):
			self.jog5b = self.reserva5b
			self.jog5b_pts = self.reserva5b_pts
			self.jog5b_flt = self.reserva5b_flt
			self.reserva5b = novoreserva_nome
			self.reserva5b_pts = novoreserva_pts
			self.reserva5b_flt = novoreserva_flt
		elif (self.sub_res6.isChecked()):
			self.jog5b = self.reserva6b
			self.jog5b_pts = self.reserva6b_pts
			self.jog5b_flt = self.reserva6b_flt
			self.reserva6b = novoreserva_nome
			self.reserva6b_pts = novoreserva_pts
			self.reserva6b_flt = novoreserva_flt
		else:
			self.jog5b = self.reserva7b
			self.jog5b_pts = self.reserva7b_pts
			self.jog5b_flt = self.reserva7b_flt
			self.reserva7b = novoreserva_nome
			self.reserva7b_pts = novoreserva_pts
			self.reserva7b_flt = novoreserva_flt
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
	self.botao_desfazer.setEnabled(False)
	self.atualizarDados()
	byte_msg = self.dados.encode('utf-8')
	tcp_client_socket.send(byte_msg)
	self.painel_substituicao.hide()

    """ A função 'ok_pt_flt_A' é acionada ao clicar em 'Ok' na tela da pontuação ou falta do time A. A função realiza
    a verificação de qual jogador está marcado no checkbox e incrementa os valores de ponto ou falta total do time e
    o individual do respectivo jogador de acordo com os valores passados pelas variáveis 'pontotemp' ou 'faltatemp', 
    que armazena os valores de acordo com os botões clicados na tela de controle. """
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

    """ A função 'ok_pt_flt_B' é acionada ao clicar em 'Ok' na tela da pontuação ou falta do time B. A função realiza
    a verificação de qual jogador está marcado no checkbox e incrementa os valores de ponto ou falta total do time e
    o individual do respectivo jogador de acordo com os valores passados pelas variáveis 'pontotemp' ou 'faltatemp', 
    que armazena os valores de acordo com os botões clicados na tela de controle. """
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

    """ A função 'desfazer' é acionada ao clicar no botão 'Desfazer' na tela de controle do cliente. Ela realiza
    a alteração dos valores da variável 'dados' para os valores da variável 'dadosAnt', que armazena sempre os valores
    de uma ação atrás. Assim, qualquer pontuação ou falta realizada é desfeita. """
    def desfazer(self):
	self.dados = self.dadosAnt
	temp = self.dados.split()
	byte_msg = self.dados.encode('utf-8')
	tcp_client_socket.send(byte_msg)
	self.time_A_pts = int(temp[1])
	self.time_A_flt_total = int(temp[2])
	self.time_B_pts = int(temp[19])
	self.time_B_flt_total = int(temp[20])
	self.botao_desfazer.setEnabled(False)
	self.atualizarDadosCliente()

    """A função 'timeA_1pt' é acionada ao clicar no botão '+1' no painel do time A. Ela exibe o painel
    com todos os jogadores do time A e um checkbox em cada um, permitindo que somente UM seja marcado para determinar
    qual jogador realizou o ponto. Ela também altera os valores das variáveis 'pontotemp' para 1 e 'faltatemp' para 0. """
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
	
    """A função 'timeA_2pt' é acionada ao clicar no botão '+2' no painel do time A. Ela exibe o painel
    com todos os jogadores do time A e um checkbox em cada um, permitindo que somente UM seja marcado para determinar
    qual jogador realizou o ponto. Ela também altera os valores das variáveis 'pontotemp' para 2 e 'faltatemp' para 0. """
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
    
    """A função 'timeA_3pt' é acionada ao clicar no botão '+3' no painel do time A. Ela exibe o painel
    com todos os jogadores do time A e um checkbox em cada um, permitindo que somente UM seja marcado para determinar
    qual jogador realizou o ponto. Ela também altera os valores das variáveis 'pontotemp' para 3 e 'faltatemp' para 0. """
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

    """A função 'timeA_falta' é acionada ao clicar no botão 'Falta' no painel do time A. Ela exibe o painel
    com todos os jogadores do time A e um checkbox em cada um, permitindo que somente UM seja marcado para determinar
    qual jogador realizou a falta. Ela também altera os valores das variáveis 'pontotemp' para 0 e 'faltatemp' para 1. """
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

    """A função 'timeB_1pt' é acionada ao clicar no botão '+1' no painel do time B. Ela exibe o painel
    com todos os jogadores do time B e um checkbox em cada um, permitindo que somente UM seja marcado para determinar
    qual jogador realizou o ponto. Ela também altera os valores das variáveis 'pontotemp' para 1 e 'faltatemp' para 0. """
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
 
    """A função 'timeB_2pt' é acionada ao clicar no botão '+2' no painel do time B. Ela exibe o painel
    com todos os jogadores do time B e um checkbox em cada um, permitindo que somente UM seja marcado para determinar
    qual jogador realizou o ponto. Ela também altera os valores das variáveis 'pontotemp' para 2 e 'faltatemp' para 0. """   
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
    
    """A função 'timeB_3pt' é acionada ao clicar no botão '+3' no painel do time B. Ela exibe o painel
    com todos os jogadores do time B e um checkbox em cada um, permitindo que somente UM seja marcado para determinar
    qual jogador realizou o ponto. Ela também altera os valores das variáveis 'pontotemp' para 3 e 'faltatemp' para 0. """
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

    """A função 'timeB_falta' é acionada ao clicar no botão 'Falta' no painel do time B. Ela exibe o painel
    com todos os jogadores do time B e um checkbox em cada um, permitindo que somente UM seja marcado para determinar
    qual jogador realizou a falta. Ela também altera os valores das variáveis 'pontotemp' para 0 e 'faltatemp' para 1. """
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

    """ A função 'avancar' é acionada ao clicar no botão 'Avançar' na tela de cadastro. Ela realiza a transferências
    de todos os campos preenchidos pelo usuário na tela de cadastro e armazena em variáveis, inicializa os valores
    referente as pontuações e faltas, atualiza os valores da variavel 'dados' através da função 'atualizarDados' e 
    manda pro servidor. Além disso, ela fecha a tela de cadastro, abre a tela de controle e atualiza os dados dos times e
    altera o estado dos botões de controle. """
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
	message = self.dados
	byte_msg = message.encode('utf-8')
	tcp_client_socket.send(byte_msg)
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
	self.botao_timeA_tt.setEnabled(False)
	self.botao_timeB_tt.setEnabled(False)
	self.botao_iniciar.setEnabled(True)
	self.botao_continuar_posse.setEnabled(False)
	self.botao_zerar_posse.setEnabled(False)
	self.Controle.show()
	
        


if __name__ == '__main__' :
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
