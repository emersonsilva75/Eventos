README.md

# Evento de Blockchain

Exemplos do curso de Blockchain


## Dependências

### Opcionais 

Instalação do virtualenv e ipython

```bash
sudo pip install virtualenv
virtualenv env
source env/bin/activate // env/bin/activate.fish 

pip install ipython
```

## Como rodar o Blockchain

### Hands on

* Inicie o arquivo em memória: 

```python
python 
>>> from blockchain_2 import * 
```

* Criando um novo Blockchain

```python
SuperlogicaBlockchain = Blockchain();
```

* Listando os blocos para exibir o bloco Genesis

```python
SuperlogicaBlockchain.blockchain
```

#### Output
```python
[{'dados': ['primeiro bloco'],
  'hash_block': 'cd712305acdbd6fad16e9695e88aefaf03e1a95a012b5e97fb931f1c2b2a3ef8',
  'index': 0,
  'prev_hash': 'Nenhum',
  'timestamp': 1508371200}]
```

* Criando transações

```python
tx1 = nova_transacao('pagamento1', 'exemplo', 220, 200)
tx2 = nova_transacao('pagamento2', 'exemplo', 200, 200)
```

* Criando novos blocos para as transações

```python
bloco = novo_bloco(SuperlogicaBlockchain, [tx1, tx2])
```

* Validando os blocos

```python
validar_bloco(SuperlogicaBlockchain, bloco)
```

```python
true
```

* Adicionando blocos ao Blockchain

```python
SuperlogicaBlockchain.adicionar_bloco(bloco)
```

* Exibindo os novos blocos

```python
SuperlogicaBlockchain.blockchain
```

#### Output

```json
[{'dados': ['primeiro bloco'],
  'hash_block': 'cd712305acdbd6fad16e9695e88aefaf03e1a95a012b5e97fb931f1c2b2a3ef8',
  'index': 0,
  'prev_hash': 'Nenhum',
  'timestamp': 1508371200},
 {'dados': [{'beneficiario': 'exemplo',
    'data_pagmt_bol': 200,
    'hash_tx': '208cecd13503dc0e85cd19de9864684c5b6e3911c81d17fcddc732c4b405f15c',
    'pagador': 'pagamento1',
    'valor_bol': 100,
    'vencimento_bol': 220},
   {'beneficiario': 'exemplo',
    'data_pagmt_bol': 200,
    'hash_tx': 'd756ca5191cb0d212b2ff559a97356099e0d82a1efee5b67c7aba53abb933ee8',
    'pagador': 'pagamento2',
    'valor_bol': 100,
    'vencimento_bol': 200}],
  'hash_block': 'a9d42ad9ec9c18cdefa6448f8abb86985f8376472b67eca9fd7c14b2124eb8e3',
  'index': 1,
  'prev_hash': 'cd712305acdbd6fad16e9695e88aefaf03e1a95a012b5e97fb931f1c2b2a3ef8',
  'timestamp': 1508429240}]
```

* Verificando um bloco específico 

```python
SuperlogicaBlockchain.blockchain[1]
```

#### Output

```README.md


## Dependências

### Opcionais 

```bash
sudo pip install virtualenv
virtualenv env
source env/bin/activate // env/bin/activate.fish 
```

## Como rodar o Blockchain

### Hands on

* Inicie o arquivo em memória: 

```python
python 
>>> from blockchain_2 import * 
```

* Criando um novo Blockchain

```python
SuperlogicaBlockchain = Blockchain();
```

* Listando os blocos para exibir o bloco Genesis

```python
SuperlogicaBlockchain.blockchain
```

#### Output
```json
[{'dados': ['primeiro bloco'],
  'hash_block': 'cd712305acdbd6fad16e9695e88aefaf03e1a95a012b5e97fb931f1c2b2a3ef8',
  'index': 0,
  'prev_hash': 'Nenhum',
  'timestamp': 1508371200}]
```

* Criando transações

```python
tx1 = nova_transacao('pagamento1', 'exemplo', 220, 200)
tx2 = nova_transacao('pagamento2', 'exemplo', 200, 200)
```

* Criando novos blocos para as transações

```python
bloco = novo_bloco(SuperlogicaBlockchain, [tx1, tx2])
```

* Validando os blocos

```python
validar_bloco(SuperlogicaBlockchain, bloco)
```

```json
true
```

* Adicionando blocos ao Blockchain

```python
SuperlogicaBlockchain.adicionar_bloco(bloco)
```

* Exibindo os novos blocos

```python
SuperlogicaBlockchain.blockchain
```

#### Output

```python
[{'dados': ['primeiro bloco'],
  'hash_block': 'cd712305acdbd6fad16e9695e88aefaf03e1a95a012b5e97fb931f1c2b2a3ef8',
  'index': 0,
  'prev_hash': 'Nenhum',
  'timestamp': 1508371200},
 {'dados': [{'beneficiario': 'exemplo',
    'data_pagmt_bol': 200,
    'hash_tx': '208cecd13503dc0e85cd19de9864684c5b6e3911c81d17fcddc732c4b405f15c',
    'pagador': 'pagamento1',
    'valor_bol': 100,
    'vencimento_bol': 220},
   {'beneficiario': 'exemplo',
    'data_pagmt_bol': 200,
    'hash_tx': 'd756ca5191cb0d212b2ff559a97356099e0d82a1efee5b67c7aba53abb933ee8',
    'pagador': 'pagamento2',
    'valor_bol': 100,
    'vencimento_bol': 200}],
  'hash_block': 'a9d42ad9ec9c18cdefa6448f8abb86985f8376472b67eca9fd7c14b2124eb8e3',
  'index': 1,
  'prev_hash': 'cd712305acdbd6fad16e9695e88aefaf03e1a95a012b5e97fb931f1c2b2a3ef8',
  'timestamp': 1508429240}]
```

* Verificando um bloco específico 

```python
SuperlogicaBlockchain.blockchain[1]
```

#### Output

```python
{'dados': [{'beneficiario': 'exemplo',
   'data_pagmt_bol': 200,
   'hash_tx': '208cecd13503dc0e85cd19de9864684c5b6e3911c81d17fcddc732c4b405f15c',
   'pagador': 'pagamento1',
   'valor_bol': 100,
   'vencimento_bol': 220},
  {'beneficiario': 'exemplo',
   'data_pagmt_bol': 200,
   'hash_tx': 'd756ca5191cb0d212b2ff559a97356099e0d82a1efee5b67c7aba53abb933ee8',
   'pagador': 'pagamento2',
   'valor_bol': 100,
   'vencimento_bol': 200}],
 'hash_block': 'a9d42ad9ec9c18cdefa6448f8abb86985f8376472b67eca9fd7c14b2124eb8e3',
 'index': 1,
 'prev_hash': 'cd712305acdbd6fad16e9695e88aefaf03e1a95a012b5e97fb931f1c2b2a3ef8',
 'timestamp': 1508429240}
```

{'dados': [{'beneficiario': 'exemplo',
   'data_pagmt_bol': 200,
   'hash_tx': '208cecd13503dc0e85cd19de9864684c5b6e3911c81d17fcddc732c4b405f15c',
   'pagador': 'pagamento1',
   'valor_bol': 100,
   'vencimento_bol': 220},
  {'beneficiario': 'exemplo',
   'data_pagmt_bol': 200,
   'hash_tx': 'd756ca5191cb0d212b2ff559a97356099e0d82a1efee5b67c7aba53abb933ee8',
   'pagador': 'pagamento2',
   'valor_bol': 100,
   'vencimento_bol': 200}],
 'hash_block': 'a9d42ad9ec9c18cdefa6448f8abb86985f8376472b67eca9fd7c14b2124eb8e3',
 'index': 1,
 'prev_hash': 'cd712305acdbd6fad16e9695e88aefaf03e1a95a012b5e97fb931f1c2b2a3ef8',
 'timestamp': 1508429240}
```
