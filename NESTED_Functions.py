'''
Funções dentro de funções.
'''

# def f1():
#     X = 8001
#     def f2():
#         print(X)
#     f2()

# f1()     # Retorna 8001.



#//////#

# X = 100
#
# def f1():
#     global X     # Usa a variável GLOBAL X
#     def f2():
#         print(X)
#     f2()
#
# f1()        # Retorna o valor de f2(), que retorna 100.


#//////#


# def exp(N):
#     def eleva(X):
#         print(X**N)
#     return eleva
#
#
# h = exp(2)  # H passa a ter exp(N) = exp(2),
# h(6)        # Quando chamado, H retorna eleva(6), sendo que exp(2)!
#             # (Uma função própria de valor pré definido foi criada)
#
# g = exp(10) # G passa a ser uma função exp() com argumento 10.
# g(2)        # G então, retorna eleva() com o argumento passado, 2.
#


#//////#


# def f1():
#     começo = 0
#     def f2():       # F2 não tem acesso a variável fora de sua local, por isso o uso de nonlocal.
#         nonlocal começo
#         print(começo)
#         começo += 1
#     # f2()
#     return f2       # Bem-Define f2() ao invés de chamá-la
#
# g = f1()
#
# g()
# g()
# g()
# g()
# g()
# g()
# g()
# g()

def lista():                        #Lista() retorna a função incrementa, e bem-define duas variáveis, start, e lista.
    start = 0
    lista = []
    def incrementa(item):
        nonlocal lista, start
        lista.append(item)
        start += 1
        print(item, start)
    return incrementa

compras = lista()                   # Compras retorna/recebe incrementa, bem-definindo start e lista.
compras('arroz')                    # Compras chama incrementa('arroz') e executa.
compras('feijão')                   # Compra chama etc...
compras('soja')

compras1 = lista()                  # Bem define compras1, como um objeto/função diferente separado da primeira compra.
compras1('banana')
compras1('maçã')
compras1('uva')