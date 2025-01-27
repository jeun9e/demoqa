import time
from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testorovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('1111111111')
    form_page.hobbies.click_force()
    form_page.current_address.send_keys('test street')
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)


    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()

    form_page.hobbies.click_force()
    form_page.current_address.send_keys('test street')

# Домашнее задание №10. Задание 3.
def test_state_city(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.btn_state_input.scroll_to_element()
    time.sleep(2)
    form_page.btn_state_input.send_keys('NCR')
    form_page.btn_state_input.send_keys(Keys.ENTER)

    form_page.btn_city_input.send_keys('Delhi')
    form_page.btn_city_input.send_keys(Keys.ENTER)