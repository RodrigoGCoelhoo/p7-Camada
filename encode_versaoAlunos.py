#importe as bibliotecas
import sys
import numpy as np
import sounddevice as sd
from suaBibSignal import signalMeu
import matplotlib.pyplot as plt

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

#converte intensidade em Db, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)

def main():
    print("Inicializando encoder")
    
    #declare um objeto da classe da sua biblioteca de apoio (cedida) 
    s = signalMeu()

    #declare uma variavel com a frequencia de amostragem, sendo 44100
    freq_amostragem = 44100
    
    #voce importou a bilioteca sounddevice como, por exemplo, sd. entao
    # os seguintes parametros devem ser setados:
    
    duration = 5
      
    #relativo ao volume. Um ganho alto pode saturar sua placa... comece com .3    
    gainX  = 0.3
    gainY  = 0.3

    print("Gerando Tons base")

    dic_tons = {0:[941, 1336],
                1:[697, 1209],
                2:[697, 1336],
                3:[697, 1477],
                4:[770, 1209],
                5:[770, 1336],
                6:[770, 1477],
                7:[852, 1209],
                8:[852, 1336],
                9:[852, 1477]
                }

    #printe a mensagem para o usuario teclar um numero de 0 a 9. 
    while True:
        ton_escolhido = int(input("Escolha um tom entre 0 e 9:\n"))
        if 0 < ton_escolhido < 9:
            break
        print("Entrada inválida")

    #gere duas senoides para cada frequencia da tabela DTMF ! Canal x e canal y 
    #use para isso sua biblioteca (cedida)
    sin_x = s.generateSin(dic_tons[ton_escolhido][0], gainX, duration, freq_amostragem)
    sin_y = s.generateSin(dic_tons[ton_escolhido][1], gainY, duration, freq_amostragem)
    
    # Plotando X
    plt.figure(figsize=(8,8))
    plt.grid()
    plt.title("Curva senóide X")
    l = [0, 0.01, -1, 1]
    plt.axis(l)
    plt.plot(sin_x[0], sin_x[1])
    plt.show()

    # Plotando Y
    plt.figure(figsize=(8,8))
    plt.grid()
    plt.title("Curva senóide Y")
    l = [0, 0.01, -1, 1]
    plt.axis(l)
    plt.plot(sin_y[0], sin_y[1])
    plt.show()

    #nao aceite outro valor de entrada.
    print("Gerando Tom referente ao símbolo : {}".format(ton_escolhido))
    
    #construa o sinal a ser reproduzido. nao se esqueca de que é a soma das senoides
    tempo = sin_x[0]
    soma_senoides = sin_x[1] + sin_y[1]

    # Plotando soma
    plt.figure(figsize=(8,8))
    plt.grid()
    plt.title("Soma senóides")
    l = [0, 0.01, -1, 1]
    plt.axis(l)
    plt.plot(tempo, soma_senoides)
    plt.show()
    
    tone = soma_senoides
    # reproduz o som
    sd.play(tone, freq_amostragem)

    # aguarda fim do audio
    sd.wait()

if __name__ == "__main__":
    main()
