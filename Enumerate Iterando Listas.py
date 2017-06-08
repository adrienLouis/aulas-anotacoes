#lista_nums = [100,200,300,400,500,600,700,800,900,1000,1100,1200]
#for item in range(len(lista_nums)):
#    lista_nums[item]+=1000
#print(lista_nums)
#O enumerate() cria uma tupla com cada elemento de uma lista.
#Exemplo:
#l = ['a', 'b', 'c', 'd', 'e', 'f']
#list(enumerate(l)) #Cria uma LISTA, contendo Tuplas da Lista anterior.
#>>> [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f')]
#
#Enumerate:

lista_nums = [100,200,300,400] #LISTA comum de 4 elementos.
for idx, item in enumerate(lista_nums): #Para cada número e valor em cada Tupla gerada à partir da Lista lista_nums;
    lista_nums[idx]+=1000 #Somar 1000 ao VALOR encontrado na LISTA à partir do NÚMERO da Tupla.
print(lista_nums) # Imprimir o valor, já alterado, da lista.
