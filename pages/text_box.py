from components.components import WebElement
from pages.base_page import BasePage


class TextBox(BasePage):


    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)


        self.first_name_text_box = WebElement (driver, '#userName')
        self.current_address = WebElement (driver, '#currentAddress')
        self.btn_submit = WebElement (driver, '#submit')
        self.check_name_address = WebElement(driver, '//*[@id="output"]/div', 'xpath')