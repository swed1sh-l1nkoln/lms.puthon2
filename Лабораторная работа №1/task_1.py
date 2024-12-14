import doctest

#Объект автомобиль, make,model,year- марка,модель и год выпуска автомобиля(включает валидацию на то,что год не ранее 1900)
#
#
#
#

class Car:
    def __init__(self, make: str, model: str, year: int):
        """
        Примеры:
        >>> car = Car("Toyota", "Camry", 2020)  # Инициализация экземпляра класса
        >>> car.make
        'Toyota'
        >>> car.year
        2020
        """
        if not isinstance(make, str):
            raise TypeError("Марка должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if year < 1900:
            raise ValueError("Год выпуска должен быть не менее 1900")

        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> None: ... #заводит движок


    def stop_engine(self) -> None: ... #глушит движок


#Объект-строение- адрес постройки и кол-во этажей(проверка на то,что оно !=0)
#
class Building:
    def __init__(self, address: str, floors: int):
        """
        Примеры:
        >>> building = Building("123 Main St", 5)  # Инициализация экземпляра класса
        >>> building.address
        '123 Main St'
        >>> building.floors
        5
        """
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть строкой")
        if not isinstance(floors, int) or floors <= 0:
            raise ValueError("Количество этажей должно быть положительным целым числом")

        self.address = address
        self.floors = floors

    def open_doors(self) -> None:  ... #открыть дверь

    def close_doors(self) -> None: ... #закрыть дверь

#Книга-название,автор и кол-во страниц
class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Примеры:
        >>> book = Book("War and Peace", "Lev Tolstoy", 1360)  # Инициализация экземпляра класса
        >>> book.title
        'War and Peace'
        >>> book.pages
        1360
        """
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.pages = pages

    def read_book(self, pages_read: int) -> None:
        """
        Читает указанное количество страниц из книги.

        :param pages_read: Количество страниц для чтения. Не должно превышать общее количество страниц.
        :raises ValueError: Если количество прочитанных страниц превышает количество страниц в книге.

        Примеры:
        >>> book = Book("War and Peace", "Lev Tolstoy", 1360)
        >>> book.read_book(580)
        """
        if not isinstance(pages_read, int) or pages_read <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным целым числом")
        if pages_read > self.pages:
            raise ValueError("Невозможно прочитать больше страниц, чем в книге")
        ...

        def get_book_info(self) -> str:
            """
            Возвращает информацию о книге.

            :return: Строка с названием и автором книги.

            Примеры:
            >>> book = Book("1984", "George Orwell", 328)
            >>> book.get_book_info()
            '1984 by George Orwell'
            """
            return f"{self.title} by {self.author}"

    if __name__ == "__main__":
        doctest.testmod()

