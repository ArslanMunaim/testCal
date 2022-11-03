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




