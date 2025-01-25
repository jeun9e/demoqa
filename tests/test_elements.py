from pages.elements_page import ElementsPage


def test_find_elements(browser):
    elemenets_page = ElementsPage(browser)
    elemenets_page.visit()

    assert elemenets_page.btns_first_menu.check_count_elements(count=9)