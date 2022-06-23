from speech_recognition import Microphone, Recognizer, UnknownValueError
import pyautogui
import pyttsx3
from  time import localtime, sleep
import pyperclip
import random
import time

criatura = pyttsx3.init()
recog = Recognizer()
mic = Microphone()


def fala_criatura(fala):
    criatura.setProperty('rate', 195)
    criatura.say(fala)
    criatura.runAndWait()
    return()

while True:
    with mic:
        fala_criatura('diga a senha')
        audio1 = recog.listen(mic)
    try:
        recognizedsenha = recog.recognize_google(audio1, language='pt').lower()         
        if recognizedsenha in 'lucas':
            fala_criatura('acesso, liberado... Vamos começaar, luucas')            
            while True:
                with mic:
                    fala_criatura('')
                    audio = recog.listen(mic)
                try:
                    recognized = recog.recognize_google(audio, language='pt').lower()
                    print(f'você disse: {recognized}')

# COMANDOS CONVERSA >>>>>>>>>>>>>>>>>>>>>
                    if recognized in 'olá''oi''oie''olá rejane''oi rejane''oie rejane':
                        conv1 = ['olá, luucas ? no que posso ajudar ?','posso lhe ajudar? Luucas?','olá, Luucas ? o que vamos fazer agora ?', 'olá, o que iremos fazer hoje, Luucas']
                        fala_criatura(random.choice(conv1))
                    elif recognized in 'tudo bem'' tudo bom''tudo bem rejane''tudo bom rejane':
                        conv2 = ['tudo bem sim e com você?', 'eu estou muito bem hoje. e você, Luucas?', 'tudo indo muito bem. E com você, Luucas?', 'estou muito bem. hoje está um dia maravilhoso']
                        fala_criatura(random.choice(conv2))
                    elif recognized in 'bom dia''bom dia rejane':
                        x = time.localtime()
                        hora = x[3]
                        minuto = x[4]
                        if hora >= 12 and hora < 18:
                            fala_criatura('não é mais bom dia, já passou do meio dia, agora é boa tarde')
                        elif hora >=18:
                            fala_criatura('LUUCAAS, tu tá louco? agora é noite, são {} horas e {} minutos'.format(hora, minuto))
                        else:
                            conv3 = ['bom dia, lucas', 'bom dia', 'bom dia Luucas, como está sendo sua manhã?']
                            fala_criatura(random.choice(conv3))
                    elif recognized in 'boa tarde''boa tarde rejane':
                        x = time.localtime()
                        hora = x[3]
                        minuto = x[4]
                        if hora < 12:
                            fala_criatura('ainda não é de tarde, ainda estamos antes do meio dia, agora é {} horas e {} minutos'.format(hora, minuto))
                        elif hora >= 19:
                            fala_criatura('já passamos da tarde, agora já é noite, Luucas são {} horas e {} minutos'.format(hora, minuto))
                        else:
                            conv4 = ['boa tarde, Luucas', 'boa tarde, o que vamos fazer hoje, Luucas?'] 
                            fala_criatura('boa tarde, lucas')
                    elif recognized in 'boa noite''boa noite rejane':
                        x = time.localtime()
                        hora = x[3]
                        minuto = x[4]
                        if hora < 19 and hora >= 12:
                            fala_criatura('ainda não é noite Luucas são apenas {} horas e {} minutos'.format(hora, minuto))
                        elif hora < 12 :
                            fala_criatura('LUUCAAS, tu tá Maluco? são apenas {} horas e {} minutos, é manhã'.format(hora, minuto))
                        else:
                            fala_criatura('boa noite, lucas')
                    elif recognized in 'bem''estou bem''to bem''estou bem rejane''to bem rejane''to super bem rejane''bem rejane''estou bem rejane':
                        fala_criatura('que bom, no que vou poder ajudar você agora?')
                    elif recognized in 'quem é você''qual seu nome''quem tu é''qual teu nome''quem é tu''qual é o teu nome''qual o seu nome''qual o teu nome''qual é o seu nome''como se chama''como tu se chama''como você se chama':
                        fala_criatura('meu nome é Re jane, fui criada para auxiliar em suas tarefas virtuais no dia-a-dia')
                    elif recognized in 'escreva''ecrever''escreve':
                        fala_criatura('escrevendo')
                        while True:
                            with mic:
                                audio2 = recog.listen(mic)
                                try:
                                    recognizedescreva = recog.recognize_google(audio2, language='pt')
                                    pyperclip.copy(recognizedescreva)
                                    if recognizedescreva in 'desativar escrita''desativa escrita''desativa a escrita''cancela''cancelar escrita''cancela a escrita''cancela escrita''cancelar a escrita':
                                        fala_criatura('modo de escrita, desativado')
                                        break
                                    elif recognizedescreva in 'ok''Ok''OK''Okay''okay':
                                        pyautogui.press('enter')
                                        break
                                    elif recognizedescreva in 'ponto''ponto final':
                                        pyautogui.press('backspace')
                                        pyautogui.write('.')
                                        pyautogui.press('space')
                                    elif recognizedescreva in 'interrogação':
                                        pyautogui.press('backspace')
                                        interr = str('?')
                                        pyperclip.copy(interr)
                                        pyautogui.hotkey('ctrl', 'v')
                                        pyautogui.press('space')
                                    elif recognizedescreva in 'exclamação':
                                        pyautogui.press('backspace')
                                        excla = str('!')
                                        pyperclip.copy(excla)
                                        pyautogui.hotkey('ctrl', 'v')
                                        pyautogui.press('space')
                                    elif recognizedescreva in 'vírgula''virgula':
                                        pyautogui.press('backspace')
                                        pyautogui.write(',')
                                        pyautogui.press('space')
                                    
                                    elif recognizedescreva in 'apagar''apague''apaga':
                                        pyautogui.hotkey('ctrl', 'shift', 'left')
                                        pyautogui.press('backspace')
                                        
                                    elif recognizedescreva in 'apagar 2''apagar dois''apague 2' \
                                                              'apague dois''apaga 2''apaga dois':
                                        pyautogui.press(['backspace', 'backspace'])
                                    elif recognizedescreva in 'apagar 3''apagar três''apague 3'\
                                                              'apague três''apaga 3''apaga três':
                                        pyautogui.press(['backspace', 'backspace', 'backspace'])
                                    elif recognizedescreva in 'apagar tudo''apague tudo''apaga tudo':
                                        pyautogui.press(['backspace']*100)
                                    elif recognizedescreva in 'letra maiúscula''letra minúscula''letra maiuscula''letra minuscula':
                                        pyautogui.press('capslock')
                                        fala_criatura('{}'.format(recognizedescreva))

                  #EXTRA                   >>>>>>>>>>>>>>><<<<<<<<<<<<<<   # AJUDANDO A MONTAR GRAFICO TEMPORAL:   >>>>>>>><<<<<<<<<

                                    elif recognizedescreva in 'crie um grafico anual''gráfico anual''criar gráfico anual''gráfico comparativo anual':
                                        pyautogui.write("import matplotlib.pyplot as plt\nx = []\ny = []\nz = []\nw = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']\nplt.title('GRAFICO ANUAL')\nplt.plot(w, x)\nplt.plot(w, y)\nplt.plot(w, z)\nplt.show()")
                                    elif recognizedescreva in 'crie um grafico semestral''gráfico semestral''criar gráfico semestral''gráfico comparativo semestral':
                                        pyautogui.write("import matplotlib.pyplot as plt\nx = []\ny = []\nz = []\nw = ['Primeiro Semestre','Segundo Semestre']\nplt.title('GRAFICO SEMESTRAL')\nplt.plot(w, x)\nplt.plot(w, y)\nplt.plot(w, z)\nplt.show()")
                                    elif recognizedescreva in 'crie um grafico trimestral''gráfico trimestral''criar gráfico trimestral''gráfico comparativo trimestral':
                                        pyautogui.write("import matplotlib.pyplot as plt\nx = []\ny = []\nz = []\nw = ['(1)TRI','(2)TRI','(3)TRI','(4)TRI']\nplt.title('GRAFICO TRIMESTRAL')\nplt.plot(w, x)\nplt.plot(w, y)\nplt.plot(w, z)plt.show()")
                                    elif recognizedescreva in 'crie um grafico bimestral''gráfico bimestral''criar gráfico bimestral''gráfico comparativo bimestral':
                                        pyautogui.write("import matplotlib.pyplot as plt\nx = []\ny = []\nz = []\nw = ['(1)BI','(2)BI','(3)BI','(4)BI','(5)BI','(6)BI']\nplt.title('GRAFICO BIMESTRAL')\nplt.plot(w, x)\nplt.plot(w, y)\nplt.plot(w, z)\nplt.show()")
                                    else:
                                        pyautogui.hotkey('ctrl', 'v')
                                        pyautogui.press('space')
                                        continue
                                except UnknownValueError:
                                    fala_criatura('')




                except UnknownValueError:
                    fala_criatura('')
        else:
            fala_criatura('senha incorreta, acesso negado!')
    except UnknownValueError:
        fala_criatura('não intendi, repita a senha por favor')
