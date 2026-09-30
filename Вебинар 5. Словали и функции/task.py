def letter_stat(our_str):
    """Буквенная статистика
    :param our_str: строка
    :return: словарь со статистикой по буквам
    """
    letters_dict = {item: our_str.count(item) for item in our_str}
    return letters_dict

