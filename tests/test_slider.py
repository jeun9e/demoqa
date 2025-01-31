from selenium.webdriver.common.keys import Keys
from pages.slider import Slider


def test_slider(browser):
    page_slider = Slider(browser)

    page_slider.visit()
    assert page_slider.sliedr.exist()
    assert page_slider.inp.exist()

    while not page_slider.inp.get_dom_attribute('value') == '50':
        page_slider.sliedr.send_keys(Keys.ARROW_RIGHT)

    assert page_slider.inp.get_dom_attribute('value') == '50'
