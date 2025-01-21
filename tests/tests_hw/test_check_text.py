from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_text(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.button.click()
    demo_qa_page.footer.get_text()

    # assert elements_page.text_elements.get_text()