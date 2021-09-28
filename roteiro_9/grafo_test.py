import unittest
from meu_grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.u = MeuGrafo(["0", "1", "2", "3"])
        self.u.adicionaAresta("A", "0", "1")
        self.u.adicionaAresta("B", "1", "2")
        self.u.adicionaAresta("C", "2", "3")

        # Grafos direcionados
        self.grafo_dir_1 = MeuGrafo(V=['A', 'B', 'C', 'D'])
        self.grafo_dir_1.adicionaAresta('a1', 'A', 'B')
        self.grafo_dir_1.adicionaAresta('a2', 'A', 'C')
        self.grafo_dir_1.adicionaAresta('a3', 'B', 'C')
        self.grafo_dir_1.adicionaAresta('a4', 'C', 'A')
        self.grafo_dir_1.adicionaAresta('a5', 'C', 'D')

        self.grafo_dir_2 = MeuGrafo(V=[chr(i) for i in range(65, 70)])
        self.grafo_dir_2.adicionaAresta('a1', 'A', 'B')
        self.grafo_dir_2.adicionaAresta('a2', 'B', 'C')
        self.grafo_dir_2.adicionaAresta('a3', 'C', 'A')
        self.grafo_dir_2.adicionaAresta('a4', 'B', 'D')
        self.grafo_dir_2.adicionaAresta('a5', 'E', 'D')
        self.grafo_dir_2.adicionaAresta('a6', 'E', 'E')

        self.grafo_dir_3 = MeuGrafo(['2', '9', '10', '11', '8', '7', '5', '3'])
        self.grafo_dir_3.adicionaAresta('a', '7', '11')
        self.grafo_dir_3.adicionaAresta('b', '7', '8')
        self.grafo_dir_3.adicionaAresta('c', '5', '11')
        self.grafo_dir_3.adicionaAresta('d', '3', '8')
        self.grafo_dir_3.adicionaAresta('e', '3', '10')
        self.grafo_dir_3.adicionaAresta('f', '11', '10')
        self.grafo_dir_3.adicionaAresta('g', '8', '9')
        self.grafo_dir_3.adicionaAresta('h', '11', '9')
        self.grafo_dir_3.adicionaAresta('i', '11', '2')

        self.grafo_dir_4 = MeuGrafo(['x' + str(i) for i in range(1, 11)])
        self.grafo_dir_4.adicionaAresta('e1', 'x1', 'x2')
        self.grafo_dir_4.adicionaAresta('e2', 'x1', 'x3')
        self.grafo_dir_4.adicionaAresta('e3', 'x1', 'x6')
        self.grafo_dir_4.adicionaAresta('e4', 'x2', 'x5')
        self.grafo_dir_4.adicionaAresta('e5', 'x3', 'x5')
        self.grafo_dir_4.adicionaAresta('e6', 'x3', 'x4')
        self.grafo_dir_4.adicionaAresta('e7', 'x4', 'x5')
        self.grafo_dir_4.adicionaAresta('e8', 'x6', 'x7')
        self.grafo_dir_4.adicionaAresta('e9', 'x6', 'x8')
        self.grafo_dir_4.adicionaAresta('e10', 'x5', 'x9')
        self.grafo_dir_4.adicionaAresta('e11', 'x7', 'x9')
        self.grafo_dir_4.adicionaAresta('e12', 'x8', 'x9')
        self.grafo_dir_4.adicionaAresta('e13', 'x9', 'x10')

        self.grafo_dir_5 = MeuGrafo([str(i) for i in range(0, 6)])
        self.grafo_dir_5.adicionaAresta('a', '0', '1')
        self.grafo_dir_5.adicionaAresta('b', '1', '2')
        self.grafo_dir_5.adicionaAresta('c', '0', '2')
        self.grafo_dir_5.adicionaAresta('d', '2', '4')
        self.grafo_dir_5.adicionaAresta('e', '4', '5')
        self.grafo_dir_5.adicionaAresta('f', '5', '3')

        self.grafo_dir_6 = MeuGrafo([str(i) for i in range(1, 8)])
        self.grafo_dir_6.adicionaAresta('a', '4', '6')
        self.grafo_dir_6.adicionaAresta('b', '2', '6')
        self.grafo_dir_6.adicionaAresta('c', '2', '4')
        self.grafo_dir_6.adicionaAresta('d', '4', '7')
        self.grafo_dir_6.adicionaAresta('e', '5', '7')
        self.grafo_dir_6.adicionaAresta('f', '4', '5')
        self.grafo_dir_6.adicionaAresta('g', '1', '5')
        self.grafo_dir_6.adicionaAresta('h', '1', '4')
        self.grafo_dir_6.adicionaAresta('i', '1', '2')
        self.grafo_dir_6.adicionaAresta('j', '1', '3')
        self.grafo_dir_6.adicionaAresta('k', '3', '4')
        self.grafo_dir_6.adicionaAresta('l', '2', '3')

        self.grafo_dir_7 = MeuGrafo([str(i) for i in range(0, 6)])
        self.grafo_dir_7.adicionaAresta('a', '0', '2')
        self.grafo_dir_7.adicionaAresta('b', '1', '2')
        self.grafo_dir_7.adicionaAresta('c', '2', '4')
        self.grafo_dir_7.adicionaAresta('d', '1', '4')
        self.grafo_dir_7.adicionaAresta('e', '5', '1')
        self.grafo_dir_7.adicionaAresta('f', '4', '5')
        self.grafo_dir_7.adicionaAresta('g', '0', '4')
        self.grafo_dir_7.adicionaAresta('h', '0', '3')
        self.grafo_dir_7.adicionaAresta('i', '3', '4')
        self.grafo_dir_7.adicionaAresta('j', '3', '5')

        self.grafo_dir_8 = MeuGrafo([str(i) for i in range(0, 8)])
        self.grafo_dir_8.adicionaAresta('a', '0', '1')
        self.grafo_dir_8.adicionaAresta('b', '2', '0')
        self.grafo_dir_8.adicionaAresta('c', '2', '3')
        self.grafo_dir_8.adicionaAresta('d', '2', '5')
        self.grafo_dir_8.adicionaAresta('e', '5', '7')
        self.grafo_dir_8.adicionaAresta('f', '3', '6')
        self.grafo_dir_8.adicionaAresta('g', '6', '3')
        self.grafo_dir_8.adicionaAresta('h', '4', '6')
        self.grafo_dir_8.adicionaAresta('i', '3', '4')
        self.grafo_dir_8.adicionaAresta('j', '1', '2')

        self.grafo_dir_9 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L'])
        self.grafo_dir_9.adicionaAresta('1', 'A', 'B')
        self.grafo_dir_9.adicionaAresta('2', 'B', 'H')
        self.grafo_dir_9.adicionaAresta('3', 'A', 'H')
        self.grafo_dir_9.adicionaAresta('4', 'A', 'C')
        self.grafo_dir_9.adicionaAresta('5', 'C', 'G')
        self.grafo_dir_9.adicionaAresta('6', 'C', 'H')
        self.grafo_dir_9.adicionaAresta('7', 'A', 'E')
        self.grafo_dir_9.adicionaAresta('8', 'E', 'G')
        self.grafo_dir_9.adicionaAresta('9', 'K', 'G')
        self.grafo_dir_9.adicionaAresta('10', 'K', 'F')
        self.grafo_dir_9.adicionaAresta('11', 'D', 'E')
        self.grafo_dir_9.adicionaAresta('12', 'D', 'F')
        self.grafo_dir_9.adicionaAresta('13', 'I', 'K')
        self.grafo_dir_9.adicionaAresta('14', 'F', 'I')
        self.grafo_dir_9.adicionaAresta('15', 'I', 'L')
        self.grafo_dir_9.adicionaAresta('16', 'L', 'L')

        self.vertices = [chr(i) for i in range(65, 91)]
        self.vertices.append("AA")
        self.vertices.append("AB")
        self.vertices.append("AC")
        self.vertices.append("AD")
        self.vertices.append("AE")
        self.vertices.append("AF")
        self.vertices.append("AG")
        self.grafo_dir_10 = MeuGrafo(self.vertices)
        self.grafo_dir_10.adicionaAresta('1', 'A', 'B', 3)
        self.grafo_dir_10.adicionaAresta('2', 'A', 'H', 1)
        self.grafo_dir_10.adicionaAresta('3', 'A', 'C', 1)
        self.grafo_dir_10.adicionaAresta('4', 'B', 'D', 4)
        self.grafo_dir_10.adicionaAresta('5', 'B', 'E', 5)
        self.grafo_dir_10.adicionaAresta('6', 'H', 'F', 1)
        self.grafo_dir_10.adicionaAresta('7', 'C', 'G', 2)
        self.grafo_dir_10.adicionaAresta('8', 'C', 'H', 3)
        self.grafo_dir_10.adicionaAresta('9', 'I', 'B', 1)
        self.grafo_dir_10.adicionaAresta('10', 'I', 'J', 2)
        self.grafo_dir_10.adicionaAresta('11', 'G', 'L', 3)
        self.grafo_dir_10.adicionaAresta('12', 'G', 'F', 3)
        self.grafo_dir_10.adicionaAresta('13', 'F', 'J', 2)
        self.grafo_dir_10.adicionaAresta('14', 'F', 'K', 1)
        self.grafo_dir_10.adicionaAresta('15', 'E', 'M', 4)
        self.grafo_dir_10.adicionaAresta('16', 'J', 'E', 2)
        self.grafo_dir_10.adicionaAresta('17', 'J', 'N', 5)
        self.grafo_dir_10.adicionaAresta('18', 'K', 'O', 3)
        self.grafo_dir_10.adicionaAresta('19', 'L', 'P', 1)
        self.grafo_dir_10.adicionaAresta('20', 'M', 'Q', 3)
        self.grafo_dir_10.adicionaAresta('21', 'M', 'S', 4)
        self.grafo_dir_10.adicionaAresta('22', 'N', 'R', 7)
        self.grafo_dir_10.adicionaAresta('23', 'O', 'S', 1)
        self.grafo_dir_10.adicionaAresta('24', 'P', 'R', 5)
        self.grafo_dir_10.adicionaAresta('25', 'N', 'T', 1)
        self.grafo_dir_10.adicionaAresta('26', 'N', 'S', 3)
        self.grafo_dir_10.adicionaAresta('27', 'U', 'S', 1)
        self.grafo_dir_10.adicionaAresta('28', 'S', 'W', 7)
        self.grafo_dir_10.adicionaAresta('29', 'S', 'T', 1)
        self.grafo_dir_10.adicionaAresta('30', 'T', 'Q', 5)
        self.grafo_dir_10.adicionaAresta('31', 'T', 'X', 2)
        self.grafo_dir_10.adicionaAresta('32', 'Q', 'Y', 1)
        self.grafo_dir_10.adicionaAresta('33', 'Y', 'Z', 7)
        self.grafo_dir_10.adicionaAresta('34', 'Y', 'AA', 7)
        self.grafo_dir_10.adicionaAresta('35', 'X', 'AA', 1)
        self.grafo_dir_10.adicionaAresta('36', 'X', 'AB', 1)
        self.grafo_dir_10.adicionaAresta('37', 'X', 'U', 1)
        self.grafo_dir_10.adicionaAresta('38', 'AC', 'U', 2)
        self.grafo_dir_10.adicionaAresta('39', 'W', 'AC', 7)
        self.grafo_dir_10.adicionaAresta('40', 'W', 'AD', 3)
        self.grafo_dir_10.adicionaAresta('41', 'Z', 'AF', 2)
        self.grafo_dir_10.adicionaAresta('42', 'AF', 'AE', 1)
        self.grafo_dir_10.adicionaAresta('43', 'AC', 'AE', 5)
        self.grafo_dir_10.adicionaAresta('44', 'AE', 'AG', 3)
        self.grafo_dir_10.adicionaAresta('45', 'AE', 'V', 1)
        self.grafo_dir_10.adicionaAresta('46', 'D', 'I', 5)
        self.grafo_dir_10.adicionaAresta('47', 'F', 'I', 4)
        self.grafo_dir_10.adicionaAresta('48', 'R', 'S', 10)

        self.caminho_1 = ['A', '2', 'H', '6', 'F', '14', 'K', '18', 'O', '23', 'S', '29', 'T', '30', 'Q', '32', 'Y', '33', 'Z', '41', 'AF', '42', 'AE', '45', 'V']
        self.caminho_2 = ['A', '2', 'H', '6', 'F', '14', 'K', '18', 'O', '23', 'S', '28', 'W', '39', 'AC', '43', 'AE', '44', 'AG']
        self.caminho_3 = ['A', '2', 'H', '6', 'F', '14', 'K', '18', 'O', '23', 'S', '29', 'T', '30', 'Q', '32', 'Y', '33', 'Z', '41', 'AF', '42', 'AE', '44', 'AG']
        self.caminho_4 = ['A', '2', 'H', '6', 'F', '13', 'J', '16', 'E', '15', 'M', '20', 'Q', '32', 'Y', '33', 'Z', '41', 'AF', '42', 'AE', '44', 'AG']
        self.caminho_5 = ['D', '46', 'I', '9', 'B', '5', 'E', '15', 'M', '20', 'Q', '32', 'Y', '33', 'Z', '41', 'AF', '42', 'AE', '45', 'V']
        self.caminho_6 = ['D', '46', 'I', '10', 'J', '16', 'E', '15', 'M', '20', 'Q', '32', 'Y', '33', 'Z', '41', 'AF', '42', 'AE', '45', 'V']
        self.caminho_7 = ['C', '8', 'H', '6', 'F', '13', 'J', '16', 'E', '15', 'M', '20', 'Q', '32', 'Y', '33', 'Z', '41', 'AF', '42', 'AE', '45', 'V']
        self.caminho_8 = ['A', '1', 'B', '5', 'E', '15', 'M', '21', 'S', '29', 'T', '31', 'X', '36', 'AB']
        self.caminho_9 = ['B', '4', 'D', '46', 'I', '10', 'J', '17', 'N', '26', 'S', '28', 'W', '39', 'AC', '43', 'AE', '44', 'AG']
        self.caminho_10 = ['A', '2', 'H', '6', 'F', '14', 'K', '18', 'O', '23', 'S', '29', 'T', '31', 'X', '35', 'AA']
        self.caminho_11 = ['H', '6', 'F', '14', 'K', '18', 'O', '23', 'S', '28', 'W', '40', 'AD']

        # Grafos das matrizes curriculares:
        self.eng_comp = MeuGrafo(
            ["11", "12", "13", "14", "15", "16", "17", 
            "21", "22", "23", "24", "25", "26", "27",
            "31", "32", "33", "34", "35", "36",
            "41", "42", "43", "44", "45",
            "51", "52", "53", "54", "55",
            "61", "62", "63", "64", "65",
            "71", "72", "73", "74", "75",
            "81", "82", "83", "84", "85",
            "91", "92", "93", "94",
            "101", "102", "103"
            ])

        self.eng_comp.adicionaAresta("a1", "11", "21")
        self.eng_comp.adicionaAresta("a2", "14", "24")
        self.eng_comp.adicionaAresta("a3", "15", "24")
        self.eng_comp.adicionaAresta("a4", "14", "25")
        self.eng_comp.adicionaAresta("a5", "15", "25")
        self.eng_comp.adicionaAresta("a6", "16", "26")
        self.eng_comp.adicionaAresta("a7", '21', "31")
        self.eng_comp.adicionaAresta("a8", "24", "33")
        self.eng_comp.adicionaAresta("a9", "14", "34")
        self.eng_comp.adicionaAresta("b1", "15", "34")
        self.eng_comp.adicionaAresta("b2", "14", "35")
        self.eng_comp.adicionaAresta("b3", "15", "35")
        self.eng_comp.adicionaAresta("b4", "26", "36")
        self.eng_comp.adicionaAresta("b5", "21", "41")
        self.eng_comp.adicionaAresta("b6", "24", "43")
        self.eng_comp.adicionaAresta("b7", "24", "44")
        self.eng_comp.adicionaAresta("b8", "36", "44")
        self.eng_comp.adicionaAresta("b9", "36", "45")
        self.eng_comp.adicionaAresta("c1", "31", "51")
        self.eng_comp.adicionaAresta("c2", "31", "52")
        self.eng_comp.adicionaAresta("c3", "24", "53")
        self.eng_comp.adicionaAresta("c4", "24", '54')
        self.eng_comp.adicionaAresta("c5", "36", "55")
        self.eng_comp.adicionaAresta("c6", "44", "55")
        self.eng_comp.adicionaAresta("c7", "51", "61")
        self.eng_comp.adicionaAresta("c8", "43", "62")
        self.eng_comp.adicionaAresta("c9", "34", "63")
        self.eng_comp.adicionaAresta("d1", "35", "63")
        self.eng_comp.adicionaAresta("d2", "31", "64")
        self.eng_comp.adicionaAresta("d3", "55", "65")
        self.eng_comp.adicionaAresta("d4", "24", "72")
        self.eng_comp.adicionaAresta("d5", "63", "73")
        self.eng_comp.adicionaAresta("d6", "52", "75")
        self.eng_comp.adicionaAresta("d7", "64", "75")
        self.eng_comp.adicionaAresta("d8", "34", "81")
        self.eng_comp.adicionaAresta("d9", "35", "81")
        self.eng_comp.adicionaAresta("e1", "54", "81")
        self.eng_comp.adicionaAresta("e2", "73", "82")
        self.eng_comp.adicionaAresta("e3", "74", "83")
        self.eng_comp.adicionaAresta("e4", "61", "84")
        self.eng_comp.adicionaAresta("e5", "64", "84")
        self.eng_comp.adicionaAresta("e6", "75", "85")
        self.eng_comp.adicionaAresta("e7", "83", "92")
        self.eng_comp.adicionaAresta("e8", "44", "93")
        self.eng_comp.adicionaAresta("e9", "45", "93")
        self.eng_comp.adicionaAresta("f1", "61", "94")
        self.eng_comp.adicionaAresta("f2", "75", "94")
        self.eng_comp.adicionaAresta("f3", "92", "103")

        self.const_ed = MeuGrafo(
            ["11", "12", "13", "14", "15", "16", "17", "18", 
            "21", "22", "23", "24", "25", "26", "27",
            "31", "32", "33", "34", "35", "36", "37", "38",
            "41", "42", "43", "44", "45", "46", "47",
            "51", "52", "53", "54", "55", "56", "57", "58",
            "61", "62", "63", "64", "65", "66", "67", "68",
            "71", "72", "73"
            ])

        self.const_ed.adicionaAresta("a1", "15", "21")
        self.const_ed.adicionaAresta("a2", "14", "23")
        self.const_ed.adicionaAresta("a3", "11", "24")
        self.const_ed.adicionaAresta("a4", "17", "24")
        self.const_ed.adicionaAresta("a5", "15", "25")
        self.const_ed.adicionaAresta("a6", "17", "26")
        self.const_ed.adicionaAresta("a7", '17', "27")
        self.const_ed.adicionaAresta("a8", "15", "32")
        self.const_ed.adicionaAresta("a9", "21", "32")
        self.const_ed.adicionaAresta("b1", "21", "33")
        self.const_ed.adicionaAresta("b2", "25", "33")
        self.const_ed.adicionaAresta("b3", "15", "34")
        self.const_ed.adicionaAresta("b4", "11", "35")
        self.const_ed.adicionaAresta("b5", "27", "35")
        self.const_ed.adicionaAresta("b6", "26", "36")
        self.const_ed.adicionaAresta("b7", "23", "37")
        self.const_ed.adicionaAresta("b8", "24", "38")
        self.const_ed.adicionaAresta("b9", "17", "41")
        self.const_ed.adicionaAresta("c1", "21", "41")
        self.const_ed.adicionaAresta("c2", "17", "42")
        self.const_ed.adicionaAresta("c3", "21", "42")
        self.const_ed.adicionaAresta("c4", "23", '43')
        self.const_ed.adicionaAresta("c5", "24", "44")
        self.const_ed.adicionaAresta("c6", "36", "45")
        self.const_ed.adicionaAresta("c7", "37", "45")
        self.const_ed.adicionaAresta("c8", "17", "46")
        self.const_ed.adicionaAresta("c9", "32", "46")
        self.const_ed.adicionaAresta("d1", "11", "47")
        self.const_ed.adicionaAresta("d2", "37", "47")
        self.const_ed.adicionaAresta("d3", "37", "51")
        self.const_ed.adicionaAresta("d4", "43", "51")
        self.const_ed.adicionaAresta("d5", "45", "51")
        self.const_ed.adicionaAresta("d6", "46", "51")
        self.const_ed.adicionaAresta("d7", "41", "52")
        self.const_ed.adicionaAresta("d8", "42", "52")
        self.const_ed.adicionaAresta("d9", "45", "52")
        self.const_ed.adicionaAresta("e1", "46", "52")
        self.const_ed.adicionaAresta("e2", "17", "53")
        self.const_ed.adicionaAresta("e3", "32", "53")
        self.const_ed.adicionaAresta("e4", "47", "54")
        self.const_ed.adicionaAresta("e5", "17", "55")
        self.const_ed.adicionaAresta("e6", "32", "55")
        self.const_ed.adicionaAresta("e7", "46", "56")
        self.const_ed.adicionaAresta("e8", "43", "57")
        self.const_ed.adicionaAresta("e9", "31", "62")
        self.const_ed.adicionaAresta("f1", "44", "62")
        self.const_ed.adicionaAresta("f2", "22", "64")
        self.const_ed.adicionaAresta("f3", "27", "64")
        self.const_ed.adicionaAresta("f4", "33", "64")
        self.const_ed.adicionaAresta("f5", "36", "64")
        self.const_ed.adicionaAresta("f6", "47", "65")
        self.const_ed.adicionaAresta("f7", "22", "66")
        self.const_ed.adicionaAresta("f8", "31", "67")

        self.fisica = MeuGrafo(
            ["11", "12", "13", "14", "15", "16", "17", 
            "21", "22", "23", "24", "25", "26", "27",
            "31", "32", "33", "34", "35", "36", "37",
            "41", "42", "43", "44", "45", "46",
            "51", "52", "53", "54", "55", "56",
            "61", "62", "63", "64", "65", "66",
            "71", "72", "73", "74", "75",
            "81", "82", "83", "84", "85", "86"
            ])

        self.fisica.adicionaAresta("a1", "11", "21")
        self.fisica.adicionaAresta("a2", "12", "21")
        self.fisica.adicionaAresta("a3", "11", "22")
        self.fisica.adicionaAresta("a4", "12", "22")
        self.fisica.adicionaAresta("a5", "12", "23")
        self.fisica.adicionaAresta("a6", "12", "24")
        self.fisica.adicionaAresta("a7", '14', "24")
        self.fisica.adicionaAresta("a8", "15", "25")
        self.fisica.adicionaAresta("a9", "21", "31")
        self.fisica.adicionaAresta("b1", "23", "31")
        self.fisica.adicionaAresta("b2", "21", "32")
        self.fisica.adicionaAresta("b3", "22", "32")
        self.fisica.adicionaAresta("b4", "23", "33")
        self.fisica.adicionaAresta("b5", "31", "41")
        self.fisica.adicionaAresta("b6", "31", "42")
        self.fisica.adicionaAresta("b7", "32", "42")
        self.fisica.adicionaAresta("b8", "33", "45")
        self.fisica.adicionaAresta("b9", "31", "46")
        self.fisica.adicionaAresta("c1", "41", "51")
        self.fisica.adicionaAresta("c2", "45", "51")
        self.fisica.adicionaAresta("c3", "41", "52")
        self.fisica.adicionaAresta("c4", "42", '52')
        self.fisica.adicionaAresta("c5", "45", "53")
        self.fisica.adicionaAresta("c6", "31", "54")
        self.fisica.adicionaAresta("c7", "43", "55")
        self.fisica.adicionaAresta("c8", "51", "61")
        self.fisica.adicionaAresta("c9", "51", "62")
        self.fisica.adicionaAresta("d1", "52", "62")
        self.fisica.adicionaAresta("d2", "21", "63")
        self.fisica.adicionaAresta("d3", "53", "63")
        self.fisica.adicionaAresta("d4", "51", "64")
        self.fisica.adicionaAresta("d5", "56", "66")
        self.fisica.adicionaAresta("d6", "61", "71")
        self.fisica.adicionaAresta("d7", "41", "72")
        self.fisica.adicionaAresta("d8", "45", "72")
        self.fisica.adicionaAresta("d9", "66", "73")
        self.fisica.adicionaAresta("e1", "31", "74")
        self.fisica.adicionaAresta("e2", "43", "74")
        self.fisica.adicionaAresta("e3", "65", "81")
        self.fisica.adicionaAresta("e4", "74", "82")
        self.fisica.adicionaAresta("e5", "73", "83")
        self.fisica.adicionaAresta("e6", "54", "84")
        self.fisica.adicionaAresta("e7", "71", "84")
        self.fisica.adicionaAresta("e8", "16", "85")
        self.fisica.adicionaAresta("e9", "25", "85")

        self.letras = MeuGrafo(
            ["11", "12", "13", "14", "15", "16", "17", 
            "21", "22", "23", "24", "25", "26", "27",
            "31", "32", "33", "34", "35", "36", "37",
            "41", "42", "43", "44", "45", "46", "47",
            "51", "52", "53", "54", "55", "56", "57",
            "61", "62", "63", "64", "65", "66", "67", "68",
            "71", "72", "73", "74", "75", "76", "77", "78",
            "81", "82", "83", "84", "85", "86", "87", "88"
            ])

        self.letras.adicionaAresta("a1", "11", "21")
        self.letras.adicionaAresta("a2", "11", "22")
        self.letras.adicionaAresta("a3", "12", "23")
        self.letras.adicionaAresta("a4", "12", "25")
        self.letras.adicionaAresta("a5", "17", "26")
        self.letras.adicionaAresta("a6", "21", "31")
        self.letras.adicionaAresta("a7", '21', "32")
        self.letras.adicionaAresta("a8", "21", "33")
        self.letras.adicionaAresta("a9", "24", "34")
        self.letras.adicionaAresta("b1", "25", "35")
        self.letras.adicionaAresta("b2", "31", "41")
        self.letras.adicionaAresta("b3", "33", "42")
        self.letras.adicionaAresta("b4", "25", "43")
        self.letras.adicionaAresta("b5", "25", "44")
        self.letras.adicionaAresta("b6", "36", "44")
        self.letras.adicionaAresta("b7", "23", "46")
        self.letras.adicionaAresta("b8", "35", "46")
        self.letras.adicionaAresta("b9", "37", "47")
        self.letras.adicionaAresta("c1", "31", "51")
        self.letras.adicionaAresta("c2", "35", "52")
        self.letras.adicionaAresta("c3", "13", "53")
        self.letras.adicionaAresta("c4", "45", '54')
        self.letras.adicionaAresta("c5", "35", "55")
        self.letras.adicionaAresta("c6", "22", "56")
        self.letras.adicionaAresta("c7", "37", "57")
        self.letras.adicionaAresta("c8", "31", "61")
        self.letras.adicionaAresta("c9", "31", "62")
        self.letras.adicionaAresta("d1", "35", "63")
        self.letras.adicionaAresta("d2", "54", "64")
        self.letras.adicionaAresta("d3", "37", "67")
        self.letras.adicionaAresta("d4", "54", "68")
        self.letras.adicionaAresta("d5", "64", "78")
        self.letras.adicionaAresta("d6", "68", "78")
        self.letras.adicionaAresta("d7", "27", "77")
        self.letras.adicionaAresta("d8", "53", "77")
        self.letras.adicionaAresta("d9", "45", "76")
        self.letras.adicionaAresta("e1", "35", "75")
        self.letras.adicionaAresta("e2", "64", "74")
        self.letras.adicionaAresta("e3", "31", "73")
        self.letras.adicionaAresta("e4", "31", "72")
        self.letras.adicionaAresta("e5", "31", "71")
        self.letras.adicionaAresta("e6", "17", "83")
        self.letras.adicionaAresta("e7", "74", "84")
        self.letras.adicionaAresta("e8", "77", "87")
        self.letras.adicionaAresta("e9", "74", "88")
        self.letras.adicionaAresta("f1", "78", "88")

        self.matematica = MeuGrafo(
            ["11", "12", "13", "14", "15", "16",
            "21", "22", "23", "24", "25",
            "31", "32", "33", "34", "35", "36",
            "41", "42", "43", "44", "45", "46", "47",
            "51", "52", "53", "54", "55", "56", "57",
            "61", "62", "63", "64", "65", "66", "67",
            "71", "72", "73", "74", "75", "76", "77", 
            ])

        self.matematica.adicionaAresta("a1", "12", "21")
        self.matematica.adicionaAresta("a2", "13", "21")
        self.matematica.adicionaAresta("a3", "13", "23")
        self.matematica.adicionaAresta("a4", "21", "31")
        self.matematica.adicionaAresta("a5", "21", "32")
        self.matematica.adicionaAresta("a6", "22", "32")
        self.matematica.adicionaAresta("a7", '23', "33")
        self.matematica.adicionaAresta("a8", "24", "34")
        self.matematica.adicionaAresta("a9", "25", "35")
        self.matematica.adicionaAresta("b1", "16", "36")
        self.matematica.adicionaAresta("b2", "31", "41")
        self.matematica.adicionaAresta("b3", "32", "42")
        self.matematica.adicionaAresta("b4", "34", "44")
        self.matematica.adicionaAresta("b5", "36", "45")
        self.matematica.adicionaAresta("b6", "22", "52")
        self.matematica.adicionaAresta("b7", "21", "53")
        self.matematica.adicionaAresta("b8", "33", "53")
        self.matematica.adicionaAresta("b9", "45", "55")
        self.matematica.adicionaAresta("c1", "46", "56")
        self.matematica.adicionaAresta("c2", "47", "57")
        self.matematica.adicionaAresta("c3", "51", "61")
        self.matematica.adicionaAresta("c4", "41", '62')
        self.matematica.adicionaAresta("c5", "56", "64")
        self.matematica.adicionaAresta("c6", "55", "65")
        self.matematica.adicionaAresta("c7", "57", "67")
        self.matematica.adicionaAresta("c8", "41", "71")
        self.matematica.adicionaAresta("c9", "41", "72")
        self.matematica.adicionaAresta("d1", "56", "73")
        self.matematica.adicionaAresta("d2", "64", "73")
        self.matematica.adicionaAresta("d3", "64", "74")
        self.matematica.adicionaAresta("d4", "65", "75")
        self.matematica.adicionaAresta("d5", "67", "77")

        self.telematica = MeuGrafo(
        ["11", "12", "13", "14", "15", "16", "17",
        "21", "22", "23", "24", "25", "26", "27",
        "31", "32", "33", "34", "35", "36", "37",
        "41", "42", "43", "44", "45", "46", "47",
        "51", "52", "53", "54", "55", "56", "57",
        "61", "62", "63", "64", "65", "66"
        ])

        self.telematica.adicionaAresta("a1", "11", "21")
        self.telematica.adicionaAresta("a2", "12", "22")
        self.telematica.adicionaAresta("a3", "16", "22")
        self.telematica.adicionaAresta("a4", "12", "23")
        self.telematica.adicionaAresta("a5", "16", "23")
        self.telematica.adicionaAresta("a6", "13", "24")
        self.telematica.adicionaAresta("a7", '16', "26")
        self.telematica.adicionaAresta("a8", "21", "31")
        self.telematica.adicionaAresta("a9", "26", "32")
        self.telematica.adicionaAresta("b1", "22", "33")
        self.telematica.adicionaAresta("b2", "23", "33")
        self.telematica.adicionaAresta("b3", "26", "33")
        self.telematica.adicionaAresta("b4", "14", "34")
        self.telematica.adicionaAresta("b5", "25", "35")
        self.telematica.adicionaAresta("b6", "21", "36")
        self.telematica.adicionaAresta("b7", "24", "36")
        self.telematica.adicionaAresta("b8", "31", "41")
        self.telematica.adicionaAresta("b9", "31", "42")
        self.telematica.adicionaAresta("c1", "32", "43")
        self.telematica.adicionaAresta("c2", "32", "44")
        self.telematica.adicionaAresta("c3", "33", "44")
        self.telematica.adicionaAresta("c4", "33", '45')
        self.telematica.adicionaAresta("c5", "21", "46")
        self.telematica.adicionaAresta("c6", "34", "46")
        self.telematica.adicionaAresta("c7", "41", "51")
        self.telematica.adicionaAresta("c8", "41", "52")
        self.telematica.adicionaAresta("c9", "44", "53")
        self.telematica.adicionaAresta("d1", "44", "54")
        self.telematica.adicionaAresta("d2", "37", "55")
        self.telematica.adicionaAresta("d3", "41", "55")
        self.telematica.adicionaAresta("d4", "44", "55")
        self.telematica.adicionaAresta("d5", "42", "61")
        self.telematica.adicionaAresta("d6", "51", "61")
        self.telematica.adicionaAresta("d7", "53", "62")

        # Resultado da ordenação topológica
        self.eng_comp_ord_top = [
            '11', '12', '13', '14', '15', '16', '17', '22', '23', '27', '32', '42', '71', '74', 
            '91', '101', '102', '21', '24', '25', '26', '34', '35', '83', '31', '33', '36', '41', 
            '43', '53', '54', '63', '72', '92', '44', '45', '51', '52', '62', '64', '73', '81', '103', 
            '55', '61', '75', '82', '93', '65', '84', '85', '94']

        self.const_ed_ord_top = [
            '11', '12', '13', '14', '15', '16', '17', '18', '22', '31', '58', '61', '63', '68', 
            '71', '72', '73', '21', '23', '24', '25', '26', '27', '34', '66', '67', '32', '33', '35', 
            '36', '37', '38', '41', '42', '43', '44', '45', '46', '47', '53', '55', '57', '62', '64', 
            '51', '52', '54', '56', '65']

        self.fisica_ord_top = [
            '11', '12', '13', '14', '15', '16', '17', '26', '27', '34', '35', '36', '37', '43', '44', '56', 
            '65', '75', '86', '21', '22', '23', '24', '25', '55', '66', '81', '31', '32', '33', '73', '85', 
            '41', '42', '45', '46', '54', '74', '83', '51', '52', '53', '72', '82', '61', '62', '63', '64', 
            '71', '84']
        
        self.letras_ord_top = [
            '11', '12', '13', '14', '15', '16', '17', '24', '27', '36', '37', '45', '65', '66', '81', '82', 
            '85', '86', '21', '22', '23', '25', '26', '34', '47', '53', '54', '57', '67', '76', '83', '31', 
            '32', '33', '35', '43', '44', '56', '64', '68', '77', '41', '42', '46', '51', '52', '55', '61', 
            '62', '63', '71', '72', '73', '74', '75', '78', '87', '84', '88']
        
        self.matematica_ord_top = [
            '11', '12', '13', '14', '15', '16', '22', '24', '25', '43', '46', '47', '51', '54', '63', '66', 
            '76', '21', '23', '34', '35', '36', '52', '56', '57', '61', '31', '32', '33', '44', '45', '64', 
            '67', '41', '42', '53', '55', '73', '74', '77', '62', '65', '71', '72', '75']

        self.telematica_ord_top = [
            '11', '12', '13', '14', '15', '16', '17', '25', '27', '37', '47', '56', '57', '63', '64', '65', 
            '66', '21', '22', '23', '24', '26', '34', '35', '31', '32', '33', '36', '46', '41', '42', '43', 
            '44', '45', '51', '52', '53', '54', '55', '61', '62']

    def test_warshall(self):
        self.assertEqual(self.grafo_dir_1.warshall(), [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]])
        self.assertEqual(self.grafo_dir_2.warshall(), [[1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 1]])
        self.assertEqual(self.grafo_dir_3.warshall(), [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0]])
        self.assertEqual(self.grafo_dir_4.warshall(), [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(self.grafo_dir_5.warshall(), [[0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0]])
        self.assertEqual(self.grafo_dir_6.warshall(), [[0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(self.grafo_dir_7.warshall(), [[0, 1, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1]])
        self.assertEqual(self.grafo_dir_8.warshall(), [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(self.grafo_dir_9.warshall(), [[0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
        self.assertEqual(self.u.warshall(), [[0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]])

    def test_dijkstra(self):
        self.assertEqual(self.grafo_dir_10.dijkstra('A', 'V', 7, 9, {'S', 'Y', 'AF', 'L', 'R'}), self.caminho_1)
        self.assertEqual(self.grafo_dir_10.dijkstra('A', 'AG', 10, 15, {'E', 'M', 'W', 'N', 'S'}), self.caminho_2)
        self.assertEqual(self.grafo_dir_10.dijkstra('A', 'AG', 8, 13, {'E', 'W', 'N', 'Y', 'K'}), self.caminho_3)
        self.assertEqual(self.grafo_dir_10.dijkstra('A', 'AG', 10, 15, {'M', 'R', 'AE'}), self.caminho_4)
        self.assertEqual(self.grafo_dir_10.dijkstra('D', 'V', 7, 11, {'B', 'Z', 'R', 'X', 'N', 'Q', 'E'}), self.caminho_5)
        self.assertEqual(self.grafo_dir_10.dijkstra('D', 'V', 7, 11, {'B', 'Z', 'R', 'X', 'Q', 'J'}), self.caminho_6)
        self.assertEqual(self.grafo_dir_10.dijkstra('C', 'V', 3, 10, {'H', 'G', 'B', 'E', 'Q', 'Z', 'AC', 'W', 'M', 'Y'}), self.caminho_7)
        self.assertEqual(self.grafo_dir_10.dijkstra('A', 'AB', 3, 7, {'B', 'C', 'E', 'M', 'P', 'S', 'W', 'AC'}), self.caminho_8)
        self.assertEqual(self.grafo_dir_10.dijkstra('B', 'AG', 12, 12, {'J', 'R', 'S', 'Y', 'U', 'W', 'AE'}), self.caminho_9)
        self.assertEqual(self.grafo_dir_10.dijkstra('B', 'AG', 11, 12, {'J', 'W', 'AC', 'R', 'N'}), self.caminho_9)
        self.assertEqual(self.grafo_dir_10.dijkstra('A', 'AA', 4, 10, {'F', 'E', 'M', 'Y'}), self.caminho_10)
        self.assertEqual(self.grafo_dir_10.dijkstra('H', 'AD', 6, 10, {'B', 'M', 'R', 'S'}), self.caminho_11)
        self.assertEqual(self.grafo_dir_10.dijkstra('A', 'AD', 5, 7, {'W', 'F', 'R', 'M'}), False)
        self.assertEqual(self.grafo_dir_10.dijkstra('A', 'A', 10, 20, {'A', 'D', 'I', 'K'}), False)
        self.assertEqual(self.grafo_dir_10.dijkstra('A', 'D', -10, 10, {'Q', 'R', 'B'}), False)
        self.assertEqual(self.grafo_dir_10.dijkstra('AD', 'AG', 10, 15, {'W', 'AC', 'AE'}), False)

    def test_topological_sorting(self):
        self.assertEqual(self.eng_comp.khan_algorithm(), self.eng_comp_ord_top)
        self.assertEqual(self.const_ed.khan_algorithm(), self.const_ed_ord_top)
        self.assertEqual(self.fisica.khan_algorithm(), self.fisica_ord_top)
        self.assertEqual(self.letras.khan_algorithm(), self.letras_ord_top)
        self.assertEqual(self.matematica.khan_algorithm(), self.matematica_ord_top)
        self.assertEqual(self.telematica.khan_algorithm(), self.telematica_ord_top)