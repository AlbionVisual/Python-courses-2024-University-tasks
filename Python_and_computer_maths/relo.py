import numpy as np

def regular_polygon_Relo(n = 3, center = np.array([0,0]), r = 1, N = 100):
    """Функция создающая координаты точек составляющих стороны многоугольника Рёло в зависимости от кол-ва сторон, точки начала, ширины фигуры и кол-ва точек на сторону

    Arguments:

    n: кол-во сторон многоугольника (n - нечётное). По умолчанию 3

    center: массив состоящий из двух чисел показывающих положения точки центра фигуры. По умолчанию np.array([0,0])

    r: ширина многоугольника Рёло. По умолчанию 1

    N: кол-во точек на одну сторону. По умолчанию 100

    Return: матрица. Массив состоящий из массивов двух чисел
    """

    assert n % 2 != 0, 'Кол-во сторон должно быть нечётным'
    assert n > 2, 'Кол-во сторон больше двух'
    assert r > 0, 'Ширина должна быть положительной'
    assert N >= 0, 'Кол-во точек N на сторону неотрицательно'
    
    alpha = 360 / n / 180 * np.pi
    beta = alpha / 2
    l = np.sqrt(2 * r**2 * (1 - np.cos(np.pi / n)))
    R = l / (2 * np.sin(np.pi / n))
    t = np.arange(0,2*np.pi,2*np.pi/n)
    vertices = center + R*np.transpose([np.cos(t), np.sin(t)])
    angle = np.linspace(-beta/2, beta/2, N)
    list_sides = [vertices[i] +
                  r*np.transpose([np.cos(angle + np.pi + i*alpha),
                                  np.sin(angle + np.pi + i*alpha)])
                  for i in range(n)]
    sides = np.concatenate(list_sides)
    
    return sides
