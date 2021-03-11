# Exames Medicos Desportivos
# -- Tarefa 7 : Produz uma listagem dos atletas que praticam atletismo ordenada pela idade;

import re

with open('emd.csv') as f:
	next(f)

	atletas = []
	for linha in f:
		campos = re.split(r',' , linha)
		modalidade = campos[8]
	
		if modalidade == 'Atletismo':
			primeiro = campos[3]
			ultimo = campos[4]
			idade = campos[5]

			nome_completo = primeiro + ' ' + ultimo
			atletas.append((nome_completo, int(idade)))

	atletas.sort(key=lambda p : (p[1],p[0]))
	
	print('Atletas que praticam atletismo por idade :')
	print(atletas)