import pytest
@pytest.mark.parametrize("test_input,expected",[(1,3),(2,4)])
def test_soft_addition(test_input,expected):
     assert test_input+2==expected-1