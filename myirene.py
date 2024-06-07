import os
import threading
from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
import time
import requests

import talking
import listening
import attitude
import cleanFiles

qhoras = datetime.now().strftime('%H:%M:%S')
hora_atual = datetime.now().strftime('%H')
#hora_atual = hora_atual.strftime('%H')
saudacao = ""
if int(hora_atual) < 12 :
    saudacao = 'Bom dia'
elif int(hora_atual) >= 12 and int(hora_atual) < 18:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'


class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.LimpaConversas()
        self.start()
        self.check_internet()

    def LimpaConversas(self):
        cleanFiles.LimpaConversas()
    
    def falando_ouvido(self):
        conversando = True
        while conversando:
            faladoStatus = listening.Listen().statusFala
            print(faladoStatus)
            frase = listening.Listen().listen_microphone()
            agindo = attitude.Attitude(frase)
            novaFrase = agindo.action()

            if novaFrase:
                frase = novaFrase
            print(frase)
            talking.Talking(frase)
    
    def check_internet(self):
        url='http://www.google.com/'
        timeout=5
        try:
            _ = requests.get(url, timeout=timeout)
            #----- inicia novas conversas
            print(saudacao + ", Meu nome é Irene! conheço algumas funções desse computador, posso ajudar?")
            talking.Talking(saudacao + ", Meu nome é Irene! conheço algumas funções desse computador, posso ajudar?")
            self.falando_ouvido()
        except requests.ConnectionError:
            #ouvir_microfone()
            self.vazando()
        finally:
            self.vazando


        

    def vazando(self):
        talking.Talking("Não posso te ajudar, você está sem internet! " + saudacao)
        print("Não posso te ajudar, você está sem internet!")
        time.sleep(10)
        os._exit(1)
        
        
app = App()
