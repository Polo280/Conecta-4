from tabulate import tabulate

def main():
    # Se crea el tablero, los nombres de los jugadores, y se entra en un ciclo que se cumple mientras checar() diga que el juego no ha terminado
    tablero = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    jugador1 = input('Nombre de jugador naranja \U0001F7E0: ')
    jugador2 = input('Nombre de jugador amarillo \U0001F7E1: ')
    print()
    iters = 1                # Variable con numero de iteraciones para manejar turnos
    victoria = 0
    while victoria == 0:
        if iters % 2 == 1:
            turno(1, tablero, jugador1, jugador2)
            victoria = checar(tablero)
            display_Tablero(tablero)
        else:
            turno(2, tablero, jugador1, jugador2)
            victoria = checar(tablero)
            display_Tablero(tablero)
        iters += 1

    if victoria == 1:
        print(f"Gana jugador {jugador1}")
    elif victoria == 2:
        print(f"Gana jugador {jugador2}")
    else:
        print("Ha habido un empate")

def turno(jugador, tablero: list, user1, user2):
    # Checa el input de un jugador para elegir la columna, la verifica y en caso de que este en el rango del tablero llama a agregar_Ficha()
    jugadores = [user1, user2]             # Index de 0 y 1
    while True:                            # Para hacer handling de una jugada invalida sin aumentar el turno
        try:
            print(f"Jugador {jugadores[jugador - 1]}")  # -1 para hacer match con la lista de jugadores
            col = int(input("Introduce columna: "))
            if col > 7 or col < 1:
                raise ValueError
            agregar_Ficha(tablero, jugador, col-1)        # Llamar a funcion para agregar ficha en columna especificada
            break
        except:
            print("Invalido, intentar de nuevo\n")
    print()


def agregar_Ficha(tablero: list, id_jugador, col):
    # Agrega ficha del jugador correspondiente en el tablero, si la columna ya esta llena lanza un ValueError para hacer handling adecuado
    if tablero[0][col] != 0:
        raise ValueError
    for fila in range(0, len(tablero)-1):           # Iteracion en filas del tablero (0 --> 4)
        if tablero[fila+1][col] != 0:               # Si la siguiente ya está ocupada
            if tablero[fila][col] != 0: break       # Esto solo pasa cuando la columna ya esta toda llena y no se pueden agregar mas fichas
            tablero[fila][col] = id_jugador
            break
        if fila == 4:             # Cuando este en la 4 significa que estara en la ultima iteracion
            tablero[fila+1][col] = id_jugador

def display_Tablero(tablero: list):
    ''' Recibe un tablero interno que funciona unicamente con 0, 1s, y 2s y lo asocia a cada tipo de fichas mediante if's
     0 = no hay ficha (circulo cafe), 1 = ficha de jugador 1, 2 = ficha de jugador 2 '''
    tablero_chido = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "]
                    , [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "]]
    for fila in range(len(tablero)):
        for item in range(len(tablero[fila])):
            if tablero[fila][item] == 0:
                tablero_chido[fila][item] = "\U0001F7E4"
            elif tablero[fila][item] == 1:
                tablero_chido[fila][item] = "\U0001F7E0"
            else:
                tablero_chido[fila][item] = "\U0001F7E1"
    print(tabulate(tablero_chido, tablefmt='orgtbl'))

def checar(tablero: list):
    # Revisa patrones en el taablero para verificar si ha gaanado algun jugador o hay un empate
    # Revisar por victoria en fila
    for fila in tablero:
        for item in range(len(fila)-3):
            if fila[item] != 0 and fila[item] == fila[item+1] == fila[item+2] == fila[item+3]:
                return fila[item]
    # Revisar en vertical (index 0, +1, +2, +3 en fila pero columna permanece igual)
    for col in range(7):
        for fila in range(len(tablero) - 3):
            if tablero[fila][col] != 0 and tablero[fila][col] == tablero[fila+1][col] == tablero[fila+2][col] == tablero[fila+3][col]:
                return tablero[fila][col]
    # Revisar en diagonal (Arriba Izq - Abajo derecha)
    for fila in range(len(tablero)-3):
        for col in range(len(tablero[fila])-3):
            if tablero[fila][col] != 0 and tablero[fila][col] == tablero[fila+1][col+1] == tablero[fila+2][col+2] == tablero[fila+3][col+3]:
                return tablero[fila][col]
    # Revisar en diagonal (Abajo izq - Arriba derecha)
    for fila in range(3, len(tablero)):
        for col in range(len(tablero[fila])-3):
            if tablero[fila][col] != 0 and tablero[fila][col] == tablero[fila-1][col+1] == tablero[fila-2][col+2] == tablero[fila-3][col+3]:
                return tablero[fila][col]
    #Checar empate
    for fila in range(len(tablero)):
        if 0 in tablero[fila]:        # Revisar cada fila de la matriz tablero
            break
        if fila == 5:                 # Si no hay ningún 0 en ninguna fila return 3 para generar empate
            return 3
    return 0                           # Si no ha habido algun return para este punto significa que el juego sigue


if __name__ == '__main__':
    main()