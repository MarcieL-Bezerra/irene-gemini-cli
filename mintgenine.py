import google.generativeai as genai
import acessos as key

def miGenine(texto):
    genai.configure(api_key=key.SECRET_KEY)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(texto)
    
    # print("Gemini:", response.text, "\n")
    return response.text



if __name__ == '__main__':
    miGenine("O que é linguagem de programação?")