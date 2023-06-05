paises = input()

paises = set(paises.split(","))

paises = sorted(paises)

resultado = ", ".join(map(str,paises))

print(resultado)