# # lista = []

# # lista += [1]
# # lista.append(2)
# # lista += ["y"]
# # lista.append([4])
# # print(lista)

def listar_numeros_ingresados():
    """Solicita al usuario números y los almacena en orden de ingreso."""
    # Inicializar una lista vacía para almacenar los números
    numeros_ingresados = []

    print("Por favor, ingrese números uno por uno. Escriba 'fin' para terminar y mostrar la lista.")

    while True:
        # Solicitar la entrada al usuario
        entrada = input("Ingrese un número o 'fin': ").strip().lower()

        # Verificar si el usuario quiere terminar
        if entrada == 'fin':
            break

        # Intentar convertir la entrada a un número (entero o flotante)
        try:
            # Puedes usar float() si esperas números decimales, o int() si solo quieres enteros
            numero = float(entrada)
            # Agregar el número a la lista
            numeros_ingresados.append(numero)
        except ValueError:
            # Manejar el caso en que la entrada no es un número ni 'fin'
            print(f"'{entrada}' no es una entrada válida. Intente de nuevo o escriba 'fin'.")

    # Mostrar el resultado final
    print("\n--- Resultado ---")
    if numeros_ingresados:
        print("Números ingresados (en orden):")
        # Imprimir la lista
        print(numeros_ingresados)
    else:
        print("No se ingresó ningún número.")

listar_numeros_ingresados()

