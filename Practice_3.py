class IntException(Exception):
    @classmethod
    def check_int(cls, check):
        try:
            inp_data.append(int(check))
        except ValueError:
            raise IntException


inp_data = []
while True:
    str_int = input('Введите число: ')
    if str_int == 'stop':
        print(f'Введенные числа: {inp_data}')
        break
    else:
        try:
            IntException.check_int(str_int)
        except IntException:
            print('Вы ввели не число, повторите попытку')
