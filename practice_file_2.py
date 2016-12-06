class Parent():
    def print_lastname(self):
        print('Huang')


class Child(Parent):
    def print_firstname(self):
        print('Yiqi', end=' ')

    def print_lastname(self):
        print('Waltson')


mic = Child()
mic.print_firstname()
mic.print_lastname()
