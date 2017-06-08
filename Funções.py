# # Introdução à funções:
#
'''
# Funções entram com parâmetros e retornam valores,
# embora nem sempre as duas coisas ocorram.
#
# Variáveis se flexionam para LOCAIS, e não é recomendado
# o uso de GLOBAIS.
#
# São blocos de instruções RESTRITOS.
#
# Função vs Método:
#
# - Métodos não retornam valores.
'''
#
# def funcao():
#     print("\nMinha função.\n")
#
# funcao() # Há a necessidade de chamar as funções.
#          # Funcs podem ser chamadas de qualquer
#          # parte do código.
#
#
# ## Parâmetros de função:
#
# # Declarar parâmetros no cabeçalho de uma função
# # para que assim, todas as vezes em que a mesma for
# # invocada, será enviado também, um conjunto de
# # dados, conforme definido.
#
# # Parâmetros são variáveis locais para a função.
#
# def somapar(x, y):
#     print(x + y)
#
# somapar(10, 15) # Imprime 25.
#
# # Parâmetro DEFAULT:
# def login(usuario='root', senha='123'):
#     print(usuario, senha)
# # se não informado, usuario será 'root'
# # e senha será '123'.
#
# login()            # 'root', '123'
# login('huela')     # 'huela', '123'
#
# # Argumentos NOMEADOS e POSICIONAIS:
# #
# # Posicionais são setados de acordo com a ordem dos
# # parâmetros definidos na função, os nomeados não
# # a seguem.

# def dadosp(nome, sobrenome, idade, sexo):
#     print('Nome: {}\nSobrenome: '
#           '{}\nIdade: {}\nSexo: {}'
#           .format(nome, sobrenome, idade, sexo))
# # A instrução .format() substitui na ordem os {}
# # pelas variáveis.
#
#
# # dadosp("Cláudio", "Rogério", 30, True)
# dadosp(nome="Cláudio",
#        idade=30,
#        sobrenome="Rogério",
#        sexo=True)
# Foi setado fora de ordem, porém com instruções
# claras sobre onde atribuir os valores.

# RETORNAR VALORES:
# return
#
# def somaa(x, y):
#     # return x + y
#     total = x+ y
#     return total # Também dá BREAK na função.
#     print('A') #Não funciona, return deu break.
#
# print(somaa(10, 90))

# # RETORNO de VALORES MÚLTIPLOS:
#
# def testefunc():
#     return 20, 30
#
# x, y = testefunc()
#
#
# def testefunc2():
#     return 1, 2, 3, 4
#
# a, b, c, d = testefunc2()
# # >>> a = 1, b = 2, c = 3, d = 4

# def potencia(x):
#     quadrado = x**2
#     cubo = x**3
#
#     return (quadrado, cubo) # Será uma tupla
#                             # mesmo sem parênteses.
#
# q, c = potencia(10)
# print(q, c)


# Função Variádica:
#
# Funções variádicas, isto é, funções capazes de
# receber quantidades arbitrárias de parâmetros.

# Sintaxe:
# def func(*args, **kwargs):
#   pass

def lista_de_argumentos(*lista):
    print(lista)

# Um asterísco gera uma tupla, duas geram um dict.

def lista_de_argumentos_associativos(**dicionario):
    print(dicionario)

lista_de_argumentos(1, 2, 3, 4)

lista_de_argumentos(100, 200, 300, 400,
                    600, 900, 1000)

lista_de_argumentos_associativos(a=1,
                                 b=2,
                                 c=3,
                                 d=4)

def argumentoss(*args, **kwargs):
    print(args, kwargs)

argumentoss(1,2,3,4,um=1,dois=2,três=3)
