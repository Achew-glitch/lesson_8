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
        print(f'Start {self.name} in the {self.place}')

    def turn_off_equipment(self):
        print(f'{self.name} is turn off')

    def get_place(self):
        print(f'{self.name} in the {self.place}')

    def get_network_adress(self):
        print(f'{self.name} belongs to the {self.l_net}')


class Printer(Office_Equipment):

    def __init__(self, dimensions, place, l_net, name):
        super().__init__(dimensions, place, l_net, name)
        self.used_paper = 0
        self.ink = 100

    def use_printer(self, count_paper):

        if self.used_paper + count_paper > 100:
            print(f'{self.name} is out of paper.\nPaper will be reloaded')
            self.reload_paper()
            self.use_printer(count_paper)
        elif self.ink - count_paper * 0.03 <= 0:
            print(f'Printer {self.name} is out of ink\nInk will be refilled')
            self.refill_ink()
            self.use_printer(count_paper)
        else:
            self.start_equipment()
            self.used_paper += count_paper
            print(f'Paper in stock {self.name}: {self.used_paper}')
            self.ink -= count_paper * 0.03
            self.turn_off_equipment()

    def refill_ink(self):
        self.ink = 100

    def reload_paper(self):
        self.used_paper = 0


class Scaner(Office_Equipment):
    def __init__(self, dimensions, place, l_net, name):
        super().__init__(dimensions, place, l_net, name)
        self.lamp_life = 100

    def use_scanner(self):
        if self.lamp_life - 0.01 <= 0:
            print(f'Lamp of {self.name} is broken.\nLamp will be changed')
            self.change_lamp()
            self.use_scanner()
        else:
            self.start_equipment()
            self.lamp_life -= 0.01
            self.turn_off_equipment()

    def change_lamp(self):
        self.lamp_life = 100


class Xerkox(Scaner, Printer):
    def __init__(self, dimensions, place, l_net, name):
        super().__init__(dimensions, place, l_net, name)
        self.used_paper = 0
        self.ink = 100
        self.lamp_life = 100

    def use_printer(self, count_paper):
        print(f'{self.name} is printing')
        super().use_printer(count_paper)

    def use_scanner(self):
        print(f'{self.name} is scanning')
        super().use_scanner()

    def use_xerox(self, count_paper):
        if self.lamp_life - 0.01 <= 0:
            print(f'Lamp of {self.name} is broken.\nLamp will be changed')
            self.change_lamp()
            self.use_xerox()
        elif self.used_paper + count_paper > 100:
            print(f'{self.name} is out of paper.\nPaper will be reloaded')
            self.reload_paper()
            self.use_xerox()
        elif self.ink - count_paper * 0.03 <= 0:
            print(f'Printer {self.name} is out of ink\nInk will be refilled')
            self.refill_ink()
            self.use_xerox()
        else:
            self.start_equipment()
            self.lamp_life -= 0.01 * count_paper
            self.used_paper += count_paper
            self.ink -= count_paper * 0.03
            print(f'{self.name} was scanned document and print {count_paper} sheets')
            self.turn_off_equipment()


class Depostite:
    equipments = []

    def __init__(self, count_equipment, name):
        self.name = name
        self.count_equipment = count_equipment

    def set_equipment(self, *equipment):
        if self.count_equipment - len(equipment) <= 0:
            print(f'Deposite {self.name} is full.'
                  f'\nYpu can not put in here {abs(self.count_equipment - len(equipment))} pieces')
        else:
            self.equipments = equipment
            self.count_equipment -= 1

    def get_equipments(self):
        print(f'Deposit {self.name} has {len(self.equipments)} pieces of equipments.')
        print('List of equipments:')
        for el in self.equipments:
            print(el.name)


printer = Printer(5, 'Main Office', '198.162.0.255', 'Main Printer')
printer.use_printer(6)
print('\n')
scanner = Scaner(2, 'Second Office', '192.168.0.134', 'Main Scanner')
scanner.use_scanner()
print('\n')
xerox = Xerkox(15, 'Main of main office', '1.1.1.1', 'Main Xerox')
xerox.use_printer(6)
xerox.use_scanner()
xerox.use_xerox(90)
print('\n')
deposite = Depostite(15, 'Main Deposite')
deposite.set_equipment(printer, scanner, xerox)
deposite.get_equipments()
deposite.equipments[0].use_printer(6)