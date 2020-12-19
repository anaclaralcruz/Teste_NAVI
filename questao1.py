# Autora: Ana Clara Loureiro
# Data: 19/12/2020
# Versao 1.0
#########################################################
# Teste de Python - NAVI

# Questao 1

def retorna_multiplos ():
	lista = []
	for i in range (1, 5000001):
		# MMC(2,49,37) = 2*49*37 = 3626
		if (i % 3626 == 0):
			lista += [i]
	return lista

print (len(retorna_multiplos()))
