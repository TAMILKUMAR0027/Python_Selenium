import pytest

@pytest.mark.dependency()
def test_create_user():
    print("User Created")


@pytest.mark.dependency(depends=["test_create_user"])
def test_update_user():
    print("User Updated")
@pytest.mark.order(1) 
def test_search(): 
    print("Search")

@pytest.mark.dependency(depends=["test_update_user"])
def test_delete_user():
    print("User Deleted")
