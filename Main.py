import copy
from BasicModule import fact
from MatrixModule import Matrix
from ComplexModule import Complex
from StochasticModule import MarkovChain
from TrigModule import sin, cos, tan, cot, sec, csc
from CalculusModule import function, derivative, integral, double_integral, path_integral

# Constants
pi = 3.1415926535897932
e = 2.7182818284590452

# calculated (float) : Approximated value of operation
# actual     (float) : Actual value of operation
def error(calculated, actual):
    return abs(calculated - actual)

# f           (str) : Function in terms of x, y, and z
# a, b      (float) : Lower and upper bounds for searching
# type        (str) : Method of calculation (bisection)
# tolerance (float) : Allowable error for the calculated root
# max_iter    (int) : Number of allowable iterations before terminating search
# iterations (bool) : Determines whether iter will be returned
def find_roots(f, a, b, type = 'bisection', tolerance = 10e-8, max_iter = 10000, iterations = False):
    iter = 0
    if type == 'bisection':
        while True:
            c = (a + b) / 2
            print(c)
            if iterations:
                iter += 1
            if abs(function(f, c)) < tolerance:
                if iterations:
                    return c, iter
                return c
            if iter == max_iter:
                return 'Root not found'
            if function(f, c) * function(f, a) > 0:
                a = c
            else:
                b = c


def main():

    i = Complex(0, 1)

    print(sin(i))
    print(sin(sin(i)))
    print(1 / i)
    print()

    M = Matrix([[0,0,0,1],
               [1,0,0,0],
               [0,1,0,0],
               [0,0,1,0]])

    print(M)
    print(M ** 2)
    print(M ** 3)
    print(M ** 4)
    print(M ** 5)
    print(M ** 6)
    

main()