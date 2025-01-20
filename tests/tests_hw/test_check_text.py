from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_text(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    # assert demo_qa_page.equal_url()
    # assert demo_qa_page.icon.exist()
    assert demo_qa_page.footer.get_text()
    demo_qa_page.button.click()
    assert demo_qa_page.footer.get_text()
    assert elements_page.text_elements.get_text_elements()