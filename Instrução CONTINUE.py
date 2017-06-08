# Continue reinicia o looping, ignorando o restante do mesmo.
print()
print("Antes")
i = 0
while i < 10:
    i += 1
    if 0 == i % 2:
        continue
    #    if(i>5):
    #        break  #interrompe todo o WHILE incluindo o else.
    print(i)
else:
    print("else")
print("Depois")
