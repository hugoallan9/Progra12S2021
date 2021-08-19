def imprimir_movimiento(partida, llegada):
    print('Mover de la torre', partida, ' a la torre', llegada)

def hanoi(n,partida, pivote,llegada):
    if n == 1:
        imprimir_movimiento(partida, llegada)
    else:
        hanoi(n-1, partida, llegada, pivote)
        hanoi(1, partida, pivote, llegada)
        hanoi(n-1, pivote, partida, llegada)

hanoi(4, 'A', 'B', 'C')