import random
import time
import numpy as np
from functions import InputInt

class matrix:
    arr = [[]]

    def __init__(self):
        self.arr = matrix.empty(self, 0)

    def generate_array(self, rows, cols):
        self.arr = np.array([[random.randint(-100, 100) for i in range(int(cols))] for _ in range(int(rows))])

    def array(self, data):
        self.arr = np.array(data)

    def values(self, data):
        self.arr = np.array(data)

    def zeros(self, count):
        self.arr = np.zeros(count)

    def ones(self, count):
        self.arr = np.ones(count)

    def empty(self, count):
        self.arr = np.empty(count)

    def full(self, number, count):
        self.arr = np.full(number, count)

    def AddNumberToEachElement(self, number):
        self.arr += int(number)

    def mean(self):
        print("Result of mean function = ", np.mean(self.arr))

    def median(self):
        print("Median value of array = ",np.median(self.arr))

    def corrcoef(self, secondArr):
        return np.corrcoef(self.arr, secondArr)

    def corrcoefWithPrint(self, secondArr):
        print("Result of corcoef function = ", np.corrcoef(self.arr.flatten(), secondArr))

    def var(self):
        print("Result of var function = ", np.var(self.arr))

    def std(self):
        print("Result of std function = ", np.std(self.arr))

    def MinValueRowsSum(self):
        row_sum = np.sum(self.arr, axis=1)
        print("Minimum row sum = ", min(row_sum))

    def corrcoefEvenOdd(self):
        elems = np.array(self.arr.flatten())
        if len(elems)%2==1:
            elems = np.append(elems, 0)
        even_elems = elems[::2]
        odd_elems = elems[1::2]
        print("corrcoef of arrays of evem and odd elements = ", np.corrcoef(even_elems, odd_elems)[0,1])

    def print(self):
        print("Current matrix")
        print(self.arr.__str__())


def task5_test_function():
    check = False
    while check == False:
        print("Input matrix size")
        a = InputInt()
        b = InputInt()
        matr = matrix()
        time.sleep(0.1)
        matr.generate_array(a,b)
        time.sleep(0.1)
        matr.print()
        time.sleep(0.1)
        matr.corrcoefEvenOdd()
        time.sleep(0.1)
        matr.MinValueRowsSum()
        matr.median()
        time.sleep(0.1)
        matr.mean()
        time.sleep(0.1)
        matr.AddNumberToEachElement(10)
        matr.print()
        print("If you want to stop this task write 'stop', else task will rerun")
        str = input()
        if str == "stop":
            return

