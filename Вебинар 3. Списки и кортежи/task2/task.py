def get_list_info(lst):
    """Получение информации о списке
    :param lst: список из чисел
    :return: min_elem, max_elem, sum_list, average
    """
    # todo Здесь нужно написать код
    min_elem = min(lst)
    max_elem = max(lst)
    sum_list = lst[0] + lst[1] + lst[2] + lst[3] + lst[4] + lst[5] + lst[6]
    average = round(sum_list / len(lst), 2)
    return min_elem, max_elem, sum_list, average