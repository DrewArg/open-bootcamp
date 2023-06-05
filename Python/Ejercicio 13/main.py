from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

numeros = filter(lambda a: a % 2 != 0,numeros)

resultado = reduce(lambda a,b: a+b, numeros)

print(resultado)