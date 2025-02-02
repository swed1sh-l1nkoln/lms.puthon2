class Book:
    def __init__(self, name: str, author: str):
        self._name = name #const
        self._author = author #const

    @property
    def name(self): return self._name
    @property
    def author(self): return self._author

    def __str__(self): return f"Книга: '{self.name}'. Автор: {self.author}"

    def __repr__(self): return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self): return self._pages

    @pages.setter
    def pages(self, value: int): #check
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self._pages = value

    def __str__(self): return f"{super().__str__()}. Количество страниц: {self.pages}"

    def __repr__(self): return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self): return self._duration

    @duration.setter
    def duration(self, value: float):#check
        if not isinstance(value, (float, int)):
            raise ValueError("Продолжительность аудиокниги должна быть числом (целым или вещественным).")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной.")
        self._duration = float(value)

    def __str__(self): return f"{super().__str__()}. Продолжительность: {self.duration:.2f} ч"

    def __repr__(self): return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    paper_book = PaperBook(name="Война и мир", author="Лев Николаевич Толстой", pages=1328)
    audio_book = AudioBook(name="Война и мир", author="Лев Николаевич Толстой", duration=5.5)

    print(paper_book)
    print(audio_book)

