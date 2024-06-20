import ply.lex as lex

# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    "porta_log",
    "id",
    "atrib",
    "abre_chave",
    "chave_valor",
    "num",
    "virgula",
    "ne",
    "tv",
    "abre_colchete",
    "bin",
    "fecha_colchete",
    "fecha_chave",
    "sinal",
    "exec",
    "abre_parentese",
    "fecha_parentese",
    "imprimir"
)

# Regular expression rules for simple tokens

t_porta_log       = r'portalogica'
t_id              = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_atrib           = r'='
t_abre_chave      = r'{'
t_chave_valor     = r':'
t_num             = r'[1-9][0-9]*'
t_virgula         = r','
t_ne              = r'numero_de_entradas'
t_tv              = r'tabela_verdade'
t_abre_colchete   = r'\['
t_fecha_colchete  = r'\]'
t_fecha_chave     = r'}'
t_sinal           = r'sinal'
t_exec            = r'exec'
t_abre_parentese  = r'\('
t_fecha_parentese = r'\)'
t_imprimir        = r'imprimir'

# Regra para novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# caracteres ignorados: espaços e tabulações
t_ignore  = ' \t'

# regra para tratar erros
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# contruir o lexer
lexer = lex.lex()

# entrada de teste
data = '''
portalogica porta_and = {
	numero_de_entradas: 2,
	tabela_verdade: {
	    [0, 0] : 0,
        [0, 1] : 0,
        [1, 0] : 0,
        [1, 1] : 1
    }
}

portalogica porta_not = {
	numero_de_entradas: 10,
	tabela_verdade: {
	    [0] : 1,
        [1] : 0,
    }
}

sinal variavel1 = exec(porta_and, [1, 1])
sinal variavel2 = exec(porta_not, [variavel1])
imprimir(variavel2)

'''

# input de teste para o lexer
lexer.input(data)

# tokenização
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)