# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:32:10 2020

@author: arthu
"""
import numpy as np
import matplotlib.pylab as plt

def ajusta(x,y):
    n = len(x)
    
    soma_x  = 0.0
    soma_x2 = 0.0
    soma_y  = 0.0
    soma_xy = 0.0
    for i in range(n):
        soma_x  += x[i]
        soma_x2 += x[i]**2
        soma_y  += y[i]
        soma_xy += x[i]*y[i]
  
    den = n*soma_x2 - soma_x**2
    a0  = (soma_x2*soma_y - soma_xy*soma_x)/float(den)
    a1  = (n*soma_xy - soma_x*soma_y)/float(den)
    return a1, a0

def lineariza(x,y):
  X = np.log(x)
  Y = np.log(y)
  
  c, d = ajusta(X, Y)
  
  D = np.exp(d)
  
  return c,D

def tempo(h):
    t = (2*h/9.81)**0.5
    return np.float(t)

def grafico(lista):
    medias = []
    desvios = []
    
    for i in range (0,6):
        medias.append(float(lista[1+3*i]))
        desvios.append(float(lista[2+3*i]))
    
    
    x = np.linspace(float(lista[0]), float(lista[15]), 6)
    tempo2 = np.vectorize(tempo)
    
    y = tempo2(x) + desvios
    a,b = lineariza(x,y)
    Y = b*(x**a)
    
    novo_g = 2/(b**2)
    print(novo_g)
    
    plt.errorbar(x, medias, yerr = desvios, fmt='o', c = 'red', label = "Experimental")
    plt.plot(x, Y, "g-", label = "$g = 8.036 m/s^2$")
    plt.plot(x, tempo2(x), "b-", label = "$g = 9.81 m/s^2$")
    
    plt.xlabel('Altura (m)')
    plt.ylabel('Tempo (s)')
    plt.grid()
    plt.margins()
    plt.legend(loc = 'upper left')
    plt.show()