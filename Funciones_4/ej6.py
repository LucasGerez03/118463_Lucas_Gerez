#Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def es_par_o_impar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
        return 1
    else:
        print(f"El número {numero} es impar.")
        return 0

es_par_o_impar(5)