# Autora: Ana Clara Loureiro
# Data: 19/12/2020
# Versao 1.0
#########################################################
# Teste de Python - NAVI

# Questao 3
# Le um arquivo do tipo:
	# nome1
	# nota1
	# nome2
	# nota2
	# nome3
	# nota3
	# nome4
	# nota4
	# nome5
	# nota5
#################################################################3


# Ler o arquivo e armazenar os dados em um vetor linhas

# nome_arquivo = input ("escreva o nome do arquivo:  ")
nome_arquivo = "teste_alunos.txt"
arquivo = open (nome_arquivo, "r")
linhas = arquivo.readlines()

#inicializando as variaveis:
nota_alunos = {} #dicionario das notas


for i in range (len(linhas)-1):
	if (i % 2 == 0):
		linhas[i] = linhas[i][0:-1]
		nota_alunos [linhas[i]] = float (linhas[i+1])

aluno_nota_maxima = max (nota_alunos, key = nota_alunos.get)
nota_maxima = nota_alunos [aluno_nota_maxima]


print("Aluno com a maior nota:", aluno_nota_maxima)
print ("Nota:", nota_maxima)
