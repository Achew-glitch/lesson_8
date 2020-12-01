class ZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    dividend = float(input('Введите делимое: '))
    divider = float(input('Введите делитель: '))
    if divider == 0:
        raise ZeroException('Я не смогу вывести настолько маленькую бесконечную цифру!\nСжалься надо мной!')
except ZeroException as err:
    print(err)
else:
    print(f'Результат деления: {dividend / divider}')
