# Exames Medicos Desportivos
# Tarefa 8: Produz uma listagem indicadora de quantos exames se realizaram em cada mˆes.

import re

import re 

f = open("emd.csv")
#salta a primeira linha
next(f)

meses = {}

for linha in f:
	campos = re.split(r',' , linha.strip())
	exame = campos[12]

	if exame == 'true' :
		data = campos[2]
		m = re.search(r'^([0-9]+)[-]([0-9][0-9])',data)
		if m:
			mes = m.group()

			if mes in meses.keys():
				meses[mes] += 1
			else: 
				meses[mes] = 1


meses = dict(sorted(meses.items(), key = lambda p: p[0], reverse = False))

print('Lista de quantos exames se realizaram em cada mês:')
print(meses)

f.close()