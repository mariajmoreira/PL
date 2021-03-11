# Exames Medicos Desportivos
# -- Tarefa 4 :  Qual a distribui ̧c ̃ao de atletas registados por sexo?
import re 

'''
f = open("emd.csv")
#salta a primeira linha
next(f)

fem = 0
masc = 0

for linha in f:
	campos = re.split(r',' , linha)
	genero = campos[6]

	if genero == 'F' : 
		fem += 1
	else:
		masc += 1

print('Feminino:', fem)
print('Masculino:', masc)

f.close()
'''

# OUTRA RESOLUCAO 
# COM DICIONARIOS

f = open("emd.csv")
#salta a primeira linha
next(f)

d = {'M' : 0, 'F' : 0}

for linha in f:
	campos = re.split(r',' , linha)
	genero = campos[6]

	d[genero] += 1

print('Feminino:', d['F'])
print('Masculino:', d['M'])

f.close()

