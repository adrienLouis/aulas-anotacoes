# Semelhantes à tuplas;
# Setados com {}

# Atribuindo valores:
d1 = dict()
# d1 = {}

d1['aaa'] = 1000
d1['bbb'] = 2000
d1['ccc'] = 3000
# No dicionário d1, a chave 'aaa' recebe o valor 1000.
# Se não existe é criada.

# Consultando valores a partir das chaves:
d1['aaa'] # Retorna 1000.

# Criando dicionários diretamente:
d2 = {1.1:"teste1", 2.2:"teste2", 3:"teste3"}
# Retorna um dicionário onde o primeiro valor antes dos
# dois pontos é a chave para o segundo valor.

# Len e Del funcionam normalmente, porém, o índice se torna a chave do dict.

# Retornar listas de CHAVES do dicionário:
d2.keys()
# Retornar listas de VALORES do dicionário:
d2.values()

# REMOVER valores do dicionário com popitem:
d2.popitem() # Remove o primeiro valor (Chave e Valor) do dict, e o retorna.

# Mesclar dicionários:
d1.update(d2) # Une d1 com d2.