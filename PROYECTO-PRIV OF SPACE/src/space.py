#-*- coding: UTF-8 -*-
'''
Created on 30 oct 2021

@author: Jaime
'''

import csv
from collections import namedtuple
from Parseo import *
from datetime import date,time




Info = namedtuple('info','company_name, location, status_rocket, rocket, status_mission,\
                   country_of_launch, date, time, billions_spended')


def lectura_fichero(fichero):
    '''
    Devuelve una lista de tuplas de tipo Info a partir de los datos incluidos en el fichero
    csv dado como parámetro. El fichero debe estar codificado en formato utf-8.
    @param fichero: Nombre y ruta del fichero csv a leer. 
    @type fichero:srt
    @return: Una lista de tuplas de tipo Info con todos los datos del csv
    @rtype: [ Info(str, str, boolean, int, boolean, str, date, time, float,)]  
    '''
    res = list()
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(f)
        for registro in lector:
            res.append((registro[0]),(registro[1]),parseo_status_rocket(registro[2]),int(registro[3]), \
                       parseo_status_mission(registro[4]),(registro[5]),datetime. strptime(registro[6]),time(registro[7]), float(registro[8]) )
                        
    return res
