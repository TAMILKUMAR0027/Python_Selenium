import pytest
@pytest.mark.k1
def test_sample():
    print("Hi")
@pytest.mark.k1
def test_sample1():
    x=1
    y=1
    assert x==1
@pytest.mark.k2
def test_sampe2():
    k="Tamil"
    b="Tamil"
    assert k.__eq__(b)    


@pytest.mark.skip(reason="Feature not implemented")
def test_sample4():
    print("Hi")
@pytest.mark.skipif(1==2,reason="dependencies")
def test_sample6():
    print("Hi")

def test_sample5():
    assert 1 == 1
@pytest.mark.xfail(reason="Assertion error")
def test_sample7():
    assert 1==1