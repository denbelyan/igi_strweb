import math
import matplotlib.pyplot as plt
import numpy as np
from functions import InputInt
from functions import InputFloat
from functions import check_range
from functions import check_range_n
class task3:
    def Calculate(self, x , n, UserEps):
        """function for calculate math expression with check useresp """
        summ = 0
        data = []
        xval = float(x)
        iter = 0
        for i in range (int(n)):
            summ+= (-1)**(i)*(xval)**(i+1)/(i+1)
            data.append(int((-1)**(i)*(xval)**(i+1)/(i+1)))
            if abs(summ-math.log(float(x)+1))<UserEps and iter == 0:
                print ("number of series terms required to achieve the specified calculation accuracy = ", i+1)
                iter+=1
        if iter==0:
            print("number of series terms required to achieve the specified calculation accuracy is more than 500, or it cannot be reached ")
        print("Arithmetic mean of the series = ", summ/n)
        data = sorted(data)
        if n%2==0:
            print("Median of elements = ", data[len(data)//2-1]+data[len(data)//2])
        else:
            print("Median of elements = ", data[len(data)//2])
        counts = {}
        for x in data:
            if x not in counts:
                counts[x]=0
            counts[x]+=1
        print("Fashion elements= ", max(counts, key=counts.get))
        mean_value = summ/n
        print("Element dispersion = ", sum((x-mean_value)**2 for x in data)/n)
        print("CKO = ", math.sqrt(sum((x-mean_value)**2 for x in data)/n))
    def Calculatex(self, x, n):
        """function for calculate math expression"""
        sum = 0
        xval = float(x)
        for i in range (int(n)):
            sum += (-1)**(i)*(xval)**(i+1)/(i+1)
        return sum
    def function_task1(self):
        """function for task1 """
        while True:
            check=False
            x=0
            n=0
            UserEps=0
            while check == False:
                print("Input float value of x from (-1,1)")
                x = InputFloat()
                check=check_range(x, -1, 1)
                if check==False:
                    print("Incorrect range of x, correct range is (-1,1)")
            check = False
            while check == False:
                print("Input integer value of n (number of iterations) from [1,500]")
                n = InputInt()
                check = check_range_n(n, 1 ,500)
                if check==False:
                    print("Incorrect range of n, correct range is [1,500]")
            check = False
            while check == False:
                print("Input float value of your eps")
                UserEps = InputFloat()
                check = check_range(UserEps, 0, 10 ** 30)
                if check == False:
                    print("Incorrect range of your eps, correct range is [0, inf)")
            self.Calculate(x, 500, float(UserEps)), 15
            print("{:<20} {:<20} {:<20} {:<20} {:<20}". format("X", "N", "F(x)", "Math F(x)", "eps"))
            print("{:<20} {:<20} {:<20} {:<20} {:<20}". format(round(float(x), 15), n, round(self.Calculatex(x, n), 15), round(math.log(float(x)+1), 15),round(abs(self.Calculatex(x, n)-math.log(float(x)+1)), 15)))
            self.graph_math(n)
            print("If you want to stop this task write 'stop', else task will rerun")
            str = input()
            if str == "stop":
                return

    def graph_math(self, n):
        xv = 500
        y = [math.log(1 + x2val+0.000000001) for x2val in np.linspace(-1, 1, int(xv))]
        y2 = [self.Calculatex(x2val, n) for x2val in np.linspace(-1, 1, int(n))]
        # Создание графика
        plt.plot(np.linspace(-1, 1, int(xv)), y, label = 'math lib')
        plt.plot(np.linspace(-1, 1, int(n)), y2, label = 'sum of the series')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of the function ln(1+x) and the sum of the series')
        plt.legend()
        plt.annotate('Point (1, ln(1))', xy=(1, math.log(1)), xytext=(1, math.log(1+50)+0.5))
        plt.xlim(-1, 1)
        plt.ylim(-5, 5)
        plt.savefig('graph.jpg', format = 'jpeg')
        plt.show()

def function_task3():
    task3().function_task1()