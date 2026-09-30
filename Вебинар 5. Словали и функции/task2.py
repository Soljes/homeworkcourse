def repeats(our_str):
    """Повторы букв
    :param our_str: строка
    :return: новая строка с повторами букв
    """
    # todo Здесь нужно написать код
    counts_dict = {}
    result_str = ""
    for char in our_str:
        if char in counts_dict:
            counts_dict[char] += 1
        else:
            counts_dict[char] = 1
        result_str += f"{char}_{counts_dict[char]}"
    return result_str

