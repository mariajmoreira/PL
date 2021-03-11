# -- Problema 4 : Matriculas de outro mundo
import re 

f = open("matriculas.txt", "r")

i=0
for linha in f:
	print("---------------------------------------------------------------------------")
	print(linha)
	
	y = re.search(r'^((\d{2}[:]){3}|(\d{2}[\.]{3}){3}|(\d{2}[-]){3})(\d{2})$',linha)
	if y:
		print("Matricula Válida\n")
		i+=1
	else:
		print("Matricula Inválida\n")

print("----------------------------------------------------------------------------")
print("Existem %s matriculas válidas" %i)