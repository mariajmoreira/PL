import ply.yacc as yacc
from tp2_lex import tokens
#from calc_lex import literals
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
    p[0] = p[1]
    #out.write(p[1]+"\n")

def p_Comandos_comandos_comando(p):
    "Comandos : Comandos Comando"
    p[0] = p[2]   
    #out.write(p[2]+"\n")

def p_Comando_ExprR(p):
    "Comando : ExprR"
    p[0] = p[1]
    #out.write(p[1]+"\n")

def p_Comando_Declaracao(p):
    "Comando : Declaracao"
    p[0] = p[1]    

def p_Comando_Atribuicao(p):
    "Comando : Atribuicao"
    p[0] = p[1] 

def p_Comando_IFELSE(p):
    "Comando : IFELSE"
    p[0] = p[1]   

##############################################################

def p_Factor_num(p):
    "Factor : num"
    p[0] = p[1]
    print(p[0])
    out.write("PUSHI " + p[0] + "\n")

def p_Factor_num_negativo(p):
    "Factor : '-' num"
    p[0] = (int(p[2])*(-1)) 
    print(p[0]) 
    out.write("PUSHI " + p[0] + "\n")

def p_Factor_id(p):
    "Factor : id"
    p[0] = p[1]
    #print(atribs)
    out.write("PUSHG " + str(atribs[p[1]]) + "\n")
    #p[0] = p.parser.registers.get(p[1])

def p_Factor_TRUE(p):
    "Factor : TRUE"
    p[0] = p[1]
    out.write("PUSHI " + "1" + "\n")

def p_Factor_FALSE(p):
    "Factor : FALSE"
    p[0] = p[1]  
    out.write("PUSHI " + "0" + "\n")

def p_Factor_ExprR(p):
    "Factor : '(' ExprR ')'"
    p[0] = p[2]      
    print(p[0])   

def p_ExprR_Expr_menor(p):
    "ExprR : Expr '<' Expr"
    if(p[1] < p[3]): 
        p[0] = print("TRUE")
        out.write("PUSHI 0\n")
    else: 
        p[0] = print("FALSE")
        out.write("PUSHI 1\n")

def p_ExprR_Expr_maior(p):
    "ExprR : Expr '>' Expr"
    if(p[1] > p[3]): 
        p[0] = print("TRUE")
        out.write("PUSHI 0\n")
    else: 
        p[0] = print("FALSE") 
        out.write("PUSHI 1\n")

def p_ExprR_Expr_igual(p):
    "ExprR : Expr EQUALS Expr"
    #p[0] = p[1] +"=="+ p[3]
    #out.write(p[1] + " " + p[3]+ " " + "EQUAL\n")
    out.write("\nEQUAL\n")

def p_ExprR_Expr_diferente(p):
    "ExprR : Expr NOTEQUALS Expr"
    #out.write(p[1] + "\n"+ p[3] + "\nEQUAL NOT\n") 
    out.write("\nEQUAL NOT\n")         

def p_ExprR_Expr(p):
    "ExprR : Expr"
    #out.write(p[1])
    p[0] = p[1]

def p_Expr_Termo(p):
    "Expr : Termo"
    p[0] = p[1]
    #out.write(p[0])

def p_Expr_Termo_ADD(p):
    "Expr : Expr '+' Termo"
    p[0] = int(p[1]) + int(p[3])  
    print(p[0])
    out.write("ADD \n")           

def p_Expr_Termo_SUB(p):
    "Expr : Expr '-' Termo"
    p[0] = int(p[1]) - int(p[3]) 
    print(p[0])
    out.write("SUB \n") 

def p_Termo_Factor(p):
    "Termo : Factor"
    p[0] = p[1]
    #out.write(p[1])

def p_Declaracao(p):
    "Declaracao : INT id"
    p[0] = p[2]
    global atribs
    global atrib_counter
    atribs[p[2]] = atrib_counter
    atrib_counter+=1
    out.write("PUSHI 0\n")
    #print(atribs)

def p_Atribuicao(p):
    "Atribuicao : id '=' ExprR"
    global atribs
    p[0] = p[1]
    print("p[3]: ",str(p[3]))
    out.write("STOREG "+str(atribs[p[1]])+"\n")

def p_Atribuicoes_Atribuicao(p):
    "Atribuicoes : Atribuicao"
    p[0] = p[1]
    #out.write("STOREG "+str(atribs[a])+"\n")

def p_Atribuicoes_Atribuicao_Varias(p):
    "Atribuicoes : Atribuicoes Atribuicao"
    p[0] = p[1]
    #out.write(p[1]+ "\n" + p[2] + "\n")


def p_IF_ELSE(p):
    "IFELSE : IF '(' ExprR ')' '{' Atribuicoes '}' ELSE '{' Atribuicoes '}'"
    #out.write(p[3]+ "\n" + "JZ IF0\n" + p[6] + "IF0:\n")
    #print("p[3]: ",p[3])
    #print("p[6]: ",p[6])

    '''if(p[3] == 'TRUE'): 
        out.write("p[6]\n") 
    else: 
        out.write("p[10]\n") 
    '''
def p_JZIF0(p):
    "JZIF0 : JUMP"
    out.write("JZ IF0\n")


def p_IFELSE(p): 
    "IFELSE : IF '(' ExprR ')' JUMP '{' Atribuicoes '}'"
    #print("ExprR: ",p[3])
    #print("Atrib: ",p[6]) 

    #out.write(p[3]+ "\n" + "JZ IF0\n" + p[6] + "\nIF0:\n")



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
