class Trigon:
    def __init__(self, *args):
        if len(args) != 3:
            raise IndexError(f'Передано {len(args)} аргументов, а ожидается 3')

        a, b, c = args

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            raise TypeError('Стороны должны быть числами')

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('Стороны должны быть положительными')

        if a >= b + c or b >= a + c or c >= a + b:
            raise Exception('Не треугольник')

        pass
        # todo Здесь нужно написать код
