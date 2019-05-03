from tests.testcases.test_base import TestBase
from tests.pages.login_page import LoginPage
from tests.pages import login_page


class LoginTest(TestBase):
    
    login_page = LoginPage()
    
    def test_login_001(self):
        username = "administrator"
        password = ""
        self.login_page.open_login_page()        
        self.login_page.login(username, password)
        current_url = login_page.browser.get_driver().current_url
        assert('2f9njff6y9.page' in current_url)
