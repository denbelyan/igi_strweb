from functions import InputInt
from functions import InputStop

def function_task2():
    """doc"""
    while True:
        arr = []
        i = 0
        summ = 0
        counter = 0
        while i!=10:
            print("Input integer number, to stop you need to input 10")
            inp = InputInt()
            i = int(inp)
            arr.append(i)
            summ+=i
            if i>0:
                counter+=1
        print(" Sum of entered elements = ", summ, "\n", "Number of positive elements = ", counter)
        print("If you want to stop this task write 'stop', else task will rerun")
        str = InputStop()
        if str == False:
            return
