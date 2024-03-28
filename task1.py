from functions import check_range_n
from functions import InputInt
from functions import check_range
from functions import InputFloat
import math

def Calculate(x, n, UserEps):
    """doc"""
    sum = 0
    xval = float(x)
    iter = 0
    for i in range (int(n)):
        sum+= (-1)**(i)*(xval)**(i+1)/(i+1)
        if abs(sum-math.log(float(x)+1))<UserEps and iter == 0:
            print ("number of series terms required to achieve the specified calculation accuracy = ", i+1)
            iter+=1
    if iter==0:
        print("number of series terms required to achieve the specified calculation accuracy is more than 500, or it cannot be reached ")
def Calculatex(x, n):
    """doc"""
    sum = 0
    xval = float(x)
    for i in range (int(n)):
        sum += (-1)**(i)*(xval)**(i+1)/(i+1)
    return sum
def function_task1():
    """doc"""
    while True:
        check=False
        x=0
        n=0
        UserEps=0
        while check == False:
            print("Input float value of x from (-1,1)\n")
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
        Calculate(x, 500, float(UserEps)), 15
        print("{:<20} {:<20} {:<20} {:<20} {:<20}". format("X", "N", "F(x)", "Math F(x)", "eps"))
        print("{:<20} {:<20} {:<20} {:<20} {:<20}". format(round(float(x), 15), n, round(Calculatex(x, n), 15), round(math.log(float(x)+1), 15),round(abs(Calculatex(x, n)-math.log(float(x)+1)), 15)))
        print("If you want to stop this task write 'stop', else task will rerun")
        str = input()
        if str == "stop":
            return