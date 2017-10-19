
# -*- coding: utf-8 -*-

from auxiliares import one_sha256


def gerar_hash_transacao(self):
    return one_sha256(self)

def nova_transacao(pagador, beneficiario, vencimento_bol, data_pagmt_bol):
    tx = {
        'pagador': str(pagador),
        'beneficiario': str(beneficiario),
        'vencimento_bol': vencimento_bol,
        'data_pagmt_bol': data_pagmt_bol,
        'valor_bol': None,
        'hash_tx': None
    }
    
    v_bol = tx['valor_bol']
    if v_bol == None:
        if (tx['vencimento_bol'] - tx['data_pagmt_bol']) >= 0:
            v_bol = 100
        else:
            v_bol = 110
    tx['valor_bol'] = v_bol
    
    h_tx = tx['hash_tx']
    if h_tx == None:
        dados_tx = tx['pagador'] + tx['beneficiario'] + str(tx['vencimento_bol']) + str(tx['data_pagmt_bol']) + str(tx['valor_bol'])
        h_tx = gerar_hash_transacao(dados_tx)
    tx['hash_tx'] = h_tx
    d = {'valor_bol': v_bol, 'hash_tx': h_tx}
    tx.update(d)
    return tx

#class Transacao():
#    def __init__(self):
#        pass
        
