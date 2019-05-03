from selenpy.element.text_box import TextBox
from selenpy.support.conditions import be, have
from selenpy.support import browser
from selenpy.element.base_element import BaseElement


class DashBoardHomePage():
    
    _txt_search = TextBox("name=q")
    _icon_global_setting = BaseElement("class=.mn-setting")

    def __init__(self):
        pass
    
    def select_global_setting(self, setting):
        self._icon_global_setting.click()
        self.find_element()

    def search(self, key_word):
        # self._txt_search.wait_for_visible()
        self._txt_search.wait_until(be.visible)
        self._txt_search.send_keys(key_word)
        self._txt_search.wait_until(have.value(key_word))
