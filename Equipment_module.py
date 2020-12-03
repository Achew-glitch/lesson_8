class Office_Equipment:
    def __init__(self, dimensions, l_net, name):
        self.name = name
        self.dimensions = dimensions
        self.l_net = l_net

    def start_equipment(self):
        print(f'Start {self.name}')

    def turn_off_equipment(self):
        print(f'{self.name} is turn off')

    def get_network_adress(self):
        print(f'{self.name} belongs to the {self.l_net}')

    @staticmethod
    def create_copy(answer):
        type_equipments = {'printer': Printer, 'scanner': Scaner, 'xerox': Xerox}
        try:
            size = int(input('What size: '))
            network_adress = input('Network Adress: ')
            name = input('Name: ')
            return type_equipments.get(answer)(size, network_adress, name)
        except ValueError:
            print('You input a wrong value')


class Printer(Office_Equipment):

    def __init__(self, dimensions, l_net, name):
        super().__init__(dimensions, l_net, name)
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
    def __init__(self, dimensions, l_net, name):
        super().__init__(dimensions, l_net, name)
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


class Xerox(Scaner, Printer):
    def __init__(self, dimensions, l_net, name):
        super().__init__(dimensions, l_net, name)
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
        self.use_scanner()
        self.use_printer(count_paper)
        self.start_equipment()
        self.lamp_life -= 0.01 * count_paper
        self.used_paper += count_paper
        self.ink -= count_paper * 0.03
        print(f'{self.name} was scanned document and print {count_paper} sheets')
        self.turn_off_equipment()
