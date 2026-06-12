class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def drive(self) -> str:
        return f"Driving the {self.make} {self.model}."


class Car(Vehicle):
    def __init__(self, make: str, model: str, doors: int):
        super().__init__(make, model)
        self.doors = doors

    def info(self) -> str:
        return f"{self.make} {self.model} with {self.doors} doors."


car = Car("Toyota", "Corolla", 4)
print(car.info())
print(car.drive())
