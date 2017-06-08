#range([start], stop[, step])

#start é de intervalo fechado (incluso no resultado);
#stop é de intervalo aberto (não incluso no resultado);

print(list(range(0, 10, 2)))
#note que é preciso a conversão para tipo LISTA, por padrão é um OBJ.

for i in range(-10, 0, 1):
    print(i)