# Exames Medicos Desportivos
# -- Tarefa 6 : Em 2020, a cˆamara de Braga tornou gratuito o exame a atletas do sexo feminino. Quantos atletas do sexo feminino realizaram exame em 2020? E em cada um dos outros anos?
import re 

f = open("emd.csv")
#salta a primeira linha
next(f)

anos = {}

for linha in f:
	campos = re.split(r',' , linha)
	genero = campos[6]

	if genero == 'F' :
		data = campos[2]
		m = re.search(r'^[0-9]+',data)
		if m:
			ano = m.group()

			if ano in anos.keys():
				anos[ano] += 1
			else: 
				anos[ano] = 1


anos = dict(sorted(anos.items(), key = lambda p: p[0], reverse = True))

print('Atletas do sexo feminino que realizaram exame por ano :')
print(anos)

f.close()