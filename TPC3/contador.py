import sys
import re

input_regex = r'(?P<soma>-?\d+)|(?P<ligar>[Oo][Nn])|(?P<desligar>[Oo][Ff]{2})|(?P<display>=)'
    
def main(imp):
    estado_calculadora = False
    soma_calculadora = 0

    with open(imp[1], 'r') as file:
        str = file.read()
    
    for object in re.finditer(input_regex, str, flags=re.IGNORECASE):
        if object.group('soma'):
            if estado_calculadora:
                soma_calculadora += int(object.group('soma'))

        elif object.group('ligar'):
            estado_calculadora = True

        elif object.group('desligar'):
            estado_calculadora = False

        elif object.group('display'):
            print(soma_calculadora)

if __name__ == "__main__":
    main(sys.argv)
