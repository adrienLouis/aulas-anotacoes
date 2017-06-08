alunos = 10
medias = []

for i in range(1, alunos+1):
	notas = 0

	for j in range(1, 5):
		notas += float(input("Digite a Nota %i de 4 do aluno %i de %i" %(j, i, alunos)))

	notas /= 4
	medias.append(notas)

num = 0

for media in medias:
	if media >= 7.0:
		num += 1

print("O número de alunos com média maior que 7 é: ", num)