#   Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
#   А также класс «Оргтехника», который будет базовым для классов-наследников.
#   Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#   В базовом классе определить параметры, общие для приведенных типов.
#   В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

from Equipment_module import Printer, Scaner, Xerox, Office_Equipment
from Depo_module import Depostite

printer = Printer(5, '198.162.0.255', 'Main Printer')
scanner = Scaner(2, '192.168.0.134', 'Main Scanner')
xerox = Xerox(15, '1.1.1.1', 'Main Xerox')
xerox_2 = Xerox(10, '4.4.4.4', 'Second Xerox')
scanner_2 = Scaner(1, '3.3.3.3', 'Second Scanner')
printer_2 = Printer(4, '2.2.2.2', 'Second Printer')
printer_3 = Printer(3, '6.6.6.6', 'Third Printer')
scanner_3 = Scaner(1, '7.7.7.7', 'Third Scanner')
xerox_3 = Xerox(12, '8.8.8.8', 'Third Xerox')

deposite = Depostite(15, 'Main Deposite')
deposite.set_equip('Central Office', printer, scanner, xerox)
deposite.set_equip('Second Office', printer_2, scanner_2, xerox_2)
deposite.set_equip('Second Office', printer_3, scanner_3, xerox_3)

while True:
    answer = input('You can:\nWatch list equipments'
                   '\nRemove equipment'
                   '\nMove equipment'
                   '\nFind equipment'
                   '\nAdd equipment\n')
    if answer.lower() == 'exit':
        break
    elif answer.lower() == 'move':
        deposite.move_equip(input('Where to move: '), input('What to move: '))
        deposite.get_equipments()
    elif answer.lower() == 'watch':
        deposite.get_equipments()
    elif answer.lower() == 'remove':
        deposite.__delitem__(input('What is remove: '))
        deposite.get_equipments()
    elif answer.lower() == 'find':
        deposite.get_place(input('What to find: '))
    elif answer.lower() == 'add':
        deposite.set_equip(input('Where to add: '), Office_Equipment.create_copy(input('What to add: ')))
        deposite.get_equipments()
else:
    pass
