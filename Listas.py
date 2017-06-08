#  Criando uma lista:
lista = [1, 2, 3, 4, 'J', 'Q', 5.9]
#  Listas guardam todos os types.

#  Acessando um valor de uma lista:
lista[0] #  Primeiro valor
lista[1] #  Segundo valor
lista[-1] #  Excessão: Último valor

#  Adicionando valores à lista:
lista = lista + [8]
lista += [8]
#  Os dois adicionam ao final da lista o inteiro 8.

lista.append(8)
#  Adiciona o inteiro 8 ao final da lista.

lista.append([8])
#  Adiciona uma sublista. Cuidado.

lista = [9, 6, 4] + lista
#  Adiciona 9 6 e 4 ao começo da lista.

#  DELETANDO valores das listas;
del(lista[0], lista[-1]) #Deleta o primeiro e último valor.
del(lista[2:4]) # Deleta valores entre os índices 2 e 4, incluindo-os.

#POP só aceita 1 argumento.
lista.clear() # APAGA TODOS os elementos de listas. Torna-a lista = [].
lista.pop() # APAGA por padrão o último valor da lista, e retorna ele.
lista.pop(0) # APAGA o elemento de índice 0. E o retorna.
lista.pop(-1) # APAGA o último valor sa lista.

print(lista)
#INSERT

lista.insert(0, 'aaa') # Insere 'aaa' como indice 0 e avança os outros.
lista.append('zzz') # Insere no final.

#Alterar elementos de índice x;
lista[1] = 'hhhh' #Altera elementos em índices.

#INVERTER Valores de uma lista:
lista.reverse() # -1 se torna 0 e vice e versa.

#ORDENAR valores de uma lista de forma ascendente:
lista.sort() #Coloca números em ordem crescente e letras em ordem alfabética.
lista.sort(reverse=True) # deve ser ordenada de forma REVERSA.

#CONTAR quantas vezez um elemento de uma lista aparece na mesma:
lista.count('elemento a ser contado') #retorna um número inteiro.

#Saber o índice de certo elemento:
lista.index('elemento a ser retornado o índice')
#Só retorna a primeira ocorrência na lista do valor.
#Caso tenha mais de um 'valor' na lista, somente o primeiro será retornado.


#Listas dentro de Listas:

listad = [1,2,3,4[5,6,7,8]]
listad[4] #  	Retorna: 			[5,6,7,8]
listad[4][2]  # Retorna o inteiro 	7.