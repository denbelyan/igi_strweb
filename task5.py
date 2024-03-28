import random
from functions import InputInt
from functions import InputFloat
def print_list(num_list):
    """doc"""
    for i in num_list:
        print(i)
def list_add(num_list):
    """doc"""
    i = 0
    print("How much numbers do you want to add?")
    iterations = InputInt()
    for i in range(int(iterations)):
            num_list.append(float(InputFloat()))
def list_find_max_abs_element(num_list):
    """doc"""
    return max(num_list, key = abs)
def random_add(num_list):
    """doc"""
    check=False
    iterations = 0
    while check == False:
        check=True
        print("How much numbers do you want to add?\n")
        iterations = InputInt()
    for i in range(int(iterations)):
        num_list.append(random.uniform(-100.0, 100.0))
def random_add1(num_list, iterations):
    """doc"""
    for i in range(iterations):
        num_list.append(random.uniform(-100.0, 100.0))
def list_find_sum_before_last_positive(num_list):
    """doc"""
    index = -1
    sum = 0
    idx = 0
    for i in num_list:
        idx+=1
        if i>0:
            index = idx
    if index == -1:
        print("no positive elements in your list")
        return 0
    idx = 0
    for i in num_list:
        idx+=1
        if idx>index:
            return sum
        else:
            sum+=i
    return sum

def function_task5():
    """doc"""
    num_list = list()
    check = True
    random_add1(num_list, 10)
    while check==True:
        print("input number, which function you want to start")
        print(" 1 -- print list\n 2 -- Add numbers in list \n 3 -- Find sum before last positive number\n 4 -- find max abs element \n 5 -- Add random elements \n Other number -- end of this task")
        case = InputInt()
        if case=="1":
            print_list(num_list)
        elif case=="2":
            list_add(num_list)
            print("Element added to list succesfully")
        elif case=="3":
            print("sum before last positive number = ", list_find_sum_before_last_positive(num_list))
        elif case=="4":
            print("max abs element = ", list_find_max_abs_element(num_list))
        elif case=="5":
            random_add(num_list)
            print("Random numbers was added to list")
        else:
            print("End of the task")
            check=False
