from pages.text_box import TextBox
import time


def test_placeholder(browser):
    text_box = TextBox(browser)
    text_box.visit()

    assert text_box.first_name_text_box.get_dom_attribute('placeholder') == 'Full Name'