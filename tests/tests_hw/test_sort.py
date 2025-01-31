import time
from pages.webtables import WebTables
from components.components import WebElement

def test_sort(browser):
    webtables = WebTables(browser)

    webtables.visit()

    for head in webtables.sort.find_elements():
        head.click()
        time.sleep(2)
        rows = webtables.rows_sort.find_elements()


