class PublicTransport:
    def __init__(self, brand, engine_power, year, color, max_speed):
        self.brand = brand
        self._engine_power = engine_power
        self.year = year
        self.color = color
        self.max_speed = max_speed
        pass

    @property
    def info(self):
        print(f"Марка: {self.brand}, Цвет: {self.color}, Год: {self.year}, Мощность: {self._engine_power}")
        return


class Bus(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, passengers, park, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.passengers = passengers
        self.__park = park
        self._fare = fare

    @property
    def park(self):
        return self.__park

    @park.setter
    def park(self, new_park):
        assert 1000 <= new_park <= 9999, "Ошибка: номер парка должен быть от 1000 до 9999"
        self.__park = new_park


class Tram(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.__route = route
        self.path = path
        self._fare = fare

    @property
    def how_long(self):
        long = self.max_speed / (4 * self.path)
        return long
