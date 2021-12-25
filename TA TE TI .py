# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:28:56 2021

@author: Martin
"""
import time


def TATETI():
        #Modul de inicio
    print("Bienvenido al juego TA - TE - TI")
    time.sleep(2)
    
    ver_tablero()
 
 
    print("Usted comienza primero y juega con X")
  
    
    time.sleep(2)
    turno()
    time.sleep(2)
    
tablerovacio= ["-","-","-","-","-","-","-","-","-"]

ganador= None

#Modulo del tablero
def ver_tablero():
    global ganador
    print("\n")
    print(tablerovacio[0] + "|" + tablerovacio[1] + "|" + tablerovacio [2] + "|" +"     1|2|3")
    print(tablerovacio[3] + "|" + tablerovacio[4] + "|" + tablerovacio [5] + "|" +"     4|5|6")
    print(tablerovacio[6] + "|" + tablerovacio[7] + "|" + tablerovacio [8] + "|" +"     7|8|9")
    print("\n")
    print()


time.sleep(2)

# En este modulo defino la jugada  
def turno():
    global ganador
    
    for i in range(5): #El primer jugador tiene un máximo de 5 jugadas
        print ("Turno PRIMER JUGADOR, ¿En cuál casillero desea colocar su X?")
        valor= "X"
        jugada(valor)
        huboganador()
        if ganador != "X" and i < 4 :
            
            for j in range(4): # El segundo jugador tiene un máximo de 4 jugadas
                    print ("Turno SEGUNDO JUGADOR, ¿En cuál casillero desea colocar su O?")
                    valor="O"
                    jugada(valor)
                    huboganador()
                    
                    if ganador == "O":
                        print( "Felicidades jugador 2 !! ganaste")
                    break
        elif ganador == "X":
            
            print("Felicidades jugador 1 !! ganaste")
            break
        else:
            print( "Empate!")
        

#En este modulo coloco el ciclo para seguir jugando
def jugada(valor):
    anoto= False
    
    while anoto == False:
        Casillero = int(input( "Especifique el casillero de 1 a 9: "))
        Casillero = Casillero- 1
                        
        if tablerovacio[Casillero] == "-":
            anoto= True        
        else:
            print("Ese casillero está ocupado")
        
    tablerovacio[Casillero]= valor
    ver_tablero()
        
#Defino las distintas combinaciones para ganar             
    
def huboganador():
    global ganador
    controllinea()
    controlvertical()
    controldiagonal()
        
def controllinea():
    global ganador
    if tablerovacio[0]== tablerovacio[1] == tablerovacio[2] != "-":
        ganador = tablerovacio[0]
    elif tablerovacio[3]== tablerovacio[4] == tablerovacio[5] != "-":
        ganador = tablerovacio[3]
    elif tablerovacio[6]== tablerovacio[7] == tablerovacio[8] != "-":
        ganador = tablerovacio[6]
        
def controlvertical():
    global ganador
    if tablerovacio[0]== tablerovacio[3] == tablerovacio[6] != "-":
        ganador = tablerovacio[0]
    elif tablerovacio[1]== tablerovacio[4] == tablerovacio[7] != "-":
        ganador = tablerovacio[1] 
    elif tablerovacio[2]== tablerovacio[5] == tablerovacio[8] != "-":
        ganador = tablerovacio[2]
        
def controldiagonal():
    global ganador
    if tablerovacio[0]== tablerovacio[4] == tablerovacio[8] != "-":
        ganador = tablerovacio[0]
    elif tablerovacio[2]== tablerovacio[4] == tablerovacio[6] != "-":
        ganador = tablerovacio[2]
        
         
    
        




