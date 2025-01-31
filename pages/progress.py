from pages.base_page import BasePage
from components.components import WebElement

class Progress(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        super().__init__(driver, self.base_url)

        self.btn_start_stop = WebElement (driver, '#startStopButton')
        self.progress_bar = WebElement(driver, '#progressBar > div')


