#Looping: While
print('--------------')
print('\nWhile Comum:\n')
print('--------------')
x = 1
while x <= 10:
    print(x)
    x+=1
# Note que X têm de ser 1 para imprimir 1, 2, 3, ..., 10.


#Looping: While True
print('--------------')
print('\nWhile True:\n')
print('--------------')

x = 1
while True:
    if x <= 10:
        print(x)
        x += 1
    else:
        break

# Seguindo o mesmo padrão anterior.
# Note que há a nescessidade de quebrar o código, já que é um looping INFINITO.
print('\nOutros.....\n')

x = 1
while(x<=10):
    print(x)
    x+=1
else:
    print('else')