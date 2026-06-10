import pytest

from actions.ProductPageAction import ProductPageAction
from actions.HomepageAction import HomePageAction


class TestAddTooCart:
    @pytest.mark.usefixtures("setup_and_teardown")
    def test_add_to_cart(self):
        ha=HomePageAction(self.driver,self.wait)
        ppa=ProductPageAction(self.driver,self.wait)
        ha.clickProduct()
        ppa.clickAddtoCart()
        print(ppa.getSuccessMessage())