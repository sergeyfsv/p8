import sys
from calc import calculate as cal

def test_calculate(a,b, expected):
    actual = cal(a,b)

    assert actual == expected


test_calculate(10,20, 30)
test_calculate(1,15, 16)
test_calculate(40,150, 190)

test_calculate(0, 100, 101)
test_calculate(sys.float_info.max, 1, sys.float_info.max)