import ply.lex as lex

tokens = ['num', 'id', 'INT', 'TRUE', 'FALSE', 'END', 'IF', 'ELSE', 'EQUALS', 'NOTEQUALS', 'JUMP']
literals = ['(', ')', '+', '-', '*', '/', '!', '=', '?', '<', '>', '{', '}']

t_num = r'\d+'

t_id = r'[a-z]+'

t_INT = r'INT' 

t_END = r'\.'

t_TRUE = r'TRUE'

t_FALSE = r'FALSE'

t_EQUALS = r'=='

t_NOTEQUALS = r'!='

t_IF = r'IF'

t_ignore = " \t\n"

#ações semanticas

def t_error(t):
	print("Carater ilegal: ", t.value[0])
	t.lexer.skip(1)

#build the lexer
lexer = lex.lex()	