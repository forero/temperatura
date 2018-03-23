#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: CatalinaBernal
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq


datos = np.loadtxt('tempdiaria.txt', dtype = 'string', skiprows = 1)
nestacion = datos[:,1]
nanual = datos[:,2]
nmes = datos[:,3]
ndia = datos[:,4]
ndato = datos[:,5]

estacion = list()
anual = list()
mes = list()
dia = list()
dato = list()

for i in range(len(ndato)):
    ndato[i] = ndato[i].replace(",", ".")

for i in range(len(nanual)):
    estacion.append(nestacion[i])
    anual.append(float(nanual[i]))
    mes.append(float(nmes[i]))
    dia.append(float(ndia[i]))
    dato.append(float(ndato[i]))
    
t = list()
for i in range(len(anual)):
    t.append(anual[i] + ((mes[i]-1.0)/float(12)) + ((dia[i]-1.0)/float(365)))
    
#plt.scatter(t, dato, s=0.3)


dato_isla = list()
dato_nuevo = list()
dato_paraiso = list()
t_isla = list()
t_nuevo = list()
t_paraiso = list()

for i in range(len(estacion)):
    e = estacion[i]
    if(e=='ISLA'):
        dato_isla.append(dato[i])
        t_isla.append(t[i])
        
    if(e=='NUEVO'):
        dato_nuevo.append(dato[i])
        t_nuevo.append(t[i])
        
    if(e=='PARAISO'):
        dato_paraiso.append(dato[i])
        t_paraiso.append(t[i])
        

dt = 1/float(365)

plt.figure()        
#Fourier ISLA
ni = len(dato_isla)

fft_t1 = fft(dato_isla)
freq1 = fftfreq(ni, dt)

fft_t1_shifted = np.fft.fftshift(fft_t1)
freq1_shifted = np.fft.fftshift(freq1)


clean_f1 = np.fft.ifft(fft_t1_shifted) 
plt.scatter(t_isla, dato_isla, s=0.3)
plt.scatter(t_isla, np.real(clean_f1), s=0.3, color='green')



plt.figure()
#Fourier NUEVO
nn = len(dato_nuevo)
fft_t2 = fft(dato_nuevo)
freq2 = fftfreq(nn, dt)

fft_t2_shifted = np.fft.fftshift(fft_t2)
freq2_shifted = np.fft.fftshift(freq2)

clean_f2 = np.fft.ifft(fft_t2_shifted) 
plt.scatter(t_nuevo, dato_nuevo, s=0.3)
plt.scatter(t_nuevo,np.real(clean_f2), s=0.3, color='green')
plt.ylim(7.5)

plt.figure()
#Fourier PARAISO
np= len(dato_paraiso)

fft_t3 = fft(dato_paraiso)
freq3 = fftfreq(np, dt)

print type(dato_paraiso[0])
fft_t3_shifted = np.fft.fftshift(fft_t3)
freq3_shifted = np.fft.fftshift(freq3)


clean_f3 = np.fft.ifft(fft_t3_shifted) 
plt.scatter(t_paraiso, dato_paraiso, s=0.3)
plt.scatter(t_paraiso,np.real(clean_f3), s=0.3, color='green')