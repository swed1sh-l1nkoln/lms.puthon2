class Car:
    def init(self, make: str, model: str, year: int) -> None:
        self._make = make
        self._model = model
        self._year = year

    @property
    def make(self) -> str:
        return self._make

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    def drive(self) -> str:
        return f"{self.make} {self.model} движется."

    def str(self) -> str:
        return f"{self.year} {self.make} {self.model}"

    def repr(self) -> str:
        return f"{self.class.name}(make={self.make!r}, model={self.model!r}, year={self.year!r})"


class PassengerCar(Car):
    def init(self, make: str, model: str, year: int, passenger_capacity: int) -> None:
        super().init(make, model, year)
        self._passenger_capacity = passenger_capacity

    @property
    def passenger_capacity(self) -> int:
        return self._passenger_capacity

    def drive(self) -> str:
        return f"{super().drive()} Вместимость: {self.passenger_capacity} пассажиров."

    def str(self) -> str:
        return f"{super().str()}, Вместимость: {self.passenger_capacity}"


class Truck(Car):
    def init(self, make: str, model: str, year: int, cargo_capacity: float) -> None:
        super().init(make, model, year)
        self._cargo_capacity = cargo_capacity

    @property
    def cargo_capacity(self) -> float:
        return self._cargo_capacity

    def drive(self) -> str:
        return f"{super().drive()} Грузоподъемность: {self.cargo_capacity} т."

    def str(self) -> str:
        return f"{super().str()}, Грузоподъемность: {self.cargo_capacity} т."



if __name__ == "__main__":
    passenger_car = PassengerCar("Toyota", "Camry", 2021, 5)
    print(passenger_car)  # Вывод информации о легковом автомобиле
    print(passenger_car.drive())  # Методы для легкового автомобиля

    truck = Truck("KamAZ", "Fourty", 2001, 15.0)
    print(truck)  # Вывод информации о грузовом автомобиле
    print(truck.drive())  # Методы для грузового автомобиля
