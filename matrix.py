

class Matrix(object):

    def __init__(self, x =2, y=2):
        self.X= x
        self.Y = y
        self.matrix = [[None for _ in range(self.Y)] for _ in range(self.X)]


    def set(self,x,y,val):
        self.matrix[x][y] = val

    def get(self,x,y):
        return self.matrix[x][y]

    def printMatrix(self):
        print "=== Start of Matrix==="
        for row in self.matrix:
            for val in row:
                print '{:{}}'.format(val, self.Y),
            print

        print "=== End of Matrix==="