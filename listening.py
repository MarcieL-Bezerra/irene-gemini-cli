import random
import speech_recognition as sr 

class Listen:
    def __init__(self):
         self.statusFala="Aguarde uns segundos e fale"
        

    def listen_microphone(self):
        r = sr.Recognizer()
        mic = sr.Microphone()
        while True:
            with mic as fonte:
                    r.adjust_for_ambient_noise(fonte)
                    self.statusFala = "Pode falar:"
                    print(self.statusFala)
                    audio = r.listen(fonte)
                    try:
                        texto = r.recognize_google(audio, language="pt-BR")
                        print("Voce falou: " + texto)
                        return texto
                    except Exception as e:
                        possiveis_falas = ['Você disse algo?', 'Se falou algo não ouvi','Não te entendi','Tente falar pausadamente','Verifique se o microfone está ok','Nem sei o que dizer']
                        sorteados = random.randint(0, 5)
                        texto_pronto = possiveis_falas[sorteados]
                        texto = ""
                        print("Você disse: {}".format(texto_pronto))
                        return texto_pronto
            
if __name__ == '__main__':
    Listen().listen_microphone()
            