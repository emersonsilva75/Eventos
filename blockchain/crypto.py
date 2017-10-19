# -*- coding: utf-8 -*-


""" https://github.com/vbuterin/pybitcointools """
import pybitcointools

from bitcoin import *

""" Gerar chave privada """
privK = random_key()
print "Essa e a chave privada: " + privK

""" A partir da chave privada gerar a chave publica """
pubK = privtopub(privK) 
print "Essa e a chave publica: " + pubK

""" Gerar endereco publico"""
addrPub = pubtoaddr(pubK)
print "Essa e o endereco publico: " + addrPub

""" Gerar Brain Wallet """
priv = sha256('Mais proposito menos banco!')
print 'esta e chave privada: ' + priv

pub = privtopub(priv)
print 'esta e chave publica: ' + pub

addr = pubtoaddr(pub)
print 'este e endereco: ' + addr

msg = 'ola'
signEDSA = ecdsa_sign(msg, priv)
print 'msg assinada com chave publica :' + signEDSA

""" ecdsa_verify : (message, sig, pubkey)"""
ver_msg = ecdsa_verify(msg, signEDSA, pub)
print ver_msg

""" Exemplo de multiplas assinaturas digitais, 3 assinaturas usando chaves publicas.
1. Gerar 3 chaves privadas, privK1, privK2, privK3.
2. Gerar 3 chaves publicas a partir das chaves privadas. pubK1, pubK2, pubK3
3. Criar a regra (script) para que a assinatura ocorra, isto e, das 3 assinaturas quantas sao necessarias.
4. Gerar a versao hash do multi.
"""

""" Gerar chave privada privK1 """
privK1 = random_key()
print "Essa e a chave privada privK1: " + privK1

""" A partir da chave privada gerar a chave publica pubK1 """
pubK1 = privtopub(privK1) 
print "Essa e a chave publica pubK1: " + pubK1

""" Gerar chave privada privK2 """
privK2 = random_key()
print "Essa e a chave privada privK2: " + privK2

""" A partir da chave privada gerar a chave publica pubK2 """
pubK2 = privtopub(privK2) 
print "Essa e a chave publica pubK2: " + pubK2

""" Gerar chave privada privK3 """
privK3 = random_key()
print "Essa e a chave privada privK1: " + privK3

""" A partir da chave privada gerar a chave publica pubK3 """
pubK3 = privtopub(privK3) 
print "Essa e a chave publica pubK3: " + pubK3

multisign = mk_multisig_script(pubK1, pubK2, pubK3, 2, 3)
print "Essa e multisign: " + multisign
multi_addr = scriptaddr(multisign)
print "Essa e o hash de multi_addr: " + multi_addr









