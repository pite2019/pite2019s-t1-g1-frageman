import math

class Matrix:

    def __init__(self, *args):
        self.N = math.sqrt(len(args))
        if math.floor(self.N) != self.N:
            raise ValueError("wrong size of matrix")
        self.N = int(self.N)
        self.matrix = [[0 for x in range(self.N)] for y in range(self.N)]
        k = 0
        for i in range(self.N):
            for j in range(self.N):
                self.matrix[i][j] = args[k]
                k += 1
    
    def __getitem__(self, number):
        return self.matrix[number]
    
    def __add__(self, second_value):

        if isinstance(second_value, int):
            tmpmatrix = []
            for i in range(self.N):
                for j in range(self.N):
                    tmpmatrix.append(self.matrix[i][j] + second_value)
            return Matrix(*tmpmatrix)
        
        if isinstance(self, int) and isinstance(second_value, Matrix):
            tmpmatrix = []
            for i in range(second_value.N):
                for j in range(second_value.N):
                    tmpmatrix.append(self + second_value[i][j])
            return Matrix(*tmpmatrix)
        
        if isinstance(second_value, list):
            tmpmatrix = []
            tmp2 = Matrix(*second_value)

            for i in range(tmp2.N):
                for j in range(tmp2.N):
                    tmpmatrix.append(self.matrix[i][j] + tmp2[i][j])
            return Matrix(*tmpmatrix)

        if(self.N != second_value.N):
            raise ValueError("wrong sizes of matrixes - can't add")

        tmpmatrix = []
        for i in range(self.N):
            for j in range(self.N):
                tmpmatrix.append(self.matrix[i][j] + second_value[i][j])
        return Matrix(*tmpmatrix)

    def __sub__(self, second_matrix):
        if(self.N != second_matrix.N):
            raise ValueError("wrong sizes of matrixes - can't sub")
        tmpmatrix = []
        for i in range(self.N):
            for j in range(self.N):
                tmpmatrix.append(self.matrix[i][j] - second_matrix[i][j])
        return Matrix(*tmpmatrix)
    
    def __iadd__(self, second_matrix): 
        if(self.N != second_matrix.N):
            raise ValueError("wrong sizes of matrixes - can't add")
        for i in range(self.N):
            for j in range(self.N):
                self.matrix[i][j] += second_matrix[i][j]
        return self

    def __isub__(self, second_matrix):
        if(self.N != second_matrix.N):
            raise ValueError("wrong sizes of matrixes - can't sub")
        for i in range(self.N):
            for j in range(self.N):
                self.matrix[i][j] -= second_matrix[i][j]
        return self
    
    def __matmul__(self, second_matrix):
        sume = 0
        if(self.N != second_matrix.N):
            raise ValueError("wrong sizes of matrixes - can't multiply")
        tmpmatrix = []
        for i in range(self.N):
            for j in range(self.N):
                for k in range(self.N):
                    sume+=self.matrix[i][k] * second_matrix[k][j]
                tmpmatrix.append(sume)
                sume = 0
        return Matrix(*tmpmatrix)

    def print(self):
        for i in self.matrix:
            print(i)
