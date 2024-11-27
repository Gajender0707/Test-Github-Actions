from src.maths_operations import add,sub


def test_add():
    assert add(3,8)==11, "addition failed"
    assert add(2,3)==5, "addition failed"



def test_sub():
    assert sub(5,2)==3, "substraction failed"
    assert sub(-1,-8)==-9, "substraction failed"


