def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int | None:
    num = int(input(mensaje)) 
    while num < minimo or num > maximo: 
        reintentos -= 1
        if reintentos <= 0:   
            return None     #fin de reintentos 
        print(mensaje_error)
        num = int(input(mensaje))
    return num  #fin del bucle
