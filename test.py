from script import sum, devide

def test_sum():
    a = 1
    b = 2
    result = 3
    assert sum(a, b) == result 

def test_devide():
    a = 2
    b = 4
    result = 0.5
    assert devide(a, b) == result

def test_devision_prohibited():
    try:
        devide([1,2,3], [4,5,6])
        print("Test list-division failed")
        assert False
    except:
        print("Test list-division passed")

def test_devide_zero():
    a = 2
    b = 0
    try:
        sum(a, b)
        assert False
    except ValueError as e:
        print("Test (zero-devision) passed")
    

if __name__ == "__main__":
    test_devide()
    test_sum()
    test_devision_prohibited()


