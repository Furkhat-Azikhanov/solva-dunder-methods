# Задача 3. Класс Temperature
# Условие:
# Реализуйте класс Temperature для работы с температурами в градусах Цельсия.

# Требования:
# Конструктор принимает значение температуры;
# Реализуйте метод __float__, который возвращает температуру как число с плавающей точкой;
# Реализуйте __add__, чтобы складывать температуры (возвращать новый объект Temperature);
# Реализуйте __repr__, чтобы возвращать строку вида Temperature(<value>°C).


class Temperature:
    def __init__(self, value):
        self.value = value

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        return Temperature(self.value + other.value)

    def __repr__(self):
        return f"Temperature({self.value}°C)"
