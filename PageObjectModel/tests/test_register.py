import pytest

from actions.SuccessAction import SuccessAction
from actions.RegisterAction import RegisterAction
from actions.HomepageAction import HomePageAction


class TestRegister:
    @pytest.mark.usefixtures("setup_and_teardown")
    def test_register(self):
        ha=HomePageAction(self.driver,self.wait)
        ra=RegisterAction(self.driver,self.wait)
        sa=SuccessAction(self.driver,self.wait)
        ha.clickMyAccount()
        ha.clickRegister()
        ra.set_firstName()
        ra.set_lastName()
        ra.set_email()
        ra.set_phone()
        ra.set_password()
        ra.set_repassword()
        ra.clickChechBox()
        ra.clickContinue()
        assert 'Your Account Has Been Created!'== sa.get_created_test()
        print(sa.get_created_test())
        
        