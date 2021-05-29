import ply.yacc as yacc
from tp2_lex import tokens
from tp2_lex import literals
import sys

#Data Structure
#key : string (nome da variavel)
#valor : endereço da stack
atribs = {}

#Contador de atribuições
atrib_counter = 0

#Output file with VM instructions
out = open("output.vm","w+")

out.write("START\n")

#Get the token map from the lexer. this is required

#Production rules
#Comandos
def p_Comandos_comando(p):
    "Comandos : Comando"
    out.write(p[1]+"\n")

def p_Comandos_comandos_comando(p):
    "Comandos : Comandos Comando"
    out.write(p[2]+"\n")

def p_Comando_ExprR(p):
    "Comando : ExprR"
    p[0] = p[1]

def p_Comando_Declaracao(p):
    "Comando : Declaracao"
    p[0] = p[1]    

def p_Comando_Atribuicao(p):
    "Comando : Atribuicao"
    p[0] = p[1] 

def p_Comando_Atribuicao_NEWLINE(p):
    "Comando : Atribuicao NEWLINE"
    p[0] = p[1]     

def p_Comando_IFELSE(p):
    "Comando : IFELSE"
    p[0] = p[1] 

def p_Comando_ONLYIF(p):
    "Comando : ONLYIF"
    p[0] = p[1]     

def p_Comando_FORDO(p):
    "Comando : FORDO"
    p[0] = p[1]  

def p_Comando_FUNC(p):
    "Comando : FUNC"
    p[0] = p[1] 

def p_Comando_PRINTER(p):
    "Comando : PRINTER"
    p[0] = p[1] 

def p_Comando_SCANNER(p):
    "Comando : SCANNER"
    p[0] = p[1]                   

##############################################################################

def p_Factor_num(p):
    "Factor : num"
    p[0] = "PUSHI " + p[1] + "\n"

def p_Factor_num_negativo(p):
    "Factor : '-' num"
    p[0] = "PUSHI " + str((int(p[2])*(-1))) + "\n" 

def p_Factor_id(p):
    "Factor : id"
    p[0] = "PUSHG " + str(atribs[p[1]]) + "\n"

def p_Factor_TRUE(p):
    "Factor : TRUE"
    p[0] = "PUSHI 1\n"

def p_Factor_FALSE(p):
    "Factor : FALSE"
    p[0] = "PUSHI 0\n"  

def p_Factor_ExprR(p):
    "Factor : '(' ExprR ')'"
    p[0] = p[2]      

def p_ExprR_Expr_menor(p):
    "ExprR : Expr '<' Expr"
    p[0] = p[1] + p[3] + "INF\n"

def p_ExprR_Expr_maior(p):
    "ExprR : Expr '>' Expr"
    p[0] = p[1] + p[3] + "SUP\n"

def p_ExprR_Expr_menor_igual(p):
    "ExprR : Expr '<' '=' Expr"
    p[0] = p[1] + p[4] + "INFEQ\n"

def p_ExprR_Expr_maior_igual(p):
    "ExprR : Expr '>' '=' Expr"
    p[0] = p[1] + p[4] + "SUPEQ\n"    

def p_ExprR_Expr_igual(p):
    "ExprR : Expr EQUALS Expr"
    p[0] = p[1] + p[3] + "EQUAL\n"

def p_ExprR_Expr_diferente(p):
    "ExprR : Expr NOTEQUALS Expr"
    p[0] = p[1] + p[3] + "EQUAL NOT\n"

# 1 E 1 = 1
# 1 E 0 = 0
# 0 E 1 = 0
# 0 E 0 = 0
def p_Termo_Termo_E_Termo(p):
    "Termo : Termo E Factor"
    p[0] = p[1] + p[3] + "MUL\n"

# 1 OU 1 = 1
# 1 OU 0 = 1
# 0 OU 1 = 1
# 0 OU 0 = 0
def p_ExprR_Expr_OU_Expr(p):
    "Expr : Expr OU Termo"
    p[0] = p[1] + "\nNOT\n" + p[3] + "\nNOT\nMUL\n NOT\n"    

def p_ExprR_Expr(p):
    "ExprR : Expr"
    p[0] = p[1]

def p_Expr_Termo(p):
    "Expr : Termo"
    p[0] = p[1]

def p_Expr_Termo_ADD(p):
    "Expr : Expr '+' Termo"
    p[0] = p[1]+p[3]+"ADD\n"  

def p_Expr_Termo_SUB(p):
    "Expr : Expr '-' Termo"
    p[0] = p[1]+p[3]+"SUB\n"

def p_Termo_Factor_MUL(p):
    "Expr : Termo '*' Factor"
    p[0] = p[1]+p[3]+"MUL\n"

def p_Termo_Factor_DIV(p):
    "Expr : Termo '/' Factor"
    erro = "\"erro -> divisão por zero >:(\"\n"
    print(p[3])
    p[0] = p[1]+p[3]+ "JZ IF0\n"+ "DIV\n" + "IF0:\n" + "ERR " + erro + "\n" 

def p_Termo_Factor(p):
    "Termo : Factor"
    p[0] = p[1]

def p_Declaracao_INT(p):
    "Declaracao : INT id"
    p[0] = "PUSHI 0\n"
    global atribs
    global atrib_counter
    atribs[p[2]] = atrib_counter
    atrib_counter+=1

def p_Atribuicao_INT(p):
    "Atribuicao : id '=' ExprR"
    global atribs
    p[0] = p[3] + "STOREG " + str(atribs[p[1]]) + "\n"
    return p[1]

'''
def p_Declaracao_STRING(p):
    "Declaracao : STRING id"
    p[0] = "PUSHS " +"\n"
    global atribs
    global atrib_counter
    atribs[p[2]] = atrib_counter
    atrib_counter+=1    

def p_Atribuicao_STRING(p):
    "Atribuicao : id '=' TEXT"
    global atribs
    p[0] = "PUSHS "+ p[3] + "\nSTOREG " + str(atribs[p[1]]) + "\n"
    return p[1]    
'''

def p_Atribuicoes_Atribuicao(p):
    "Atribuicoes : Atribuicao"
    p[0] = p[1]

def p_Atribuicoes_Atribuicao_NEWLINE(p):
    "Atribuicoes : Atribuicao NEWLINE"
    p[0] = p[1]

# atribs : atribs atrib
def p_Atribuicoes_Atribuicao_Varias(p):
    "Atribuicoes : Atribuicoes Atribuicao"
    p[0] = p[1] + p[2]

def p_Atribuicoes_Atribuicao_Varias_NEWLINE(p):
    "Atribuicoes : Atribuicoes NEWLINE Atribuicao"
    p[0] = p[1] + p[2]

'''
Atribuicoes : Atribuicao
            : Atribuicoes Atribuicao  

 Atribuicao : id = Expr

Operacoes : Atribuicoes
          : IFELSE

FOR (ExprR) {a=2 IFELSE}

FOR (ExprR)  {Operacoes}   
'''

def p_Atribuicao_IFELSE(p):
    "Atribuicoes : IFELSE"
    p[0] = p[1]

def p_Atribuicao_ONLYIF(p):
    "Atribuicao : ONLYIF"
    p[0] = p[1]    

def p_Atribuicao_FORDO(p):
    "Atribuicao : FORDO"
    p[0] = p[1]

def p_Atribuicao_PRINT(p):
    "Atribuicao : PRINTER"
    p[0] = p[1]

def p_Atribuicao_SCAN(p):
    "Atribuicao : SCANNER"
    p[0] = p[1]


def p_IF_ELSE(p):
    "IFELSE : IF '(' ExprR ')' '{' Atribuicoes '}' ELSE '{' Atribuicoes '}'"
    p[0] = p[3]+ "\n" + "JZ IF0\n" + p[6] + "\nJUMP END\n"+ "\nIF0:\n" + p[10]+ "\nEND:\n"

def p_IF(p): 
    "ONLYIF : IF '(' ExprR ')' '{' Atribuicoes '}'"
    p[0] = p[3]+ "\n" + "JZ IF0\n" + p[6] + "\nIF0:\n"

def p_FORDO(p): 
    "FORDO : FOR '(' Atribuicao ',' ExprR ')' DO '{' Atribuicoes '}'"
    global atribs
    a = p[3][-2]
    p[0] = p[3]+ "FOR:\n"+ "\n" + p[5]+ "\n" + "JZ IF \n" + p[9] + "PUSHG "+ a +"\nPUSHI 1\nADD\nSTOREG " + a +"\n" + "JUMP FOR\n" + "\nIF:\n"


def p_ARGS(p):
    "ARGS : ARG"
    p[0] = p[1]

def p_ARG_0(p):
    "ARG : "
    #p[0] = p[1]

def p_ARG_1(p):
    "ARG : id"
    p[0] = p[1]

def p_ARG_varios(p):
    "ARGS : ARGS ',' ARG"   
    p[0] = p[1] + p[2]    

def p_FUNC(p):
    "FUNC : NOME '(' ARGS ')' '{' Atribuicoes '}'"
    p[0] = p[6]
    print("nome:" + p[1])

def p_FUNC_NEWLINE(p):
    "FUNC : NOME '(' ARGS ')' '{' NEWLINE Atribuicoes NEWLINE '}'"
    p[0] = p[7]
    print("nome:" + p[1])    


def p_TEXTO(p):
    "TEXTO : TEXT" 
    p[0] = "PUSHS "+p[1]+"\n"+"WRITES\n"     

def p_STRING_PRINTER(p):
    "PRINTER : PRINT '(' TEXTO ')'"
    p[0] = p[3]

def p_INT_PRINTER(p):
    "PRINTER : PRINT '(' id ')'"
    global atribs
    p[0] = "PUSHG "+ str(atribs[p[3]]) + "\nWRITEI\n"   

def p_SCANNER(p): 
    "SCANNER : SCAN '(' id ')'" 
    global atribs
    p[0] = "READ "+ "\nSTOREG " +str(atribs[p[3]]) + "\nPUSHG " +str(atribs[p[3]]) + "\nATOI" + "\nSTOREG " +str(atribs[p[3]]) + "\n"

###########################################################################
#### QUERIES ######
'''
def p_QUADRADO(p):
    "QUADRADO : QUAD '(' ID ',' ID ',' ID ',' ID ')' '{' IFELSE '}'" 
QUAD(a,b,c,d){IF ((a==b)E(a==c)E(a==d))}
'''

#error rule for syntax errors
def p_error(p):
    print("Syntax error in input:", p)

#buil the parser
parser = yacc.yacc()

#reading input
file = open("input.txt","r")
for linha in file:
    result = parser.parse(linha)
    print("Frase válida")

out.write("STOP")
out.close()