def tablero_a_cadena(tablero):
    """
    list of list -> str

    :param tablero: list of list que representa el tablero
    :return: str que representa los valores del tablero
    """
    cadena = ""
    for fila in tablero:
        cadena += str(fila) + "\n"
    return cadena


def obtener_nombre_pieza(simbolo):
    """
    (str) -> str

    >>> obtener_nombre_pieza('p')
    'Peon blanco'
    >>> obtener_nombre_pieza('R')
    'Rey Negro'

    Retorna el nombre de la pieza del ajedrez dado su simbolo

    :param simbolo: la representacion de la pieza segun el enunciado
    :return: El nombre y color de la pieza
    """
    tipo = 'Negro'
    if simbolo.islower():
        tipo = 'blanco'
    retorno = simbolo.lower()
    if retorno == 'p':
        return 'Peon ' + tipo
    elif retorno == 't':
        return 'Torre ' + tipo
    elif retorno == 'k':
        return 'Caballo ' + tipo
    elif retorno == 'a':
        return 'Alfil ' + tipo
    elif retorno == 'q':
        return 'Reina ' + tipo
    elif retorno == 'r':
        return 'Rey ' + tipo
    else:
        return 'No es una pieza'

def mover_torre1(tablero, x_inicial, y_inicial, x_final, y_final):
    """
    (list of list, int, int, int, int) -> list of list
    :param tablero: list of list que representa el tablero
    :param x_inicial: int que representa la posicion inicial en X
    :param y_inicial: int que representa la posicion inicial en Y
    :param x_final: int que representa la posicion final en X
    :param y_final: int que representa la posicion final en Y
    :return: list of list que representa un tablero final
    """
    tab = tablero.copy()
    if (x_inicial == x_final or y_inicial == y_final) and tab[x_inicial][y_inicial].lower() == 't':
            if x_inicial != x_final:
                for x in range(x_inicial +1, x_final):
                    if tab[x][y_inicial] != ' ':
                        raise ValueError('El camino no es valido')
            tab[x_final][y_inicial] = 't'
            tab[x_inicial][y_inicial] = ' '
            if y_inicial != y_final:
                for y in range(y_inicial +1, y_final):
                    if tab[x_inicial][y] != ' ':
                        raise ValueError('El camino no es valido')
            tab[x_inicial][y_final] = 't'
            tab[x_inicial][y_inicial] = ' '
    return tab

def mover_torre(tablero, x_inicial, y_inicial, x_final, y_final):
    """
    (list of list, int, int, int, int) -> list of list

    :param tablero: list of list que representa el tablero
    :param x_inicial: int que representa la posicion inicial en X
    :param y_inicial: int que representa la posicion inicial en Y
    :param x_final: int que representa la posicion final en X
    :param y_final: int que representa la posicion final en Y
    :return: list of list que representa un tablero final
    """
    tab = tablero.copy()
    if tab[y_inicial][x_inicial].lower() == 't':
        if x_inicial == x_final and y_inicial != y_final:
            if y_inicial < y_final:
                y_auxiliar = y_inicial + 1
            else:
                y_auxiliar = y_inicial - 1
            for y in range(y_auxiliar, y_final):
                if tab[y][x_inicial] != ' ':
                    raise Exception('No hay camino para mover la torre')
        elif x_inicial != x_final and y_inicial == y_final:
            if x_inicial < x_final:
                x_auxiliar = x_inicial + 1
            else:
                x_auxiliar = x_inicial - 1
            for x in range(x_auxiliar, x_final):
                if tab[x][y_inicial] != ' ':
                    raise Exception('No hay camino para mover la torre')
        else:
            raise Exception('Movimiento invalido para la torre')
        if tab[y_final][x_inicial] == ' ' \
                or (tab[y_inicial][x_inicial].islower() != tab[y_final][x_inicial].islower()):
            tab[y_final][x_inicial] = tab[y_inicial][x_inicial]
            tab[y_inicial][x_inicial] = ' '
        else:
            raise Exception('No puedo comer mis propias piezas')
    else:
        raise Exception('La pieza en x = {0} y={1} no es una torre'.format(x_inicial, y_inicial))
    return tab

def mover_alfil(tablero, x_inicial, y_inicial, x_final, y_final):
    """
    (list of list, int, int, int, int) -> list of list

    :param tablero: list of list que representa el tablero
    :param x_inicial: int que representa la posicion inicial en X
    :param y_inicial: int que representa la posicion inicial en Y
    :param x_final: int que representa la posicion final en X
    :param y_final: int que representa la posicion final en Y
    :return: list of list que representa un tablero final
    """
    tab = tablero.copy()
    if ((x_inicial - y_inicial == x_final - y_final) or (x_inicial + y_inicial == x_final + y_final)) and tab[x_inicial][y_final].lower() == 'a':
        if x_inicial - y_final:
            for x in range(x_inicial +1, y_final):
                if tab[x][y_inicial] != ' ':
                    raise ValueError('El camino no es valido')
        tab[x_final][y_inicial] = 'a'
        tab[x_inicial][y_inicial] = ' '
        if y_inicial - y_final:
            for y in range(y_inicial +1, y_final):
                if tab[x_inicial][y] != ' ':
                    raise ValueError('El camino no es valido')
        tab[x_inicial][y_final] = 'a'
        tab[x_inicial][y_inicial] = ' '
    return tab