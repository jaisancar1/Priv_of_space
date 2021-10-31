#-*- coding: UTF-8 -*-
'''
Created on 31 oct 2021

@author: Jaime
'''

from space import*

#Lectura

print("***Proyecto Privatizacion del espacio***")
datos = lectura_fichero("dataproyecto.csv")
print("Total de registros: {}".format(len(datos)))
print("Los 3 primeros {}".format(datos[3]))
print("Los 3 ultimos {}". format(datos[-3]))




