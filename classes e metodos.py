# #  Definição basica de classes
#
# class NomeDaClasse(object):
#     pass
#
# #  Definição basica de metodos:
#
# def metodo(args):
#     return args
#
#
# #  Unindo os dois:
# class NomeDaClasse(object):
#     atributo1 = None  # O atributo1 é um atributo
#     # com valor inicial None (nada).
#     # Poderia ser atributo1 = 0, por exemplo.
#
#     def metodo(self, args):
#         pass
#
# # Todos metodo criado dentro de uma classe deve
# # definir como primeiro parametro o self.
#

# Calculadora simples:

class storeNames:
    def yname(self, name):
        self.name = name
    def yage(self, age):
        self.age = age
    def ysex(self, sex):
        self.sex = sex
    def sayit(self):
        print(self.name, self.age, self.sex)

obj_um      = storeNames()
obj_dois    = storeNames()
obj_tres    = storeNames()
obj_quatro  = storeNames()

obj_um.yname('Mateus')
obj_um.yage('16')
obj_um.ysex('Masculino')
obj_um.sayit()

print(obj_um.age + obj_um.sex)
