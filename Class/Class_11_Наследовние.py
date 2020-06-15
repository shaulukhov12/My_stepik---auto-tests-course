class MyList(list):#Указываем те классы от которых мы наследуемся в скобка
    def even_lenght(self):# Проверка является ли длина четной
        return len(self) % 2 ==0
x = MyList()
print(x)
x.extend([1, 2, 3, 4, 5])
print(x)
print(x.even_lenght())
x.append(6)
print(x.even_lenght())#

