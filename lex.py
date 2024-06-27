import ply.lex as lex

import ply.lex as lex

# List of token names.   This is always required
tokens = (
    "porta_log",
    "sinal",
    "bin",
    "id",
    "atrib",
    "abre_chave",
    "chave_valor",
    "num",
    "virgula",
    "ne",
    "tv",
    "abre_colchete",
    "fecha_colchete",
    "fecha_chave",
    "exec",
    "abre_parentese",
    "fecha_parentese",
    "imprimir",
    "eol"
)

# Regular expression rules for simple tokens

t_porta_log       = r'Portalogica'
t_sinal           = r'Sinal'
t_bin             = r'[0 | 1]+b'
t_id              = r'(?!\d+)[a-z0-9_]+'
t_atrib           = r'='
t_abre_chave      = r'{'
t_chave_valor     = r':'
t_num             = r'\d+(?!\w+)'
t_virgula         = r','
t_ne              = r'Numero_de_entradas'
t_tv              = r'Tabela_verdade'
t_abre_colchete   = r'\['
t_fecha_colchete  = r'\]'
t_fecha_chave     = r'}'
t_exec            = r'Exec'
t_abre_parentese  = r'\('
t_fecha_parentese = r'\)'
t_imprimir        = r'Imprimir'
t_eol             = r';'

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
Portalogica porta_and = {
	Numero_de_entradas: 2,
	Tabela_verdade: {
	    [0b, 0b] : 0b,
        [0b, 1b] : 0b,
        [1b, 0b] : 0b,
        [1b, 1b] : 1b
    },
};

Portalogica porta_not = {
	Numero_de_entradas: 10,
	Tabela_verdade: {
	    [0b] : 1b,
        [1b] : 0b
    },
};

Sinal variavel1 = Exec(porta_and, [1b, 1b]);
Sinal variavel2 = Exec(porta_not, [variavel1]);
Imprimir(variavel2);
'''

# input de teste para o lexer
lexer.input(data)

lexed_code = ""

# tokenização
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
    lexed_code += tok.value + " "