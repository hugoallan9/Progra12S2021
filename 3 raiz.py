'''
Estre programa encuetra la raíz cúbica de un número entero
utilizando para ello fuerza bruta *enumeración exhaustiva*
'''

cubo = 8
for x in range(abs(cubo)+1):
    if x**3 >= abs(cubo):
        break

if x**3 != abs(cubo):
    print('El número ', cubo, 'no tiene raíz cúbica')
elif( cubo < 0 ):
    print('La raíz cúbica de', cubo, 'es', -x)
else:
    print('La raíz cúbica de', cubo, 'es', x)
