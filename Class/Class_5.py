class Counter:
    def __init__(self,start = 0):
        self.count = 0

    def inc(self):#Увеличение счетчика на 1
        self.count += 1

    def reset(self):#Обнулять наш счетчик
        self.count = 0
Counter
x = Counter()
x.inc()
print(x.count)
Counter.inc(x)
print(x.count)
x.reset()
print(x.count)