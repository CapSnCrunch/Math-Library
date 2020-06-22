class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        if not isinstance(other, Complex):
            return Complex(self.a * other, self.b * other)
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __truediv__(self, other):
        if not isinstance(other, Complex):
            return Complex(self.a / other, self.b / other)
        return Complex((self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2), (self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2))

    def __pow__(self, other):
        temp = Complex(self.a, self.b)
        for i in range((other - 1) % 4):
            self *= temp
        return self

    def conjugate(self):
        return Complex(self.a, -self.b)

    def mag(self):
        return eval((self.a**2 + self.b**2)**1/2)

    def __repr__(self):
        return 'Complex(' + str(self.a) + ', ' + str(self.b) + ')' 
        # return '(' + str(self.a) + ', ' + str(self.b) + ')'