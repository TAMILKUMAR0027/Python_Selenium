import pytest

from actions.HomepageAction import HomePageAction
from actions.LoginPageAction import LoginPageAction
from actions.MyAccountAction import MyAccountAction


class TestLogin:
    @pytest.mark.usefixtures("setup_and_teardown")
    def test_login(self):
        hpa=HomePageAction(self.driver,self.wait)
        lpa=LoginPageAction(self.driver,self.wait)
        maa=MyAccountAction(self.driver,self.wait)
        hpa.clickMyAccount()
        hpa.clickLogin()
        lpa.set_email()
        lpa.set_password()
        lpa.clickLogin()
        assert "My Account"==maa.getAccountMessage()
        