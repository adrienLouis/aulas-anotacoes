# AND verifica se um E o outro, obrigatoriamente...
# OR verifica se um OU o outro, qualquer um dos dois...

3 and 4 in range(1,10) #Retorna TRUE
3 or 70 in range(1,10) #Retorna True, já que 3 está na lista.

3 and 70 in range(1,10) # Retorna False.
90 or 70 in range(1,70) # Nenhum dos dois está, logo retorna FALSE.


# a = 10
# b = 25
# c = 66
#
# x = int(input('Digite um número: '))
#
# #if(x == a or x == b or x == c):
# if (x in [a, b, c]):
#     print("Igual")
# else:
#     print("Diferente")

cores = ['azul', 'amarelo', 'vermelho', 'branco']
while True:
    valor = str(input('Digite o número de uma cor, ou '
                      '0 para sair:'))
    if(valor == "0"):
        break
    elif(valor.lower() in cores):
        print('Esta cor está na minha lista.')
    else:
        print('Esta cor não está contida na minha lista.')
