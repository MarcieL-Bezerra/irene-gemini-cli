import os
from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import talking
import listening
import mintgenine
import cleanFiles
import arquivos.conversas as conver

class Attitude():
    def __init__(self,frase):
        self.frase = frase
        self.resposta = ""
        

    def action(self):
        possiveis_falas = ['Você disse algo?', 'Se falou algo não ouvi','Não te entendi','Tente falar pausadamente','Verifique se o microfone está ok','Nem sei o que dizer']
        saindo = 'SAIR' in self.frase.upper()
        questao = 'QUESTÃO' in self.frase.upper()
        if self.frase in possiveis_falas:
            return self.frase
        if saindo ==True:
            print("Saindo! Até logo.")
            talking.Talking("Até logo")
            cleanFiles.LimpaConversas()
            os._exit(1)

        if questao ==True:
            print("Legal, agora com a integração com a Gemine consigo tudo")
            talking.Talking("Legal, agora com a integração com a Gemine consigo tudo")
            print("Aguarde um pouco pra falar.")
            pergunta = listening.Listen().listen_microphone(self.falinha)
            if not pergunta in possiveis_falas:
                 self.resposta = mintgenine.miGenine(pergunta)
                 self.resposta = self.resposta.replace("*", " ")             
                 return f"Essa foi a resposta da Gemini: {self.resposta}"
            else:
                return pergunta
            
        if not self.frase in possiveis_falas:    
            bot = ChatBot('irene',
                        storage_adapter='chatterbot.storage.SQLStorageAdapter',
                        database_uri='sqlite:///database.sqlite3'
                        )
            conversa = ListTrainer(bot)
            conversa.train(conver.conversas)
            resposta = bot.get_response(self.frase)
            return str(resposta)
        else:
            return self.frase

    


if __name__ == '__main__':
    print(Attitude("Vocé é muito inteligente").action())