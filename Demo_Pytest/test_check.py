import pytest_check as check

def test_demo():
    print("Start")
    check.equal(1, 1)
    print("next")
    assert 1== 1
    print("End")