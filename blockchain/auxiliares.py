
# -*- coding: utf-8 -*-

"""
Esse arquivo contém funções que serão usadas no arquivo
cursoSuperlogica.py

"""
import calendar

import hashlib as hash_
## double_sha256 

def utcTimestamp(dt):
    """Will return a UTC timestamp of the given datetime"""
    if dt.tzinfo is not None:
        raise ValueError("Datetime must be naiv and must not contain any tzinfo")
    return calendar.timegm(dt.utctimetuple())

def double_sha256(valor):
    """ Retorna o dobro da função hash sha256 de um valor
        O 'valor' deve ser do tipo string (str)
    """
    
    """ Assegurar que o valor é str """
    if valor is None:
        valor = ""
    elif not isinstance(valor, str):
        valor = str(valor)
    
    h1 = hash_.sha256()
    h2 = hash_.sha256()
    h1.update(valor.encode("utf-8"))
    h2.update(h1.hexdigest().encode("utf-8"))
    return h2.hexdigest()

def one_sha256(valor):
    """ Retorna função hash sha256 de um valor
        O 'valor' deve ser do tipo string (str)
    """
    
    """ Assegurar que o valor é str """
    if valor is None:
        valor = ""
    elif not isinstance(valor, str):
        valor = str(valor)
    
    h1 = hash_.sha256()
    h1.update(valor.encode("utf-8"))
    return h1.hexdigest()