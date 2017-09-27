# -*- coding: utf-8 -*-

notas100 = 0
notas50= 0
notas20 = 0
notas10 = 0

valor = 80

notas100 = int(valor / 100)
if notas100 > 0:
    valor = valor % 100
    
notas50 = int(valor / 50)
if notas50 > 0:
    valor = valor % 50
    
notas20 = int(valor / 20)
if notas20 > 0:
    valor = valor % 20

notas10 = int(valor / 10)
if notas10 > 0:
    valor = valor % 10
    
print 'notas 100 ' + str(notas100)
print 'notas 50 ' + str(notas50)
print 'notas 20 ' + str(notas20)
print 'notas 10 ' + str(notas10)
print 'valor ' + str(valor)

