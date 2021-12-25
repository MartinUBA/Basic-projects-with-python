# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:52:35 2020

@author: Martin
"""

import random 
import time 

def simulacion(): 
    i=0
    respuesta= "s"
    
    while i <= 9 and respuesta == "s":   #La idea es que se tiren los dados 10 veces como máximo
        
        dado1= random.choice([1,2,3,4,5,6]) #Selecciono un numero random entre 1 y 6
        print("El valor del primer dado es:", dado1)
        time.sleep(1)

        dado2= random.choice([1,2,3,4,5,6]) #Selecciono un numero random entre 1 y 6
        print("El valor del segundo dado es:", dado2)
        
        
        Suma= dado1+dado2
        i = i + 1 # Sumo 1 al contador i
        print("Tirada N°:", i)
        time.sleep(3)
        print("La suma de ambos dados es: ", Suma)
        time.sleep(1)
       
            
        print("¿Desea tirar nuevamente?")
        respuesta = input("Quieres intentarlo otra vez? (s/n)")
        time.sleep (1)
    else:
        print("Gracias por utilizar el programa") #Aca se acabaron los intentos
        
    
    return 


simulacion()s
