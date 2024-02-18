if __name__ == "__main__":
    class Liquid:
        """ Базовый класс жидкости. """

        def __init__(self, temperature: float, density: float):
            """
            Создание и подготовка к работе объекта "Жидкость"

            :param temperature: Температура жидкости
            :param density: Плотность жидкости

            Примеры:
            >>> liquid = Liquid(23, 970)  # Инициализация экземпляра класса
            """
            self.temperature = temperature
            self.density = density

        def __str__(self):
            return f"Температура - {self.temperature}. Плотность - {self.density}"

        def __repr__(self):
            return f"{self.__class__.__name__}temperature={self.temperature!r}, density={self.density!r})"

        def is_safe_to_drink(self) -> bool:
            """
            Функция, которая проверяет безопасно ли пить жидкость согласно параметрам температуры и плотности

            :return: Безопасно ли пить жидкость согласно имеющимся параметрам

            Примеры:
            >>> liquid = Liquid(23, 970)
            >>> liquid.is_safe_to_drink()
            """
            ...

        def possible_liquids(self) -> list:
            """
            Функция, которая возвращает названия жидкостей, близких по плотности

            :return: Возвращает список возможных видов жидкостей

            Примеры:
            >>> liquid = Liquid(23, 970)
            >>> liquid.possible_liquids()
            """
            ...

    class Water(Liquid):
        def __init__(self, temperature: float, density: float, hardness: float):
            """
            Создание и подготовка к работе объекта "Вода", унаследованного от класса "Жидкость"

            :param temperature: Температура воды
            :param density: Плотность воды
            :param hardness: Жесткость воды

            Примеры:
            >>> water = Liquid(23, 970, 15)  # Инициализация экземпляра класса
            """
            super().__init__(temperature, density)
            if hardness < 0:
                raise ValueError("Жесткость воды не может быть отрицательна")
            else:
                self.hardness = hardness

        def __repr__(self):
            return f"{self.__class__.__name__}temperature={self.temperature!r}," \
                   f" density={self.density!r}), hardness={self.hardness!r}"

        def is_safe_to_drink(self) -> bool:
            """
            Функция, которая проверяет безопасно ли пить воду согласно параметрам температуры, плотности и жесткости
            UPD: Дополнительно учитывает жесткость воды

            :return: Безопасно ли пить воду согласно имеющимся параметрам

            Примеры:
            >>> water = Water(23, 970, 15)
            >>> water.is_safe_to_drink()
            """
            ...

    pass
