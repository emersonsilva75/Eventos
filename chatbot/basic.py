# encoding: utf-8
import math
import dateutil.parser
import datetime
import time
import os
import urllib2
#import logging

# Set inicial

#logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)


# Funcoes para construir respostas minimas para as acoes do dialogo

# Obtem o slot do intent
def get_slots(intent_request):
    return intent_request['currentIntent']['slots']

def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message
        }
    }

# Nao espera retorno do client, encerra o dialogo
def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }
    return response

# Delega o dialogo para novos slots
def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }

# Funcoes de apoio 

# Adaptacao tecnica para validar negacoes em portugues
def is_negado(valor_analise):
    negativos = ['no','nao','nunca','never','nada']
    curinga = 'não'.decode("UTF8")
    status = False
    if valor_analise is None:
        return 'Sem valor negado definido'
    else :        
        if valor_analise in negativos or valor_analise == curinga:
            status = True
        return status
    
# Adaptacao tecnica para validar valores positivos
def is_positivo(valor_analise):
    positivos = ['sim','ok','beleza','belezera','podepa','legal','valeu','vlw','pdp','claro','com certeza','certeza','quero','pode']
    status = False
    if valor_analise is None:
        return 'Sem valor positivo definido'
    else :        
        if valor_analise in positivos :
            status = True
        return status

def parse_int(n):
    try:
        return int(n)
    except ValueError:
        return float('nan')

def build_validation_result(is_valid, violated_slot, message_content):
    if message_content is None:
        return {
            "isValid": is_valid,
            "violatedSlot": violated_slot,
        }
    return {
        'isValid': is_valid,
        'violatedSlot': violated_slot,
        'message': {'contentType': 'PlainText', 'content': message_content}
    }

def isvalid_date(date):
    try:
        dateutil.parser.parse(date)
        return True
    except ValueError:
        return False

def validate_livros(livro):
    print livro
    #if is_negado(livro) and livro is not None and not is_positivo(livro):
    if is_positivo(livro):
        return build_validation_result(False, 'slotOne', 'Teste' )
    return build_validation_result(True, None, None) 

def buscar_livros(intent_request):
    source = intent_request['invocationSource']
    entrada = get_slots(intent_request)["slotOne"]
    validation_result = validate_livros(entrada)
    if source == 'DialogCodeHook':
        return validador(intent_request,validation_result,source)

def validador(intent_request,validation_result,source):
    if source == 'DialogCodeHook':
        slots = get_slots(intent_request)
        if not validation_result['isValid']:
            slots[validation_result['violatedSlot']] = None
            return elicit_slot(intent_request['sessionAttributes'],
                               intent_request['currentIntent']['name'],
                               slots,
                               validation_result['violatedSlot'],
                               validation_result['message'])
        elif validation_result['isValid'] and validation_result['violatedSlot'] is not None:
            mensagem = validation_result['message']['content']
            return close(intent_request['sessionAttributes'],'Fulfilled',{'contentType': 'PlainText','content': '{} '.decode("ISO-8859-1").format(mensagem)})
        output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
        return delegate(output_session_attributes, get_slots(intent_request))
    return close(intent_request['sessionAttributes'],'Fulfilled',{'contentType': 'PlainText','content': 'Tudo bem, qualquer coisa é só me chamar ! '.decode("ISO-8859-1")})

# Intent

def dispatch(intent_request):
    #logger.debug('dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))
    intent_name = intent_request['currentIntent']['name']
    # Dispatch to your bot's intent handlers
    if intent_name == 'todos_livros':
        return buscar_livros(intent_request)
    raise Exception('Intent with name ' + intent_name + ' not supported')

# Principal funcao

def lambda_handler(event, context):    
    os.environ['TZ'] = 'America/New_York'
    os.environ['LANG'] = 'pt_BR.UTF-8'
    time.tzset()
    #logger.debug('event.bot.name={}'.format(event['bot']['name']))

    return dispatch(event)