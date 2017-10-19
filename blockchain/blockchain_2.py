# -*- coding: utf-8 -*-
from datetime import datetime
from auxiliares import utcTimestamp, double_sha256
from transacao import nova_transacao

""" Diferença deste file com blockchain.py é que este tem mais info na função def novo_bloco """

__versao_bloco__ = "1.0"
"""Versão do bloco."""

__tamanho_max_bloco__ = 256
""" Limitação referente ao comprimento dos dados len(data)  """

def gerar_hash_bloco(index, timestamp, prev_hash, dados):
    
    """Aplica a função double_sha256 cujo resultado será usado como o
    endereço do novo bloco que foi inserido no Blockchain.    
    :index     : indice do bloco (int)
    :timestamp : timestamp do bloco (str)
    :prev_hash : é o hash (endereço) do bloco anterior (str)
    :dados     : conteúdo existente no bloco
    A função retorna o hash SHA256    
    """    
    fonte_hash = str(index) + str(timestamp) + str(prev_hash) + str(dados)
    return double_sha256(fonte_hash)

def novo_bloco(blockchain, dados):
    if not isinstance(dados, list):
        raise ValueError("Dados Devem Ser LISTAS")
    if len(dados) > __tamanho_max_bloco__:
        raise ValueError("Os dados não devem ser maiores que {}".format(__tamanho_max_bloco__))
    if len(dados) == 0:
        raise ValueError("A lista dos dados não pode ser Vazia")
    ultimo_blockchain = blockchain.end
    block = {
        'index': ultimo_blockchain['index'] + 1,
        'timestamp': utcTimestamp(datetime.utcnow()),
        #'transactions': current_transactions,
        'dados': dados,
        'prev_hash': ultimo_blockchain['hash_block'],
        'hash_block': None ##$gerar_hash_bloco('index', 'timestamp', 'dados', 'previous_hash')
    }
    if block['hash_block'] == None:
        hb = gerar_hash_bloco(block['index'], block['timestamp'], block['dados'], block['prev_hash'])
    d = {'hash_block': hb}
    block.update(d)
    return block


def validar_bloco(blockchain, bloco):
    
    """ Checar se um bloco é um bloco válido para ser incluido no Blockchain """
    
    ultimo_bloco = blockchain.end
    
    
    """ Checar se o bloco está corretamente conectado ao bloco anterior.
        O previous_hash do bloco anterior DEVE ser IGUAL ao do bloco atual.    
    """
    if ultimo_bloco['hash_block'] != bloco['prev_hash']:
        raise ValueError("Os hashes sao diferentes.")    
        
        
    """ Checar o index do bloco anterior com o bloco atual.
        A diferença do bloco anterior com o bloco atual DEVE ser IGUAL a -1.    
    """    
    if ultimo_bloco['index'] - bloco['index'] != -1:
        raise ValueError("O index deste bloco nao esta correto em relacao ao bloco anterior")
    
    return True 

class Blockchain(object):
    def __init__(self):
        self.blockchain = []
        self.gerar_bloco_genesis(dados = ['primeiro bloco'], timestamp=None)
 
    @property    
    def end(self):
        return self.blockchain[-1]
        
    def gerar_bloco_genesis(self, dados, timestamp = None, blockchain=None, prev_hash=None, hash_block=None):
        bloco_genesis = {
            'index': 0,
            'timestamp': utcTimestamp(datetime(2017, 10, 19, 0, 0, 0)),
            'dados': ['primeiro bloco'],
            'prev_hash': 'Nenhum',
            'hash_block': None
        }
        
        hB = bloco_genesis['hash_block']
        if hB == None:
            nhB = gerar_hash_bloco(bloco_genesis['index'], bloco_genesis['timestamp'], bloco_genesis['dados'], bloco_genesis['prev_hash'])
        d_nhB = {'hash_block': nhB}
        bloco_genesis.update(d_nhB)
        
        
        """ Reset the current list of transactions """
        self.current_transactions = []
        return self.blockchain.append(bloco_genesis)
        
    @property    
    def lenght(self):
        return len(self.blockchain)
    
           
    def adicionar_bloco(self, bloco):
        validar_bloco(self, bloco)
        self.blockchain.append(bloco)
    

    
    

    
    
    
    
    
    
    
    
    
    