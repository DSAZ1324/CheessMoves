from unittest import TestCase
from movimientos import *

class Test_movimientos(TestCase):

    def test_tablero_a_cadena(self):
        dado = []
        espero = ""
        obtengo = tablero_a_cadena(dado)
        self.assertEquals(espero, obtengo)

    def test_obtener_nombre_pieza(self):
        dado = []
        espero = ""
        obtengo = obtener_nombre_pieza(dado)
        self.assertEquals(espero, obtengo)

    def test_mover_torre(self):
        dado = [[['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
[' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
], 0, 0, 0, 2]
        espero = [[' ', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
[' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
['t', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
]
        obtengo = mover_torre(dado[0], dado[1], dado[2], dado[3], dado[4])
        self.assertEqual(espero, obtengo)

    def test_mover_alfil(self):
            dado = [[['t', 'k', ' ', 'q', 'r', 'a', 'k', 't'],
                     ['p', ' ', 'p', 'p', 'p', 'p', 'p', 'p'],
                     ['a', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                     ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
                     ], 0, 2, 0, 2]
            espero = [['t ', 'k', ' ', 'q', 'r', 'a', 'k', 't'],
                      ['p', ' ', 'p', 'p', 'p', 'p', 'p', 'p'],
                      ['a', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                      ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
                      ]
            obtengo = mover_alfil(dado[0], dado[1], dado[2], dado[3], dado[4])
            self.assertEqual(espero, obtengo)
