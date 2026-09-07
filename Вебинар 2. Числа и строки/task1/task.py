def square_calculation(a):
    perimeter = a * 4
    square = a ** 2
    square = round(square, 2)
    diagonal = a * (2 ** 0.5)
    diagonal = round(diagonal, 2)
    return perimeter, square, diagonal
