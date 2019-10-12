# d = dict()
#
# d['a'] = 1
# d['b'] = 5
# d['c'] = 10
#
# d = {'a': [1, 2, 3],
#      'b': {'z': [23]},
#      'c': 10}



# dict anidado
#print(d['b']['z'])
# Verificar si existe una key en un dict
# if 'a' in d:
#     print(d['a'])
# else:
#     print('No existe la llave')
import json

d = dict()

while True:
    print('1) Agregar llave y valor')
    print('2) Sacar Valor')
    print('3) Mostrar Llaves')
    print('4) Mostrar Llave-Valor')
    print('5) Eliminar Llave')
    print('6) Vaciar')
    print('7) Mostrar Valores')
    print('8) Respaldar')
    print('9) Recuperar')
    print('0) Salir')
    op = input('> ')

    if op == '1':
        llave = input('Llave: ')
        valor = int(input('Entero: '))

        if llave in d:
            lista = d[llave]
            lista.append(valor)
        else:
            lista = [valor]
            d[llave] = lista
    elif op == '2':
        llave = input('Llave: ')
        if llave in d:
            print(llave)
            print('   ', d[llave])
        else:
            print('No existe la llave', llave)
    elif op == '3':
        for llave in d.keys():
            print(llave)
    elif op == '4':
        for llave, valor in d.items():
            print(llave)
            print('\t', valor)
    elif op == '5':
        llave = input('Llave')
        if llave in d:
            d.pop(llave)
        else:
            print('No existe la llave', llave)
    elif op == '6':
        d.clear()
    elif op == '7':
        for valor in d.values():
            print(valor)
    elif op == '8':
        with open('dict.json', 'w') as file:
            json.dump(d, file, indent=5)
    elif op == '9':
        with open('dict.json', 'r') as file:
            d = json.load(file)
    elif op == '0':
        break
