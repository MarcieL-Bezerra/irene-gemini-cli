import platform
import os

def LimpaConversas():
        caminhoinicial = './conversas'
        meusistema=platform.system().upper()
        files = os.listdir(caminhoinicial)
        with open("arquivos/dados.txt", "w") as arquivo:
            arquivo.write("0")
            arquivo.close()            
        if meusistema == "WINDOWS":
            files_mp3=[caminhoinicial + '\\' + f for f in files if f[-3:]== 'mp3']
        else:
            files_mp3 =[caminhoinicial + '/' + f for f in files if f[-3:]== 'mp3']
        for f in files_mp3:
            os.remove(f)