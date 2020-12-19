# Autora: Ana Clara Loureiro
# Data: 19/12/2020
# Versao 1.0
#########################################################
# Teste de Python - NAVI

# Questao 2
#################################################################3


# inicializacao
from math import factorial
from math import log


# Realiza as operacoes e devolve ([vetor] , maximo , media)

def cria_vetor():
	vetor = []
	for i in range (10):
		if (i % 2 == 0):
			vetor += [3**i + 7*(factorial(i))]
		else:
			vetor += [2**i + 4*(log(i))]

	maior_valor = max(vetor)
	media = sum(vetor)/len(vetor)
	return (vetor, maior_valor , round (media,2))


# Printando os resultados:
print ("Vetor =", cria_vetor()[0])
print ("Posicao do maior valor:", cria_vetor()[0].index(cria_vetor()[1]))
print ("Media dos valores =", cria_vetor()[2])

