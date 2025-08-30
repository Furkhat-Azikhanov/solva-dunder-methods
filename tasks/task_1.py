# Задача 1. Класс Vector2D
# Условие:

# Создайте класс Vector2D, который описывает вектор на плоскости с координатами x и y.
# Реализуйте следующие магические методы:
# __init__ для инициализации вектора;
# __repr__ для вывода вида Vector2D(x, y);
# __add__ для сложения двух векторов;
# __eq__ для проверки равенства векторов (считаем равными, если координаты совпадают).

class Vector2D:
    def __init__(self, x, y):
    
        self.x = x
        self.y = y

    def __repr__(self):
        
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
       
        return self.x == other.x and self.y == other.y
