#-*- coding: UTF-8 -*-
'''
Created on 31 oct 2021

@author: Jaime
'''

from datetime import datetime

def parseo_status_rocket(cadena):
    '''
    Toma una cadena y si la cadena contiene el literal 'verdadero' (indpendientemente
    de si está escrtio en mayúsculas o minúsculas) la función devuelve 'Mujer', si contiene
    el literal 'falso' entonces devuelve 'Hombre' y con cualquier otra cadena, devuelve None.
    
    @param cadena: Cadena de caracteres con el valor verdadero
    @type cadena: str
    @return: 'Status Active', 'Status Retired' o None, dependiendo de si la cadena que se pasa como parámetro 
    tiene el literal 'verdadero', el literal 'falso' o cualquier otra cadena
    @rtype: str 
    '''
    res = None
    cadena = cadena.upper()
    if cadena == 'VERDADERO':
        res ='Status Active'
    elif cadena == 'FALSO':
        res='Status Retired'
    return res


def parseo_status_mission(cadena):
    '''
    Toma una cadena y si la cadena contiene el literal 'verdadero' (indpendientemente
    de si está escrtio en mayúsculas o minúsculas) la función devuelve 'Mujer', si contiene
    el literal 'falso' entonces devuelve 'Hombre' y con cualquier otra cadena, devuelve None.
    
    @param cadena: Cadena de caracteres con el valor verdadero
    @type cadena: str
    @return: 'Success', 'Failure' o None, dependiendo de si la cadena que se pasa como parámetro 
    tiene el literal 'verdadero', el literal 'falso' o cualquier otra cadena
    @rtype: str 
    '''
    res = None
    cadena = cadena.upper()
    if cadena == 'VERDADERO':
        res ='Success'
    elif cadena == 'FALSO':
        res='Failure'
    return res
