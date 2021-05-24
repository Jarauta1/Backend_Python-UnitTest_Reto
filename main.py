from Reto_05.model.Geometria import Geometria
from Reto_05.view.View import View

if __name__ == '__main__':
    g = Geometria(2.00, 3.10, 4.00)
    v = View()
    v.select(g)
