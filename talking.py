from gtts import gTTS
from playsound import playsound

class Talking():
    def __init__(self,texto):
        self.texto = texto
        self.contador = ""
        self.answering()

    def answering(self):
        try:
            
            self.openDataFile()
            voz = gTTS(self.texto, lang="pt")
            voz.save('./conversas/voz' + str(self.contador) + '.mp3')
            falar = './conversas/voz' + str(self.contador) + '.mp3'
            playsound(falar) 
        except:
            voz = gTTS("Você pode tentar novamente?", lang="pt")
            voz.save('./conversas/voz' + str(self.contador) + '.mp3')
            falar = './conversas/voz' + str(self.contador) + '.mp3'
            playsound(falar) 

    def openDataFile(self):
        with open("arquivos/dados.txt", "r") as arquivo:
            self.contador = arquivo.read()
            arquivo.close()
            
        with open("arquivos/dados.txt", "w") as arquivo:
            newContador = str(int(self.contador) + 1)
            arquivo.write(newContador)
            arquivo.close()
if __name__ == '__main__':
    Talking("Oi Boa Tarde")