def minimum_length_slice(first_string, second_string):

    a, b, c = first_string[0], first_string[1], first_string[2]
    i1 = second_string.find(a)
    i2 = second_string.find(b)
    i3 = second_string.find(c)

    f1 = min(i1, i2, i3)
    f2 = max(i1, i2, i3)

    return second_string[f1 : f2 + 1]