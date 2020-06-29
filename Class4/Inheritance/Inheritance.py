class Person: #Родительский класс, parent

    def can_walk(self):
        print('Я могу ходить')

    def can_breath(self):
        print('Я могу ходить')


class Doctor(Person):# Sub-class

    def can_cure(self):
        print('Я могу лечить')


class Architect(Person):

    def can_build(self):
        print('Я могу построить здание')

d = Doctor()
d.can_cure()
a = Architect()
a.can_build()
a.can_walk()
d.can_walk()