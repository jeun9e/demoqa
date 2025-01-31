import time

from selenium.webdriver.common.keys import Keys
from pages.progress import Progress


def test_progress(browser):
    progress = Progress(browser)

    progress.visit()
    time.sleep(2)
    progress.btn_start_stop.click()

    while True:
        if progress.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            progress.btn_start_stop.click()
            break

    time.sleep(4)
