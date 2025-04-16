

class Complex:
    def __init__(self, realpart=0, imagpart=0):
        self.r, self.i = realpart, imagpart

    # Два метода строкового представления
    def __str__(self):
        return f'{self.r}+{self.i}i'

    def __repr__(self): # Не зная что это не пишите
        return f'Complex({self.r},{self.i})'
    
    # Некоторые методы перегрузки операций
    def __add__(self, other):   
        if isinstance(other, Complex):
            return Complex(self.r+other.r, self.i+other.i)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self + Complex(other)
        if isinstance(other, complex):
            return self + Complex(other.real, other.imag)

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.r += other
            return self
        if isinstance(other, Complex):
            self.r += other.r; self.i += other.i
            return self

    def __eq__(self, other):
        return self.r==other.r and self.i==other.i

    def __abs__(self):
        return (self.r**2 + self.i**2)**(1/2)

    def __bool__(self):
        return bool(abs(self))