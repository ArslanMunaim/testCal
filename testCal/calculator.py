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


#import pytest
import pytest

from calculator import add_num
from calculator import sub_num
from calculator import mul_num
from calculator import div_num

def test_add_positives():
    assert add_num(2,3) == 5


def test_add_zero():
    assert add_num(2, 0) == 2


def test_add_negative():
    assert add_num(2, -3) ==  -1


def test_string_expect_exception_firstinput():
    with pytest.raises(TypeError):
        add_num('Random Text' , 4)
        
        
def test_string_expect_exception_secondinput():
    with pytest.raises(TypeError):
        add_num(4,'Random Text')
        
        

        
        








