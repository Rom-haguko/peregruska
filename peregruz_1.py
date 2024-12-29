class Negator:
    @staticmethod
    def neg(num):
        if type(num) in (int, float):
            return -num
        elif type(num) == bool:
            return not num
        else:
            raise TypeError('Аргумент переданного типа не поддерживается')


print(Negator.neg(5))
print(Negator.neg(-3.14))
print(Negator.neg(True))
print(Negator.neg(False))
print()
print(Negator.neg('pip')) #вызов ошибки