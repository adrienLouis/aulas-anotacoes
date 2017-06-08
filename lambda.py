'''
LAMBDA
Resumo de funções
'''

f = (lambda x,y,z: print(x+y+z))        # Lambda precisa ser atribuído à uma variável.
f(1,2,3)

# O código acima é igual ao de baixo:

def f2(x, y, z):
    print(x + y + z)

f2(1, 2, 3)

#####################################################
d = (lambda x: lambda y: x+y)  # Suporte à 'nested'.|
e = d(2)    # x é 2, retorne    (lambda y).         |
e(3)        # y é 3, retorne o  valor x+y.          |
#####################################################