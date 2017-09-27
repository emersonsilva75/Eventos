#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Validação numeros sem Regex - GoHorse Way

def isPhoneNumber(text):
    if len(text) != 14:
        return False
    for i in range(0,3):
        if text[0] != '(':
            return False
        if text[3] != ')':
            return False    
        if not text[1:2].isdecimal():
            return False            
        for i in range(4,9):
            if not text[4:8].isdecimal():
                return False
        if text[9] != '-':
            return False
        for i in range(10,13):
            if not text[i].isdecimal():
                return False
        return True
        
print(isPhoneNumber('(19)8147-7222'))
print(isPhoneNumber('Teste'))

# Validação numeros com Regex

import re

phoneNumRegex = re.compile(r'\(\d{2}\)\d{5}\-\d{4}')

no = phoneNumRegex.search('Meu numero é (19)98147-7222 e (19)98160-4774')

print('Numero encontrado com search : ' + no.group())

no2 = phoneNumRegex.findall('Meu numero é (19)98147-7222 e (19)98160-4774')          

print('Numero encontrado com findall : ' + str(no2))
            
# validando Pipe e grupos

heroRegex = re.compile(r'Bat(man|movel|copter|bat)')

heroi = heroRegex.search('Batmovel perdeu uma roda')

print(heroi.group(0))
        
    
