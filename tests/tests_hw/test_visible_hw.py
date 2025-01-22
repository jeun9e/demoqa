import time

from pages.accordian_page import Accordian


def test_visible_accordian(browser):
    accordian_page = Accordian(browser)

    accordian_page.visit()
    assert accordian_page.text_accordian.visible()
    accordian_page.btn_lorem.click()
    time.sleep(2)
    assert not accordian_page.text_accordian.visible()


def test_visible_accordian_default(browser):
    accordian_page = Accordian(browser)

    accordian_page.visit()
    assert not accordian_page.btn_come.visible()
    assert not accordian_page.btn_come_from.visible()
    assert not accordian_page.btn_use_it.visible()