import re

class WrongNumberException(Exception):
    def __init__(self, message):
        super().__init__(message)


def CheckNumber(phonenumber):
    r = re.compile('(\+7|8)\D*\d{3}\D*\d{3}\D*\d{2}\D*\d{2}')
    if r.search(phonenumber):
        print(f"Ваш номер {phonenumber}")
        return True
    else:
        raise WrongNumberException("Неверно введен номмер")
        pass


print(CheckNumber('89179541350'))
print(CheckNumber("+79179541350"))
print(CheckNumber("134151"))
print(CheckNumber("fkladsjfqplkjf"))
print(CheckNumber("0"))



