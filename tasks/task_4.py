# Задача 4. Класс CustomList
# Условие:
# Создайте класс CustomList, который хранит список элементов.
# Реализуйте:

# Конструктор, принимающий и сохраняющий список;
# Магический метод __len__, возвращающий количество элементов;
# Магический метод __getitem__, чтобы можно было обращаться по индексу (поддержка срезов не обязательна);
# Магический метод __contains__ для проверки принадлежности элемента списку через оператор in.


class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, value):
        return value in self.items
