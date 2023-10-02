from collections import OrderedDict

# Seu JSON de entrada
json_data = {"Ano": 2020, "Tamanho": 120, "Garagem": 2}

# Defina a ordem desejada das chaves
ordem_das_chaves = ["Tamanho", "Ano", "Garagem"]

# Crie um OrderedDict ordenado pelas chaves especificadas
json_data_ordenado = OrderedDict((chave, json_data[chave]) for chave in ordem_das_chaves)

# Crie uma lista com os valores na ordem das chaves
valores_ordenados = list(json_data_ordenado.values())

# Imprima a lista de valores ordenados
print(valores_ordenados)