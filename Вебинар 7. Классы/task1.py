class Segment:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def length(self):
        x1, y1 = self.first_point
        x2, y2 = self.second_point
        result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return round(result, 2)

    def x_axis_intersection(self):
        y1 = self.first_point[1]
        y2 = self.second_point[1]
        if y1 * y2 <= 0:
            return True
        else:
            return False

    def y_axis_intersection(self):
        x1 = self.first_point[0]
        x2 = self.second_point[0]
        if x1 * x2 <= 0:
            return True
        else:
            return False
