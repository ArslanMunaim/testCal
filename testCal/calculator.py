# This is a sample Python script.

# this script is a basic calculator which can perform addition, subtraction, division and multiplication
# 25.10.2021 21:21
# ScriptWriter: Arslan

def add_num(a,b):
    return a+b;


def sub_num(a,b):
    return a-b;


def mul_num(a,b):
    return a*b;


def div_num(a,b):
    if(b == 0):
        raise ZeroDivisionError("Divisor must not be Zero")
    return a/b;




if __name__ == '__main__':
    print('Hello! GITHUB Calculator')



        

        
        








