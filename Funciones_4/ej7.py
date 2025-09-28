#Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
print(es_par(4))
print(es_par(5))