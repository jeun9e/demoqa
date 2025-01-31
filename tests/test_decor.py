from pages.demoqa import DemoQa
import pytest

@pytest.mark.skip

def test_icon(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    assert demo_qa_page.h5.check_count_elements(count=6)

    for element in demo_qa_page.h5.find_elements():
        assert element.text != ''