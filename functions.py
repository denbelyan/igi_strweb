
def my_decorator(func):
    """doc"""
    def wrapper(stroke):
        print("Checking for correct input...")
        if func(stroke)==-1:
            print("Input is correct")
            return wrapper
        print("Input is incorrect")
        raise ValueError("")
    return wrapper

@my_decorator
def check_enter(stroke):
    """doc"""
    if stroke.find(' ')==len(stroke)-1:
        return -1
    return stroke.find(' ')
def InputInt():
    while True:
        inp = input("Input integer number\n")
        try:
            int(inp)
        except:
            print("Incorrect input, please enter integer number")
            continue
        try:
            check_enter(inp)
        except:
            print("Incorrect input, please enter integer number")
            continue
        return inp

def InputFloat():
    while True:
        inp = input("Input float number\n")
        try:
            float(inp)
        except:
            print("Incorrect input, please enter float number")
            continue
        try:
            check_enter(inp)
        except:
            print("Incorrect input, please enter integer number")
            continue
        return inp

def InputStop():
    str = input()
    if str == "stop":
        return False
    return True

def InputStr():
    stroke = "ffff"
    Check = True
    while Check:
        print("Input string ")
        stroke = input()
        try :
            check_enter(stroke)
        except:
            continue
        Check = False
    return stroke

def check_range(x, lower , upper):
    """doc"""
    if upper>float(x)>lower:
        return True
    return False

def check_range_n(n, lower, upper):
    """doc"""
    if upper>=int(n)>=lower:
        return True
    return False