import logging
import ply.yacc as yacc

from lex import tokens

# Início da gramática
def p_start(p):
    '''start : expression
             | empty'''
    p[0] = p[1]

# Expressões possíveis
def p_expression(p):
    '''expression : impressao
                  | atribuicao'''
    p[0] = p[1]

# Regra de produção vazia
def p_empty(p):
    'empty :'
    pass

def p_impressao(p):
    '''impressao : imprimir abre_parentese num fecha_parentese 
                | imprimir abre_parentese id fecha_parentese'''
    p[0] = (p[1], p[3])

def p_atribuicao(p):
    'atribuicao : sinal id atrib num'
    p[0] = (p[2], p[4])

def p_error(p):
    print(f"Erro de sintaxe em '{p.value}'")

# Build the parser
parser = yacc.yacc()
log = logging.getLogger()

print('\n----------ANÁLISE SINTÁTICA----------')
s = '''
Sinal sinal = 1
Imprimir(sinal)
'''


s = s.split('\n')

for line in s:
  if len(line) == 0:
      continue
  result = parser.parse(line, debug=log)
  print(result)