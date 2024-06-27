import logging
import ply.yacc as yacc

from lex import tokens
from lex import lexed_code

# Início da gramática
def p_start(p):
    '''start : expression end_of_line
             | empty'''
    p[0] = p[1]

def p_end_of_line(p):
    '''end_of_line : eol start'''
    pass

# Expressões possíveis
def p_expression(p):
    '''expression : impressao
                  | atribuicao
                  | exec'''
    p[0] = p[1]

# Regra de produção vazia
def p_empty(p):
    'empty :'
    pass

def p_impressao(p):
    '''impressao : imprimir abre_parentese num fecha_parentese 
                | imprimir abre_parentese id fecha_parentese'''
    p[0] = (p[1], p[3])

def p_executar(p):
    'executar : exec abre_parentese id virgula vetor fecha_parentese'
    p[0] = (p[1], p[3], p[5])

def p_vetor(p):
    'vetor : abre_colchete items fecha_colchete'
    p[0] = (p[2])

def p_items(p):
    '''items : item virgula items 
            | item'''
    p[0] = (p[1])

def p_item(p):
    '''item : bin
            | id
            | entradas_saida
            '''
    p[0] = (p[1])

def p_atribuicao(p):
    'atribuicao : tipo id atrib atribuiveis'
    p[0] = (p[1], p[2])

def p_atribuiveis(p):
    '''atribuiveis : num
                    | executar
                    | porta_logica'''
    p[0] = (p[1])

def p_porta_logica(p):
    'porta_logica : abre_chave numero_de_entradas virgula tabela_verdade virgula fecha_chave'
    p[0] = (p[3])

def p_numero_de_entradas(p):
    'numero_de_entradas : ne chave_valor num'
    p[0] = p[1]

def p_tabela_verdade(p):
    'tabela_verdade : tv chave_valor abre_chave items fecha_chave'
    p[0] = p[3]

def p_entradas_saida(p):
    '''entradas_saida : vetor chave_valor bin'''
    p[0] = (p[1])

def p_tipo(p):
    '''tipo : sinal
            | porta_log'''
    p[0] = p[1]

def p_error(p):
    print(f"Erro de sintaxe em '{p}'")

# Build the parser
log = logging.getLogger()
parser = yacc.yacc(debug=True, debuglog=log)

print('\n----------ANÁLISE SINTÁTICA----------')

print(lexed_code)
result = parser.parse(lexed_code)
print(result)