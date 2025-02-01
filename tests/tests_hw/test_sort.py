import time
from pages.webtables import WebTables
from components.components import WebElement

def test_sort(browser):
    webtables = WebTables(browser)

    webtables.visit()

    for head in webtables.sort.find_elements():
        head.click()
        time.sleep(2)

        class_after_click = webtables.sort.get_dom_attribute('class')

        if '-sort' in class_after_click:
            assert True
        else:
            assert False



