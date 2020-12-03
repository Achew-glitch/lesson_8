#   Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
#   А также класс «Оргтехника», который будет базовым для классов-наследников.
#   Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#   В базовом классе определить параметры, общие для приведенных типов.
#   В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Office_Equipment:
    def __init__(self, dimensions, place, l_net, name):
        self.name = name
        self.dimensions = dimensions
        self.place = place
        self.l_net = l_net

    def start_equipment(self):
        return f'Start {self.name} in {self.place}'

    def turn_off_equipment(self):
        return f'{self.name} is turn off'

    def get_place(self):
        return f'{self.name} in the {self.place} '

    def get_network_adress(self):
        return f'{self.name} belongs to the {self.l_net}'


class Printer(Office_Equipment):

    def __init__(self):
        Office_Equipment.__init__()
        self.used_paper = 0
        self.ink = 100

    def use_printer(self, count_paper):

        if self.used_paper > 100:
            print(f'{self.name} is out of paper.\nPaper will be reload')
            self.reload_paper()
        else:
            self.used_paper += count_paper
            print(f'Paper in stock {self.name}: {self.used_paper}')
            if self.ink <= 0:
                print(f'Printer {self.name} is out of ink\nInk will be refill')
                self.refill_ink()
            else:
                self.ink -= count_paper * 0.03

    def refill_ink(self):
        self.ink = 100

    def reload_paper(self):
        self.used_paper = 0


class Scaner(Office_Equipment):
    pass


class Xerkox(Office_Equipment):
    pass


class Depostite:
    pass
