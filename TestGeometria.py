import unittest

#Importamos las clases entrando en las carpetas que estan ubicadas y las renombramos para tener menos código
from Reto_05.model.Geometria import Geometria as g
from Reto_05.view.View import View as v

class TestGeometria(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass() - OK')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass() - OK')

    def setUp(self):
        print('setUp - OK')
        global object_test
        #Preparamos variables para pasar valores a las funciones y testearlas
        self.r = []
        self.a = [1, 2, 3, 4, 5, 6, 7, 8]
        self.b = [8, 7, 6, 5, 4, 3, 2, 1]
        object_test = g(2,3,4)

    def test_areaCuadrado(self):
        # Ejecutamos la función a testear con la tabla de valores que deseamos y guardamos los resultados que nos devuelve en la tabla "r"
        self.r = [g.areaCuadrado(self, n) for n in self.a]
        # Comparamos los resultados obtenidos y los esperados
        self.assertEqual(self.r, [1, 4, 9, 16, 25, 36, 49, 64])
        print("test_areaCuadrado() -> OK")

    def test_areaCirculo(self):
        # Ejecutamos la función a testear con la tabla de valores que deseamos y guardamos los resultados que nos devuelve en la tabla result
        for n in self.a:
            result = g.areaCirculo(self,n) # Ejecutamos la función con las variables de nuestra tabla y guardamos el resultado en la variable "result"
            result = round(result,4) # Limitamos a cuatro decimales el resultado
            self.r.append(result) # Cargamos el resultado a nuesta tabla de resultados "r"
        # Comparamos los resultados obtenidos y los esperados
        self.assertEqual(self.r, [3.1416, 12.5664, 28.2744, 50.2656, 78.540, 113.0976, 153.9384, 201.0624])
        print("test_areaCirculo() -> OK")

    def test_areaTriangulo(self):
        # Ejecutamos la función a testear con la tabla de valores que deseamos y guardamos los resultados que nos devuelve en la tabla "r"
        for valor_a, valor_b in zip(self.a, self.b):
            self.r.append(g.areaTriangulo(self, valor_a, valor_b))
            # Comparamos los resultados obtenidos y los esperados
        self.assertEqual(self.r, [4, 7, 9, 10, 10, 9, 7, 4])
        print("test_areaTriangulo() -> OK")

    def test_areaRectangulo(self):
        # Ejecutamos la función a testear con la tabla de valores que deseamos y guardamos los resultados que nos devuelve en la tabla "r"
        for valor_a, valor_b in zip(self.a, self.b):
            self.r.append(g.areaRectangulo(self, valor_a, valor_b))
        # Comparamos los resultados obtenidos y los esperados
        self.assertEqual(self.r, [8, 14, 18, 20, 20, 18, 14, 8])
        print("test_areaRectangulo() -> OK")

    def test_areaPentagono(self):
        # Ejecutamos la función a testear con la tabla de valores que deseamos y guardamos los resultados que nos devuelve en la tabla "r"
        for valor_a, valor_b in zip(self.a, self.b):
            self.r.append(g.areaPentagono(self, valor_a, valor_b))
        # Comparamos los resultados obtenidos y los esperados
        self.assertEqual(self.r, [4, 7, 9, 10, 10, 9, 7, 4])
        print("test_areaPentagono() -> OK")

    def test_areaRombo(self):
        # Ejecutamos la función a testear con la tabla de valores que deseamos y guardamos los resultados que nos devuelve en la tabla "r"
        for valor_a, valor_b in zip(self.a, self.b):
            self.r.append(g.areaRombo(self, valor_a, valor_b))
        # Comparamos los resultados obtenidos y los esperados
        self.assertEqual(self.r, [4, 7, 9, 10, 10, 9, 7, 4])
        print("test_areaRombo() -> OK")

    def test_areaRomboide(self):
        # Ejecutamos la función a testear con la tabla de valores que deseamos y guardamos los resultados que nos devuelve en la tabla "r"
        for valor_a, valor_b in zip(self.a, self.b):
            self.r.append(g.areaRomboide(self, valor_a, valor_b))
        # Comparamos los resultados obtenidos y los esperados
        self.assertEqual(self.r, [8, 14, 18, 20, 20, 18, 14, 8])
        print("test_areaRomboide() -> OK")

    def test_areaTrapecio(self):
        # Ejecutamos la función a testear con la tabla de valores que deseamos y guardamos los resultados que nos devuelve en la tabla "r"
        for valor_a, valor_b, valor_c in zip(self.a, self.a, self.b):
            self.r.append(g.areaTrapecio(self, valor_a, valor_b, valor_c))
        # Comparamos los resultados obtenidos y los esperados
        self.assertEqual(self.r, [8, 14, 18, 20, 20, 18, 14, 8])
        print("test_areaTrapecio() -> OK")

    def test_set_figuraName(self):
        # Ejecutamos la función a testear con el objeto creado previamente y guardamos los resultados de los casos que nos devuelve en la tabla "r"
        for n in self.a:
            object_test.set_figuraName(n)
            self.r.append(object_test.figuraName)
        # Comparamos los resultados obtenidos y los esperados
        self.assertEqual(self.r, ["Cuadrado","Circulo","Triangulo","Rectangulo","Pentagono","Rombo","Romboide","Trapecio"])
        print("test_set_figuraName() -> OK")

    def test_switch(self):
        # Ejecutamos la función a testear con el objeto creado previamente y guardamos los resultados de todas sus funciones (cálculo de areas) que nos devuelve en la tabla "r"
        for n in self.a:
            result = object_test.switch(n)
            self.r.append(result)
        # Comparamos los resultados obtenidos y los esperados
        self.assertEqual(self.r, [4, 12.5664, 3, 6, 3, 3, 6, 10])
        print("test_swtich() -> OK")

    def test_select(self):
        # Ejecutamos la función a testear con el objeto creado previamente y guardamos los resultados de todas sus funciones (cálculo de areas) que nos devuelve en la tabla "r"
        for n in self.a:
            v.case = n
            object_test.set_figuraName(v.case)
            self.r.append(object_test.switch(v.case))
        # Comparamos los resultados obtenidos y los esperados
        self.assertEqual(self.r, [4, 12.5664, 3, 6, 3, 3, 6, 10])
        print("test_select() -> OK")

    def tearDown(self):
        print('tearDown - OK')
        # Borramos las variables
        del self.a
        del self.b
        del self.r

if __name__ == '__main__':
    unittest.main()