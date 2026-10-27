def segment(first_point, second_point):

    try:
        x1, y1 = first_point
        x2, y2 = second_point
        totalsum = x1 + y1 + x2 + y2

    except Exception as err:
        err_text = str(err)
        return err_text[::-1]

    else:
        return totalsum
