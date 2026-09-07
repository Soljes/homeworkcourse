def string_concatenation(str1, str2):
    """Объединение строк
    :param str1: первая строка
    :param str2: вторая строка
    :return: преобразованную строку
    """

    # todo Здесь нужно написать код
    s1 = str1[:2]
    s2 = str2[:2]
    z1 = str1[2:]
    z2 = str2[2:]
    new_string1 = s2 + z1
    new_string2 = s1 + z2
    return new_string1 + " " + new_string2
