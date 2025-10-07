def sumar_pares_de_lista(lista=[]):
    total = 0
    for numero in lista:
        if es_par(numero):
            total += numero
    return total

def mayor_numero_impar(lista=[]):
    lista_impar = []
    for num in lista:
        if not es_par(num):
            lista_impar += [num]
    if not lista_impar:
        return []
    else:
        return max(lista_impar)

def mostrar_lista_en_orden(lista):
    for numero in lista:
        print(numero)

def mostrar_numeros_pares(lista):
    for numero in lista:
        if es_par(numero):
            print(numero)

def mostrar_numeros_en_pos_impares(lista):
    for i in range(len(lista)):
        if not es_par(i):
            print(lista[i])

def esta_entre(num, num1, num2): #validacion del ingreso del numero en rango
    if num >= num1 and num <= num2:
        return True
    else:
        return False
    
def es_positivo(num) -> bool | None:
        try:
            if num >= 0:
                return True
            else:
                return False
        except (TypeError):
            return None
        
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False