# Exames Medicos Desportivos
# -- Tarefa 5 : Dos atletas que realizaram exame, quantos s ̃ao federados? E quantos foram aprovados no exame?
import re 


f = open("emd.csv")
#salta a primeira linha
next(f)

d = {'F' : 0, 'A' : 0}

for linha in f:
	campos = re.split(r',' , linha.strip())
	federado = campos[11]
	aprovado = campos[12]

	if federado == 'true':
		d['F'] += 1

	if aprovado	== 'true':
		d['A'] += 1

print('Atletas Federados:', d['F'])
print('Atletas Aprovados:', d['A'])

f.close()