import ply.lex as lex

tokens = ['num', 'id', 'INT', 'TRUE', 'FALSE', 'IF', 'FOR', 'ELSE', 'EQUALS', 'NOTEQUALS', 'DO', 'E', 'OU', 'NOME', 'TEXT', 'PRINT', 'SCAN', 'STRING', 'NEWLINE']
literals = ['(', ')', '+', '-', '*', '/', '!', '=', '?', '<', '>', ',', '{', '}', '"']

t_num = r'\d+'

t_id = r'[a-z]+'

t_INT = r'INT' 

t_TRUE = r'TRUE'

t_FALSE = r'FALSE'

t_EQUALS = r'=='

t_NOTEQUALS = r'!='

t_IF = r'IF'

t_ELSE = r'ELSE'

t_FOR = r'FOR'

t_DO = r'DO'

t_E = r'E'

t_OU = r'OU'

t_NOME = r'^((def_)[a-zA-Z]+)'

#t_TEXT = r'^".+"$'
t_TEXT = r'"([^"]+)"'

t_PRINT = r'PRINT'

t_SCAN = r'SCAN'

t_STRING = r'STRING'

t_NEWLINE = r'\n'

t_ignore = " \t\n"

#ações semanticas

def t_error(t):
	print("Carater ilegal: ", t.value[0])
	t.lexer.skip(1)

#build the lexer
lexer = lex.lex()	