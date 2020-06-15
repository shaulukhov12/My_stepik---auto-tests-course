class EvenLengthMixin:
    def even_lenght(self):
        return len(self) % 2 ==0

class MyList(list,EvenLengthMixin):
    pass

class MyDict(dict, EvenLengthMixin):
    pass
x = MyDict()
x["key"] = "value"
x["another key"] = "another key"
print(x.even_lenght())