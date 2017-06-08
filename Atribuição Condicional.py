# -*- coding: utf-8 -*-
#
#===Atribuição Condicional======================
#<variável> = <valor1> if (True) else <valor2>
#var = 10 if 10 == 10 else 20
#===============================================

num1 = int(input("Digite um número: "))
s = "Par" if num1 % 2 == 0 else "Ímpar"
# s é igual á Par se o resto de num1 for 0, se não ele é igual à "Impar".

print(s)