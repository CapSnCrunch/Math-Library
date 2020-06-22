from MatrixModule import Matrix
from BasicModule import fact
from ComplexModule import Complex

# Constants
pi = 3.1415926535897932
e = 2.7182818284590452

# x  (float) : Value to take sin of
# mode (str) : Determines what units x is given in
def sin(x, mode = 'rad', terms = 10):
    if isinstance(x, Matrix):
        total = Matrix(x.array) * 0
    elif isinstance(x, Complex):
        total = Complex(0,0)
    else:
        total = 0
    if mode == 'rad':
        convert = 1
        if not isinstance(x, Matrix) and not isinstance(x, Complex):
            x %= (2 * pi)
    if mode == 'deg':
        convert = pi / 180
        if not isinstance(x, Matrix) and not isinstance(x, Complex):
            x %= 360
    for i in range(terms):
        total += (x * convert) ** (2*i + 1) * (-1)**i / fact(2*i + 1)
    return total

# x  (float) : Value to take cos of
# mode (str) : Determines what units x is given in
def cos(x, mode = 'rad', terms = 10):
    if isinstance(x, Matrix):
        total = Matrix(x.array) * 0
    elif isinstance(x, Complex):
        total = Complex(0,0)
    else:
        total = 0
    if mode == 'rad':
        convert = 1
        if not isinstance(x, Matrix) and not isinstance(x, Complex):
            x %= (2 * pi)
    if mode == 'deg':
        convert = pi / 180
        if not isinstance(x, Matrix) and not isinstance(x, Complex):
            x %= 360
    for i in range(terms):
        total += (x * convert) ** (2 * i) * (-1)**i / fact(2 * i)
    return total

# x  (float) : Value to take tan of
# mode (str) : Determines what units x is given in
def tan(x, mode = 'rad', terms = 10):
    return sin(x, mode, terms) / cos(x, mode, terms)

# x  (float) : Value to take cot of
# mode (str) : Determines what units x is given in
def cot(x, mode = 'rad', terms = 10):
    return cos(x, mode, terms) / sin(x, mode, terms)

# x  (float) : Value to take sec of
# mode (str) : Determines what units x is given in
def sec(x, mode = 'rad', terms = 10):
    if not isinstance(x, Complex):
        return 1 / cos(x, mode, terms)
    return Complex(1,0) / cos(x, mode, terms)
    
# x  (float) : Value to take csc of
# mode (str) : Determines what units x is given in
def csc(x, mode = 'rad', terms = 10):
    if not isinstance(x, Complex):
        return 1 / sin(x, mode, terms)
    return Complex(1,0) / sin(x, mode, terms)