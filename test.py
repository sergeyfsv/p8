from calc import calculate as cal

def test_calculate(a,b):
    c = cal(a,b)

    test_c = a+b

    assert c == test_c


test_calculate(10,20)
test_calculate(1,15)
test_calculate(40,150)

test_calculate(0, 1E-30)
