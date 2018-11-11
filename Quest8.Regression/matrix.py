import numpy as np
import time

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def transpose(self):
        start = time.time()
        [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        end = time.time()
        return end - start

    def zip_transpose(self):
        # may not need to include list conversion for timing
        start = time.time()
        zip(*self.matrix)
        end = time.time()
        return end - start
    
    def numpy_transpose(self):
        start = time.time()
        np.transpose(self.matrix)
        end = time.time()
        return end - start