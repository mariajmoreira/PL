# Exames Medicos Desportivos
# -- Tarefa 3 :  Produz uma lista ordenada alfabeticamente das modalidades registadas, no fim indica quantas s ̃ao;

import re 

f = open("emd.csv")
#salta a primeira linha
next(f)

#criamos set final
modalidades = set()

for linha in f:
	#separamos toda a informação do csv com virgulas
	campos = re.split(r',' , linha)
	modalidade = campos[8]

	modalidades.add(modalidade)


modalidades = list(modalidades)
modalidades.sort()

numero_modalidades = len(modalidades)

#print(campos)
print(f"Modalidades: {modalidades} , Numero de Modalidades: {numero_modalidades}")

f.close()

