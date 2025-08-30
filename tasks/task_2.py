# Задача 2. Класс Circle
# Условие:
# Создайте класс Circle с атрибутом radius (радиус окружности).

# Реализуйте:
# __init__;
# __str__ — чтобы при вызове print(circle) выводилась строка Circle with radius: <radius>;
# __lt__ — для сравнения двух окружностей по радиусу (меньше, если радиус меньше);
# __mul__ — умножение окружности на число должно возвращать новую окружность с радиусом, умноженным на это число.


class Circle:
    def __init__(self, radius):
    
        self.radius = radius

    def __str__(self):
    
        return f"Circle with radius: {self.radius}"

    def __lt__(self, other):
      
        return self.radius < other.radius

    def __mul__(self, value):
       
        return Circle(self.radius * value)
