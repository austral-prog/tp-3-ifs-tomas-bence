def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    cont=input()
    tiene_numero= '0'in cont or '1' in cont or '2' in cont or '3' in cont or '4' in cont or '5' in cont or '6' in cont or '7' in cont or '8' in cont or '9' in cont
    if len(cont)>=8 and tiene_numero:
        print('Contraseña valida')
    else:
        if len(cont)<8:
            print('Contraseña muy corta')
        if not tiene_numero:
            print('Debe contener un numero')
