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


def test_string_expect_exception_firstinputAdd():
    with pytest.raises(TypeError):
        add_num('Random Text' , 4)
        
        
def test_string_expect_exception_secondinputAdd():
    with pytest.raises(TypeError):
        add_num(4,'Random Text')
    

def test_add_pushing_limits():
    assert add_num(9999999999, 9999999999) ==  19999999998

    
  
def test_sub_positives():
    assert sub_num (3,2) == 1
    

def test_sub_zero_1():
    assert sub_num (3,0) == 3
    

def test_sub_zero_2():
    assert sub_num (0,3) == -3
 
 
def test_string_expect_exception_firstinputSub():
    with pytest.raises(TypeError):
        sub_num('Random Text' , 4)


def test_string_expect_exception_secondinputSub():
    with pytest.raises(TypeError):
        sub_num(4,'Random Text')
        
    
def test_mul_positives():
    assert mul_num(2,2) == 4
    
 
def test_mul_zero():
    assert mul_num(2, 0) == 0


def test_mul_negative():
    assert mul_num(2, -3) ==  -6


def test_string_expect_exception_firstinputMUL():
    with pytest.raises(TypeError):
        mul_num('Random Text' , 4)


def test_string_expect_exception_secondinputMUL():
    with pytest.raises(TypeError):
        mul_num(4,'Random Text')
    


    



