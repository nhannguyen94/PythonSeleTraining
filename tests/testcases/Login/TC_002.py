from tests.testcases.test_base import TestBase
from tests.pages.login_page import LoginPage
from tests.pages import login_page
from selenium import webdriver


class LoginTest(TestBase):
    
    login_page = LoginPage()
    
    def test_login_001(self):
        username = "incorrect"
        password = "test"
        self.login_page.open_login_page()        
        self.login_page.login(username, password)
        current_url = login_page.browser.get_driver().current_url
        browser = webdriver.Chrome
        alert = browser.switch_to_alert()
        alert.accept()
        assert('logins' in current_url)