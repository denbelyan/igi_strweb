from functions import InputInt
from task5 import task5_test_function
from task2 import function_task2
from task1 import function_task1
from task4 import function_task4
from task3 import function_task3

print("Laboratory work 4, done by Belyan Denis Dmitrievich date 04/26/24")
while True:
    print("1 -- Task 1")
    print("2 -- Task 2")
    print("3 -- Task 3")
    print("4 -- Task 4")
    print("5 -- Task 5")
    case = InputInt()
    if case=="1":
        function_task1()
    elif case=="2":
        function_task2()
    elif case=="3":
        function_task3()
    elif case=="4":
        function_task4()
    elif case=="5":
        task5_test_function()

