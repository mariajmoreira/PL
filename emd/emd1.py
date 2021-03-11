# Exames Medicos Desportivos
# -- Tarefa 1 :  Produz uma listagem apenas com o primeiro e u ́ltimo nome do atleta e a cidade onde vive;

import re 
''''
f = open("emd.csv")

for linha in f:
	m = re.search(r'^(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+)$', linha)
	if m:
		primeiro = m.group(4)
		ultimo = m.group(5)
		cidade = m.group(8)

		print(f"Primeiro nome: {primeiro} , Ultimo nome: {ultimo} , Cidade: {cidade}")

f.close()
	'''
# outra resolucao

## 
f = open("emd.csv")
next(f)

for linha in f:
	campos = re.split(r',' , linha)
	primeiro = campos[3]
	ultimo = campos[4]
	cidade = campos[7]

	print(f"Primeiro nome: {primeiro} , Ultimo nome: {ultimo} , Cidade: {cidade}")

f.close()
