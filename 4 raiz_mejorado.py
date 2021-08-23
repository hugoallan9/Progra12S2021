cubo = 27
epsilon = 0.01
raiz_propuesta = 0
incremento = 0.5
numero_intentos = 0

while abs(raiz_propuesta**3 - cubo) >=epsilon and numero_intentos <= cubo:
    raiz_propuesta += incremento
    numero_intentos += 1

print('El numero de iteraciones fue=', numero_intentos)
if( abs(raiz_propuesta**3 - cubo) >=epsilon ):
    print('No fue posible hallar la raíz cúbica de ', cubo)
else:
    print('La raíz cúbida de ', cubo, 'es', raiz_propuesta, ' con un error de ', epsilon)