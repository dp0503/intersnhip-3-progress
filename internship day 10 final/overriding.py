class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def sound(self) -> str:
        return "The vehicle makes a generic sound."


class Car(Vehicle):
    def sound(self) -> str:
        return f"The {self.make} {self.model} honks: beep beep!"


car = Car("Honda", "Civic")
print(car.sound())
