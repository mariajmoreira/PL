# -- Problema 2 : Endereços IP 
import re 

f = open("enderecos.txt", "r")

for linha in f:
	print("---------------------------------------------------------------------------")
	print(linha)
	y = re.search(r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$', linha)
	
	if y:
		print("Endereço IPv4\n")
	else:
		x = re.search(r'^((([0-9a-zA-Z\:]{5}){7})[0-9a-zA-Z]{4})$',linha)
		if x:
			print("Endereço IPv6\n")

		else:
			print("Erro\n")

