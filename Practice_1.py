class Date:
    date = '0-0-0'

    def __init__(self, date_str):
        Date.date = date_str

    @classmethod
    def get_date(cls):
        data_int = map(int, cls.date.split('-'))
        return list(data_int)

    @staticmethod
    def valid_date(st_date):

        if 1 < Date(st_date).get_date()[0] < 31:
            print(f'Day: {Date(st_date).get_date()[0]}')
        else:
            print('Wrong day')

        if 1 < Date(st_date).get_date()[1] < 12:
            print(f'Month: {Date(st_date).get_date()[1]}')
        else:
            print('Wrong month')


date = Date('05-04-1991')
print(Date.get_date())
Date.valid_date('05-04-1991')
