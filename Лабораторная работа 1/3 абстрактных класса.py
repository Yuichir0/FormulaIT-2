import doctest


class Banana:
    def __init__(self, size: float, age: float):
        """
        Создание и подготовка к работе объекта "Банан"

        :param size: Длина банана в сантиметрах
        :param age: Возраст банана (со стадии цветка)

        Примеры:
        >>> banana = Banana(6, 143)  # Инициализация экземпляра класса
        """
        if not isinstance(size, (int, float)):
            raise TypeError("Длина банана должна быть типа int или float")
        if size <= 0:
            raise ValueError("Длина банана быть положительным числом")
        self.size = size

        if not isinstance(age, (int, float)):
            raise TypeError("Возраст банана должен быть int или float")
        if age < 0:
            raise ValueError("Возраст банана не может быть отрицательным числом")
        if age > 365:
            raise ValueError("Это больше не банан...")
        self.age = age

    def is_it_mini_banana(self) -> bool:
        """
        Функция которая проверяет, сорт банана мини или нет (меньше ли 8 см)

        :return: Является ли сорт банана мини

        Примеры:
        >>> banana = Banana(6, 143)
        >>> banana.is_it_mini_banana()
        """
        ...

    def is_banana_ripe(self) -> bool:
        """
        Функция которая проверяет, созрел ли банан (проверка по возрасту)

        :return: Созрел ли банан

        Примеры:
        >>> banana = Banana(6, 143)
        >>> banana.is_banana_ripe()
        """
        ...


class Table:
    def __init__(self, area: float, legs: int):
        """
        Создание и подготовка к работе объекта "Банан"

        :param area: Площадь поверхности стола в см^2
        :param legs: Количество ножек стола

        Примеры:
        >>> table = Table(10000, 4)  # Инициализация экземпляра класса
        """
        if not isinstance(area, (int, float)):
            raise TypeError("Площадь стола должна быть типа int или float")
        if area < 0:
            raise ValueError("Площадь стола быть положительным числом")
        self.area = area

        if not isinstance(legs, int):
            raise TypeError("Количество ног стола должно быть типа int")
        if legs < 0:
            raise ValueError("Количество ног стола не может быть отрицательным числом")
        self.legs = legs

    def put_tablecloth(self, tablecloth_area: float) -> None:
        """
        Функция, которая накрывает на стол простыню.

        :param tablecloth_area: Площадь простыни

        :raise ValueError: Если площадь простыни меньше площади стола, то вызвать ошибку

        Примеры:
        >>> table = Table(10000, 4)
        >>> table.put_tablecloth(12000)
        """
        if not isinstance(tablecloth_area, (int, float)):
            raise TypeError("Площадь простыни должна быть типа int или float")
        if tablecloth_area < 0:
            raise ValueError("Площадь простыни должна положительным числом")
        ...

    def cut_leg(self, legs_to_cut: int) -> None:
        """
        Функция, которая отпиливает столу указанное количество ног.

        :param legs_to_cut: Количество отпиливаемых ног

        :raise ValueError: Если количество отпиливаемых ног >= количество ног стола, вызвать ошибку

        Примеры:
        >>> table = Table(10000, 4)
        >>> table.cut_leg(3)
        """
        if not isinstance(legs_to_cut, int):
            raise TypeError("Количество отпиливаемых ног должно быть типа int")
        if legs_to_cut < 0:
            raise ValueError("Количество отпиливаемых ног должно быть положительным числом")
        ...


class Dictionary:
    def __init__(self, words: int, name: str):
        """
        Создание и подготовка к работе объекта "Словарь"

        :param words: Количество слов в словаре
        :param name: Название словаря

        Примеры:
        >>> dictionary = Dictionary(200000, "Толковый словарь живого великорусского языка")  # Инициализация экземпляра класса
        """
        if not isinstance(words, int):
            raise TypeError("Площадь стола должна быть типа int или float")
        if words <= 0:
            raise ValueError("Площадь стола не может быть отрицательным числом")
        self.words = words

        if not isinstance(name, str):
            raise TypeError("Название словаря должно быть типа str")
        if name == "":
            raise ValueError("Название словаря не должно быть пустым")
        self.name = name

    def check_for_word(self, checked_word: str) -> None:
        """
        Функция, которая ищет слово в словаре.

        :param checked_word: Искомое слово

        :return: Найдено ли слово в словаре

        Примеры:
        >>> dictionary = Dictionary(200000, "Толковый словарь живого великорусского языка")
        >>> dictionary.check_for_word("Стол")
        """
        if not isinstance(checked_word, str):
            raise TypeError("Искомое слово должно быть типа str")
        if checked_word == "":
            raise ValueError("Искомое слово не должно быть пустым")
        ...

    def add_word(self, added_word: str) -> None:
        """
        Функция, которая добавляет слово в словарь.

        :param added_word: Добавляемое слово

        :raise ValueError: Если слово уже в словаре, вызвать ошибку

        Примеры:
        >>> dictionary = Dictionary(200000, "Толковый словарь живого великорусского языка")
        >>> dictionary.add_word("Стол")
        """
        if not isinstance(added_word, str):
            raise TypeError("Добавляемое слово должно быть типа str")
        if added_word == "":
            raise ValueError("Добавляемое слово не должно быть пустым")
        ...

    def change_name(self, new_name: str) -> None:
        """
        Функция, которая изменяет название словаря.

        :param new_name: Новое название

        :raise ValueError: Если название словаря уже существует, вызвать ошибку

        Примеры:
        >>> dictionary = Dictionary(200000, "Толковый словарь живого великорусского языка")
        >>> dictionary.change_name("Словарь Даля")
        """
        if not isinstance(new_name, str):
            raise TypeError("Новое название должно быть типа str")
        if new_name == "":
            raise ValueError("Новое название не должно быть пустым")
        ...


if __name__ == "__main__":
    doctest.testmod()
