# f         (str) : Function in terms of x, y, and z
# x, y, z (float) : Value to sample function at
def function(f, x = 0, y = 0, z = 0):
    if 't' in f:
        return eval(f.replace('t', str(x)))
    if '^' in f:
        f = f.replace('^', '**')
    for i in ['e', 'pi', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'ceil', 'floor', 'log']:
        if i in f:
            f = f.replace(i, 'math.' + i)
    return eval(f.replace('x', str(x)).replace('y', str(y)).replace('z', str(z)))


# f   (str) : Function in terms of x, y, and z
# x (float) : Value to sample derivative at
# h (float) : Size of gap for secant line
def derivative(f, x, h = 10e-4):
    return (function(f, (x + h)) - function(f, x)) / h


# f       (str) : Function in terms of x, y, and z
# a, b  (float) : Lower and upper bounds for x
# type (string) : Method of calculation (lower, midpoint, upper)
# delta (float) : Size of Riemann samples of f
def integral(f, a, b, type = 'midpoint', delta = 10e-4):
    total = 0
    if type == 'lower':
        for i in range(int((b-a) / delta)):
            total += function(f, (a + i * delta)) * delta
    if type == 'midpoint':
        for i in range(int((b-a) / delta)):
            total += function(f, (a + (i + 0.5) * delta)) * delta
    if type == 'upper':
        for i in range(int((b-a) / delta)):
            total += function(f, (a + (i + 1) * delta)) * delta
    return total


# f       (str) : Function in terms of x, y, and z
# a, b  (float) : Lower and upper bounds for x
# c, d  (float) : Lower and upper bounds for y
# type    (str) : Method of calculation (lower, midpoint, upper)
# delta (float) : Size of Riemann samples of f
def double_integral(f, a, b, c, d, type = 'midpoint', delta = 10e-4):
    total = 0
    if type == 'lower':
        for i in range(int((b-a) / delta)):
            for j in range(int((d-c) / delta)):
                total += function(f, a + i * delta, c + j * delta) * delta**2
    if type == 'midpoint':
        for i in range(int((b-a) / delta)):
            for j in range(int((d-c) / delta)):
                total += function(f, a + (i + 0.5) * delta, c + (j + 0.5) * delta) * delta**2
    if type == 'upper':
        for i in range(int((b-a) / delta)):
            for j in range(int((d-c) / delta)):
                total += function(f, a + (i + 1) * delta, c + (j + 1) * delta) * delta**2
    return total


# f       (str) : Function in terms of x, y, and z
# r      (list) : Vector valued function in terms of t (Curve to integrate along)
# a, b  (float) : Lower and upper bounds for t
# delta (float) : Size of Riemann samples of f
def path_integral(f, r, a, b, delta = 10e-4):
    f = f.replace('x', r[0]).replace('y', r[1]).replace('z', r[2])
    total = 0
    for i in range(int((b-a) / delta)):
        v = a + i * delta
        total += function(f, v) * (derivative(r[0], v)**2 + derivative(r[1], v)**2 + derivative(r[2], v)**2) ** (1/2) * delta
    return total