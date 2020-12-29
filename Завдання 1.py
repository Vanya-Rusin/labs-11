import math


class TCircle:
    def __init__(self,r):
        self.r = int(input('введіть радіус:'))

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
        return self.r * math.pi ** 2

    def p(self):
        return 2*math.pi*self.r

    def __add__(self, other):
        return self.r + other

    def __sub__(self, other):
        return self.r - other

    def __mul__(self, other):
        return self.r * other

    def da(self,value):
        value -= 1
        return value


c1 = TCircle(3)
print('периметр=',c1.p())
print('довжина кола=',c1.s())
print(c1.__add__(2))
print(c1.__sub__(3))
print(c1.__mul__(4))
print(c1.da(3))