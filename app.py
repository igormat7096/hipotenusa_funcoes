# Biblioteca :

from math import sqrt

# Função que vai calcular a hipotenusa :

def calcular_hipotenusa(c1, c2):
    h = sqrt((c1**2) + (c2**2))
    return h

# Programa principal :

print("calcular hipotenusa")

# Usúario informa os valores dos catetos :

c1 = float(input("Informe o valor do 1° cateto: ").replace(",","."))
c2 = float(input("Informe o valor do 2° cateto: ").replace(",","."))

# Exebir na tela o valor da hipotenusa :

print(f"O valor da hipotenusa é {calcular_hipotenusa(c1, c2)}.")
