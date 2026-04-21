def triangle():
    """
    Ejercicio 8 - Validar Triángulo

    Leer tres números que representan los lados de un triángulo mediante input().
    Verificar si pueden formar un triángulo válido e imprimir el resultado.
    Un triángulo es válido si la suma de dos lados cualesquiera es estrictamente mayor
    que el tercer lado (desigualdad triangular). Si la suma es igual, forman una línea
    recta, no un triángulo.

    Ejemplo:
        Para las entradas "3", "4" y "5", la salida esperada es:
        Los lados forman un triangulo valido

        Para las entradas "1", "2" y "5", la salida esperada es:
        Los lados no forman un triangulo valido
    """
    num1=int(input())
    num2=int(input())
    num3=int(input())
    if num1 + num2 > num3:
        print('Los lados forman un triangulo valido')
    else:
        print('Los lados no forman un triangulo valido')
