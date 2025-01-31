import time
from pages.links import Links


def test_windows_tab(browser):
    page_links = Links(browser)

    page_links.visit()
    page_links.btn_home.exist()
    assert page_links.btn_home.get_text() == 'Home'
    assert page_links.btn_home.get_dom_attribute('href') == 'https://demoqa.com'
    page_links.btn_home.click()
    time.sleep(4)

    assert len(browser.window_handles) == 2




