from task1 import function_task1
from task2 import function_task2
from task3 import function_task3
from task4 import function_task4
from task5 import function_task5
from functions import InputInt

while True:
    print(" 1 -- Run task 1 \n 2 -- Run task 2 \n 3 -- Run task 3 \n 4 -- Run task 4 \n 5 -- Run task 5 ")
    case = InputInt()
    if case=="1":
        print("Task 1 Option 3 -- In accordance with the assignment of your option, create a program to calculate\n the value of a function using a power series expansion of the function.\nSet the precision of calculations eps."
        " Provide a maximum number of iterations equal to 500."
        "\nPrint the number of series terms required to achieve the specified calculation accuracy. \nGet the result in the form of a table")
        function_task1()
    elif case=="2":
        print("In accordance with the assignment of your option, create a program to find the sum of a sequence of numbers.")
        function_task2()
    elif case=="3":
        print("Task 3 opiton 3: \n Determine whether the string entered from the keyboard is a hexadecimal number")
        function_task3()
    elif case=="4":
        print("Given a line of text in which words are separated by spaces and commas. In accordance with the specification of your option, \ncreate a program to analyze the string initialized in the program code:")
        function_task4()
    elif case=="5":
        print("In accordance with the instructions of your option, create a program for processing real lists. The program must contain the following basic functions:"
        "\n1) input of list elements by the user;"
        "\n2) checking the correctness of the entered data;"
        "\n3) implementation of the main task with output of results;"
        "\n4) displaying the list on the screen.")
        function_task5()