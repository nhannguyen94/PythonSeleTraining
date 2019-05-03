from tests.testcases.test_base import TestBase
from tests.pages.login_page import LoginPage
from tests.pages import login_page
from tests.pages.dashboard_homepage import DashBoardHomePage


class LoginTest(TestBase):
    
    login_page = LoginPage()
    dashboard_homepage = DashBoardHomePage()
    
    
    def test_add_additional_page_012(self):
        username = "administrator"
        password = ""
        self.login_page.open_login_page()        
        self.login_page.login(username, password)
                
        
                
