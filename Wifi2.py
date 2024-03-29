import numpy as np
from numpy.random import seed
from numpy.random import randint
from decimal import *
import random as rn 
#seed(1)
getcontext().prec = 8
Byt= 8.0  #Size of a Byte
DIFS = 40.0*Byt
SIFS =  20.0*Byt
Datos = 1500.0*Byt
Ack = 40.0*Byt 

Rbps = 1000.00 #1000kbps = 1Mbps




T_DIFS = DIFS/Rbps
print "Tiempo de transmision de DIFS: ", T_DIFS, "ms"
T_SIFS = SIFS/Rbps
print "Tiempo de transmision de SIFS: ", T_SIFS, "ms"     
T_Datos = Datos/Rbps
print "Tiempo de transmision de Datos: ", T_Datos, "ms"
T_Ack = Ack/Rbps
print "Tiempo de transmision de  Ack ", T_Ack, "ms"
print "-------------------------------------------------------------------------------------------------------------------------"
print "Arreglo de tiempos: + "



def EB(times): #Exponential Backup function. 
    fullWindow = range(0, 16*times, 1)
    CW =rn.choice(fullWindow)
    #CW = rn.choice(range(0, 16*times, 1))
    #CW = rn.randrange(0, 16*times,1)
    #print fullWindow
    #print CW
    CW_inDIFS = CW*DIFS
    #print CW_inDIFS
    Times_CW_inDIFS = CW_inDIFS/Rbps
    #print Times_CW_inDIFS
    return Times_CW_inDIFS,CW


SLargo = T_Datos + T_SIFS + T_Ack
SCorto = T_DIFS

times_array = (np.zeros((1001,6), dtype=np.dtype(Decimal)))

PromWin = 0.0
CW1 = 0

i=0
j=0
for i in range (0,1000):
    Times_CW_inDIFS,CW1 = EB(1)

    times_array[[i],[0]] += 0   #Time 0
    times_array[[i],[1]] = times_array[[i],[0]] + T_DIFS #Add DIFS time
    times_array[[i],[2]] = times_array[[i],[1]] + T_Datos #Add Data time
    times_array[[i],[3]] = times_array[[i],[2]] + T_SIFS #Add SIFS time
    times_array[[i],[4]] = times_array[[i],[3]] + T_Ack #Add ACK Time
    times_array[[i],[5]] = times_array[[i],[4]] + Times_CW_inDIFS #Add EB times, defined as DIFS unit times
    times_array[[i+1],[0]] = times_array[[i],[5]] #Next transmision time 0 = last time of previous transmision
    PromWin += CW1  #Add of all EB times 
    
print times_array
print "-------------------------------------------------------------------------------------------------------------------------"

R_experimental = (1000*Datos)/ times_array[999][5]
print "La velocidad de transmision promedio es : ", R_experimental, "Kbps"
#print PromWin
print "El valor promedio de valores tomados por EB es: ", PromWin/1000
#print PromWin