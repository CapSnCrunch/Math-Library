from MatrixModule import Matrix
from ComplexModule import Complex

class MarkovChain():
    def __init__(self, transition_array):
        self.matrix = Matrix(transition_array)
        self.size = self.matrix.rows

    def calculate(self, start, time):
        vector_array = []
        for i in range(self.size):
            vector_array.append(int(i == start))
        a = Matrix([vector_array])
        for i in range(time):
            a *= self.matrix
        return a

    # def add_state(self, name)

    # def add_transition(self, name, name2, p)

    def __repr__(self):
        print(self.matrix)
        return ''