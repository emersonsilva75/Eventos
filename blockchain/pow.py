# -*- coding: utf-8 -*-

""" Este módulo existe com propósito didático. Na prática há mecanismos
    de consenso melhores que o PoW. O Delegated Proof of Stake é um exemplo.
"""

import random
import logging
import time
from auxiliares import double_sha256


DIFICULDADE = 4
"""Numero de ZEROS consecutivos que devem constar no hash gerado."""

NONCE = ""
""" No blockchain do Bitcoin todos os blocos possuem um Nonce. Esse
    numero é usado pelos mineradores.
"""

INIT = "k5#@09Dm%l0wc3R"

log = logging.getLogger(__name__)


def gerar_nonce(init, length=None):
    """ Gera uma 'string' aleatória a partir dos dados contidos em INIT.
    Essa 'string' é usada como Nonce. O tamanho da 'string' é igual ao do
    INIT.    
    
    :retorna: 'strings' permutadas
    """
    while 1:
        yield ''.join(random.choice(init) for _ in range(len(init)))


def calcular_nonce(valor, dificuldade, init=INIT):
    """ Retorna um Nonce aleatório que atende os requisitos, isto é,
    que o Hash gerado do valor concatenado e o Nonce possuem a quantidade
    especificada de numero de zeros.
    """    

    ciclo = 1
    for nonce in gerar_nonce(init):
        hash_valor = gerar_hash(valor, nonce)
        if verificar_hash(hash_valor, dificuldade):
            log.info("Nonce encontrado com ciclo {}".format(ciclo))
            return nonce
        ciclo += 1


def gerar_hash(valor, nonce):
    """ Gera o valor do Hash do valor concatenado e o Nonce.
    :value: Static string, which is modified over and over again with the nonce.
    :nonce: Random data added to the value.
    :returns: A hash build from the given value and nonce
    """
    return double_sha256(valor + nonce)


def verificar_hash(hash_valor, dificuldade):
    """ Retorna True se o hash obtido possui o numero de zeros desejados na
    representação binaria do valor do hash. O número de zeros desejados é 
    determinado pelo nivel de dificuldade.
    :hash_valor:  hash gerado
    :dificuldade: Numero de zeros a esquerda que devem ser gerados.
    :retorna: True or False
    """
    padrao = "0" * dificuldade
    bin_valor = bin(int(hash_valor, 16))[2::]
    if bin_valor.endswith(padrao):
        print 'esse e o ' + bin_valor + '  gerado relativo ao padrao ' + padrao
        return True
    return False


if __name__ == "__main__":
    for dificuldade in range(DIFICULDADE, 10):
        a = time.time()
        nonce = calcular_nonce("Mais Proposito Menos Banco!", dificuldade)
        b = time.time()
        print("Encontrado depois de {} com dificuldade {}".format((b - a), dificuldade))

