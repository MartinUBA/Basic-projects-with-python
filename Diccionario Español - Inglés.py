# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 17:44:03 2021

@author: Martin
"""

diccionario={}

palabra = input("Introduce la lista de palabras y traducciones en formato palabra:traduccion separadas por comas: ")
palabra1= palabra.split(",") # Separo con comas la combinacion "palabra:traduccion"
for i in palabra1:
    clave, valor = i.split(":")
    diccionario[clave]= valor
    
frase = input("Introduzca una frase: ")
frase1= frase.split()
for i in frase1:
    if i in diccionario:
        print(diccionario[i],end=" ")
    else:
        print(i, end= " ")