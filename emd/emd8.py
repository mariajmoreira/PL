# Exames Medicos Desportivos
# Tarefa 8: Produz uma listagem das modalidades ordenada alfabeticamente e, para cada uma, indica quantos atletas realizaram exame;

import re

with open('emd.csv') as f:
	next(f)

	modalidades = {}

	for linha in f:
		campos = re.split(r',' , linha)
		modalidade = campos[8]
	
		if modalidade in modalidades:
			modalidades[modalidade] +=1
		else:
			modalidades[modalidade] = 1

	#ordenar as modalidades por ordem alfabetica		
	modalidades = dict(sorted(modalidades.items(), key = lambda p: p[0]))
	
	print('Modalidades e numero de atletas que realizaram exame:')
	print(modalidades)
	print('Numero de modalidades', len(modalidades))