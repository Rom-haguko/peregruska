from datetime import date

class BirthInfo:
    def __init__(self, birth_date):
        if isinstance(birth_date, date):
            if birth_date<=date.today():
                self.birth_date = birth_date
            else:
                raise TypeError('Некорректная дата')
        elif type(birth_date) == str:
            if date.fromisoformat(birth_date)<=date.today():
                self.birth_date = date.fromisoformat(birth_date)
            else:
                raise TypeError('Некорректная дата')
        elif type(birth_date) in (list, tuple):
            if date(*birth_date) <= date.today():
                self.birth_date = date(*birth_date)
            else:
                raise TypeError('Некорректная дата')

        else:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        if date.today().month >= self.birth_date.month and date.today().day >= self.birth_date.day:
            return date.today().year - self.birth_date.year
        else:
            return date.today().year - self.birth_date.year - 1


px1 = BirthInfo("2000-01-01")
print(px1.age)

px2 = BirthInfo([2020, 2, 29])
print(px2.age)

px3 = BirthInfo((2006, 10, 11))
print(px3.age)
