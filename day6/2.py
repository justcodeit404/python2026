# 2026-01-11  12:40:53
class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight=weight

    def run(self):
        self.weight-=0.5
        print(f'{self.name}跑步了，体重减了0.5')

    def eat(self):
        self.weight+=1
        print(f'{self.name}吃饭了，体重增加了1')
    def __str__(self):
        return f'{self.name}体重是{self.weight}'
elephant=Person('elephant',18)
elephant.eat()
print(elephant)