from pages.text_box import TextBox
import time


def test_clear(browser):
    text_box = TextBox(browser)
    text_box.visit()

    text_box.first_name_text_box.send_keys('test_text_box')
    time.sleep(2)
    text_box.first_name_text_box.clear()
    time.sleep(2)
    assert text_box.first_name_text_box.get_text() == ''