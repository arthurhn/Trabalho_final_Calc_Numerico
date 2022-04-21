# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 18:16:40 2020
@author: arthu
"""
import ajuste as aj

arq = open('final.txt', 'r')
valores = arq.read().split()
arq.close()

aj.grafico(valores)