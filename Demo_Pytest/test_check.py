import pytest_check as check

def test_demo():
    print("Start")
    check.equal(1, 3)
    print("next")
    assert 2 == 1
    print("End")