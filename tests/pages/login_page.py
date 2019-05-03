from selenpy.element.text_box import TextBox
from selenpy.support import browser
from selenpy.element.base_element import BaseElement
from selenpy.support.conditions import be, have


class LoginPage():
    
    _txt_username = TextBox("id=username")
    _txt_password = TextBox("id=password")
    _btn_login = BaseElement("class=btn-login")
    
    def __init__(self):
        pass
    
    def open_login_page(self):
        browser.open_url("http://192.168.188.99/TADashboard/login.jsp")        

    def login(self, username, password):
        self._txt_username.wait_until(be.visible)
        self._txt_username.send_keys(username)
        self._txt_password.send_keys(password)        
        self._btn_login.click()
        self._txt_username.wait_for_invisible(10)
            
    def get_alert_msg(self):
        diaglog = self._driver.switch_to.alert
        msg = diaglog.text
        return msg