#!/usr/bin/env python3
"""Show a text-mode spectrogram using live microphone data."""

#Importe todas as bibliotecas
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
from suaBibSignal import signalMeu
import time
import peakutils


#funcao para transformas intensidade acustica em dB
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)


def main():
 
    #declare um objeto da classe da sua biblioteca de apoio (cedida)    
    #declare uma variavel com a frequencia de amostragem, sendo 44100

    signal = signalMeu()
    
    #voce importou a bilioteca sounddevice como, por exemplo, sd. entao
    # os seguintes parametros devem ser setados:
    
    sd.default.samplerate = 44100
    sd.default.channels = 2  #voce pode ter que alterar isso dependendo da sua placa
    duration = 5


    # faca um print na tela dizendo que a captacao comecará em n segundos. e entao 
    #use um time.sleep para a espera

    print("a captação começara em 5 segundos")
    time.sleep(1)
   
    #faca um print informando que a gravacao foi inicializada
    print("a gravação foi iniciada")
   
   #declare uma variavel "duracao" com a duracao em segundos da gravacao. poucos segundos ... 
   #calcule o numero de amostras "numAmostras" que serao feitas (numero de aquisicoes)

    numAmostras = 44100 * duration
    freqDeAmostragem = sd.default.samplerate
   
    audio = sd.rec(int(numAmostras), freqDeAmostragem, channels=2)
    sd.wait()
    print("...     FIM")
    
    #analise sua variavel "audio". pode ser um vetor com 1 ou 2 colunas, lista ...

    print(audio)
    print(len(audio))

    #grave uma variavel com apenas a parte que interessa (dados)
    audio_interessante = audio[0]
    

    # use a funcao linspace e crie o vetor tempo. Um instante correspondente a cada amostra!
    inicio = 0
    fim = 5
    numPontos = 44100 * (fim - inicio)

    t = np.linspace(inicio,fim,numPontos)

    # plot do grafico  áudio vs tempo!


    plt.figure("F(y)")
    plt.plot(t,audio[:,0])
    plt.grid()
    plt.title('Fourier audio')
   
    
    ## Calcula e exibe o Fourier do sinal audio. como saida tem-se a amplitude e as frequencias
    y = audio[:,0]
    fs = 44100
    xf, yf = signal.calcFFT(y, fs)
    plt.figure("F(y)")
    plt.plot(xf,yf)
    plt.grid()
    plt.title('Fourier audio')
    

    #esta funcao analisa o fourier e encontra os picos
    #voce deve aprender a usa-la. ha como ajustar a sensibilidade, ou seja, o que é um pico?
    #voce deve tambem evitar que dois picos proximos sejam identificados, pois pequenas variacoes na
    #frequencia do sinal podem gerar mais de um pico, e na verdade tempos apenas 1.
   
    index = peakutils.indexes(np.abs(yf),0.2,50)

    lista_picos = []

    print("******")
    for v in index:
        print(xf[v])
        lista_picos.append(xf[v])

    if min(lista_picos) < 720:
        if max(lista_picos) < 1250:
            print("A tecla digitada digitado foi a 1")
        elif max(lista_picos) < 1370:
            print("A tecla digitada digitado foi a 2")
        elif max(lista_picos) < 1490:
            print("A tecla digitada digitado foi a 3")
        else:
            print("A tecla digitada digitado foi a A")

    elif min(lista_picos) < 780:
        if max(lista_picos) < 1250:
            print("A tecla digitada digitado foi a 4")
        elif max(lista_picos) < 1370:
            print("A tecla digitada digitado foi a 5")
        elif max(lista_picos) < 1490:
            print("A tecla digitada digitado foi a 6")
        else:
            print("A tecla digitada digitado foi a B")

    elif min(lista_picos) < 870:
        if max(lista_picos) < 1250:
            print("A tecla digitada digitado foi a 7")
        elif max(lista_picos) < 1370:
            print("A tecla digitada digitado foi a 8")
        elif max(lista_picos) < 1490:
            print("A tecla digitada digitado foi a 9")
        else:
            print("A tecla digitada digitado foi a C")

    elif min(lista_picos) < 960:
        if max(lista_picos) < 1250:
            print("A tecla digitada digitado foi a X")
        elif max(lista_picos) < 1370:
            print("A tecla digitada digitado foi a 0")
        elif max(lista_picos) < 1490:
            print("A tecla digitada digitado foi a #")
        else:
            print("A tecla digitada digitado foi a D")


    
    #printe os picos encontrados! 
    
    #encontre na tabela duas frequencias proximas às frequencias de pico encontradas e descubra qual foi a tecla
    #print a tecla.
    
  
    ## Exibe gráficos
    plt.show()

if __name__ == "__main__":
    main()
