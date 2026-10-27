def treatment_sum(our_tuple: tuple):
    if len(our_tuple) > 2:
        raise Exception('Много данных')

    try:
        if len(our_tuple) < 2:
            raise IndexError

        return our_tuple[0] + our_tuple[1]

    except IndexError:
        return 'Недостаточно данных'

    except TypeError:
        return 'Нельзя сложить эти данные'