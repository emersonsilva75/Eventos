#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Validação numeros sem Regex

import pyperclip,re 

foneRegex = re.compile(r'''(
                       (\(\d{2}\))? # DDD
                       (\d)?        # Digito opcional
                       (\d{4})      # Numero principais
                       (\s|-|.)?     # Separador
                       (\d{4})      # Numeros finais
                       )''',re.VERBOSE)
# Obtendo dados do Clipboard
texto = str(pyperclip.paste())

blocos = []

for bloco in foneRegex.findall(texto):
                       nroTelefone = bloco[0]
                       blocos.append(nroTelefone)

if len(blocos) > 0:
                       pyperclip.copy('\n'.join(blocos))
                       print('Enviado para o clipboard : ')
                       print('\n'.join(blocos))
else:
                       print('Nenhum telefone encontrado !')
                       
