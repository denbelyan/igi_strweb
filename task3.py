from functions import InputStr
from functions import InputStop
def is_16_system(stroke):
    """doc"""
    try:
        int(stroke, 16)
        return True
    except ValueError:
        return False
def check_enter(stroke):
    """doc"""
    if stroke.find(' ')==len(stroke)-1:
        return -1
    return stroke.find(' ')
def function_task3():
    """doc"""
    RunTask = True
    while RunTask==True:
        stroke = InputStr()
        result = is_16_system(stroke)
        if result :
            print("The entered string is a hexadecimal number")
        else:
            print("The entered string is not a hexadecimal number")
        print ("If you want to stop this task write 'stop', else task will rerun")
        str = InputStop()
        if str == False:
            return