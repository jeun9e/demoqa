from pages.radio import Radio
import pytest

@pytest.mark.skipif(True, reason='просто пропуск')

def test_decor_2(browser):
    radio = Radio(browser)

    radio.visit()
    radio.yes.click_force()
    assert radio.text.get_text() == 'You have selected Yes'

    radio.impressive.click_force()
    assert radio.text.get_text() == 'You have selected Impressive'

    assert 'disabled' in radio.no.get_dom_attribute('class')

