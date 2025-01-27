from pages.text_box import TextBox
import time


def test_check_text(browser):
    text_box = TextBox(browser)
    text_box.visit()

    name = 'Test Test_Box'
    address = 'Test street, d.22'
    text_box.first_name_text_box.send_keys(name)
    text_box.current_address.send_keys(address)
    text_box.btn_submit.click()
    time.sleep(2)

    assert text_box.check_name_address.get_text() == ('Name:'+name + '\n'+ 'Current Address :'+address)