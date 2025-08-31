#Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def es_par_o_impar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

es_par_o_impar(5)