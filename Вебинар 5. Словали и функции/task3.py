def everything_for_your_cat(cats_data):
    """Котики и их владельцы
    :param cats_data: информация о котах и их владельцах
    :return: информация о котах и их владельцах в виде строки
    """
    # todo Здесь нужно написать код
    owners_dict = {}
    for cat_name, cat_age, first_name, last_name in cats_data:
        pols = f"{first_name} {last_name}"
        if pols not in owners_dict:
            owners_dict[pols] = [f"{cat_name}, {cat_age}"]
        else:
            owners_dict[pols].append(f"{cat_name}, {cat_age}")
    result = ""
    for owner, cats_list in owners_dict.items():
        all_cats = "; ".join(cats_list)
        result += f"{owner}: {all_cats}\n"
    return result
