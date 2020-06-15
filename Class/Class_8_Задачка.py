class MoneyBox:

    def __init__(self, capacity=10):
        self.count = 0
        self.capacity = capacity # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        self.v = v
        if self.capacity - self.count < v :
            return False# True, если можно добавить v монет, False иначе
        else:
            return True

    def add(self, v):
        if self.can_add(v):
            self.count += v# положить v монет в копилку
        else:
            print(",fkfkf")


# Класс должен поддерживать информацию о количестве монет в копилке +
# предоставлять возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
# При создании копилки, число монет в ней равно 0.

# Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True﻿.