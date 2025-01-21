from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_text(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.button.click()
    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    assert elements_page.text_elements.get_text() == 'Please select an item from left to start practice.'