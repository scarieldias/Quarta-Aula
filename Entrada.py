numero = int(input ("Entrada de Numero.:  "))

def verificaEntrada (numero) :
    if numero > 0 :
        return "Numero Positivo"
    elif numero < 0 :
        return "Numero Negativo"
    else:
        return "Numero digitado igual a 'Zero'"

print(verificaEntrada(numero))    