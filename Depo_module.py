class Depostite:
    equipments = {}

    def __init__(self, count_equipment, name):

        self.name = name
        self.count_equipment = count_equipment
        self.have_equipmets = 0

    def set_equip(self, location, *equipment):

        if self.count_equipment - len(equipment) <= 0:
            print(f'Deposite {self.name} is full.'
                  f'\nYpu can not put in here {abs(self.count_equipment - len(equipment))} pieces')
        else:
            if location in self.equipments.keys():
                for el in equipment:
                    self.equipments[location].append(el)
            else:
                self.equipments.update({location: list(equipment)})
            self.count_equipment -= len(equipment)
            self.have_equipmets += len(equipment)

    def get_counts_equip(self, key):

        return len(self.equipments.get(key))

    def get_place(self, finder):

        for key, values in self.equipments.items():
            for el in values:
                if el.name.lower() == finder.lower():
                    print(f'{finder} is in the {key}')
                    return el
                else:
                    print(f'The {key} have not {finder}')

    def get_equipments(self):

        print(f'Deposit {self.name} has {self.have_equipmets} pieces of equipments.')
        print('List of equipments:')
        for key, item in self.equipments.items():
            print(f'There are {self.get_counts_equip(key)} equipments in the {key} :')
            for el in item:
                print(f'{el.name}')

    def get_equip_in_place(self, place):

        try:
            print(f'{place} has:')
            for value in self.equipments.get(place):
                print(value.name)
        except TypeError:
            print(f'{place} has not equipments')

    def move_equip(self, comp_division, equipment):

        if comp_division in self.equipments.keys():
            for key, values in self.equipments.items():
                for el in values:
                    if el.name.lower() == equipment.lower():
                        self.set_equip(comp_division, el)
                        self.have_equipmets -= 1
                        values.remove(el)
                else:
                    print(f'The {key} have not {equipment}')
        else:
            self.equipments.update({comp_division: list(equipment)})

    def __delitem__(self, key):
        for k, values in self.equipments.items():
            for el in values:
                if el.name.lower() == key.lower():
                    self.have_equipmets -= 1
                    values.remove(el)
            else:
                print(f'The {k} have not {key}')