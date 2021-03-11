# Exames Medicos Desportivos
# -- Tarefa 2 :  Produz uma lista ordenada alfabeticamente dos clubes desportivos registados, no fim indica quantos sao;

import re 

f = open("emd.csv")
#salta a primeira linha
next(f)

#criamos set final
clubes = set()

for linha in f:
	#separamos toda a informação do csv com virgulas
	campos = re.split(r',' , linha)
	clube = campos[9]

	clubes.add(clube)


clubes = list(clubes)
clubes.sort()

numero_clubes = len(clubes)

#print(campos)
print(f"Clubes Registados: {clubes} , Numero de Clubes: {numero_clubes}")

f.close()

