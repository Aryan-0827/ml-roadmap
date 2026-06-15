class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius   # Uses the property setter

    @staticmethod
    def c_to_f(celsius):
        return (celsius * 9/5) + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        self._celsius = value