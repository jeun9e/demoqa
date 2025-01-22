from components.components import WebElement
from pages.base_page import BasePage


class Accordian(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.text_accordian = WebElement (driver, '#section1Content > p')
        self.btn_lorem = WebElement(driver, '#section1Heading')
        self.btn_come = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.btn_come_from = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.btn_use_it = WebElement(driver, '#section3Content > p')

