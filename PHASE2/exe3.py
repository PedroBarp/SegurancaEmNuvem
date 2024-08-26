import random

# Valores fornecidos
p = 1041607122029938459843911326429539139964006065005940226363139
g = 10
A = 105008283869277434967871522668292359874644989537271965222162

# Gerar um número aleatório b com pelo menos 40 dígitos e menor que p
# b = random.randint(10**39, p-1)
b = 466576100834174955391144577479300074751732290939997481929154

# Calcular B
B = pow(g, b, p)

print("Valor de b:", b)
print("Valor de B:", B)
