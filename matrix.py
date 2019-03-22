class Matrix:
    matrix = None
    def __init__(self, a, b, c, d):
        w, h = 2, 2
        self.matrix = [[0 for x in range(w)] for y in range(h)]
        self.matrix[0][0] = a
        self.matrix[0][1] = b
        self.matrix[1][0] = c
        self.matrix[1][1] = d
    
    def __getitem__(self, number):
        return self.matrix[number]
    
    def add(self, second_matrix):
        self.matrix[0][0] += second_matrix[0][0]
        self.matrix[0][1] += second_matrix[0][1]
        self.matrix[1][0] += second_matrix[1][0]
        self.matrix[1][1] += second_matrix[1][1]

    def product(self):
        for i in self.matrix:
            print(i)
