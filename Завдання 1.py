from math import pi
class TCircle:
    def __init__(self,r):
        self.r = r

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self,value):
        value = int(value)
        if value <= 0:
            raise Exception('error')
        else:
            self.__r = value

    def s(self):
        return self.__r * pi ** 2

    def p(self):
        return 2*pi*self.__r

    def __add__(self, other):
        return TCircle(self.__r + other.__r)

    def __sub__(self, other):
        return TCircle(self.__r - other.__r)

    def __mul__(self, other):
        return TCircle(self.__r * other)



c1 = TCircle(3)
print(c1.p())