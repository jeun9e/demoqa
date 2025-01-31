from components.components import WebElement
from pages.base_page import BasePage


class Alerts(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.btn_alert = WebElement(driver, '#alertButton')
        self.btn_confirm =WebElement(driver, '#confirmButton')
        self.confirmResult = WebElement(driver, '#confirmResult')
        self.btn_promt = WebElement (driver, '#promtButton')
        self.promtResult = WebElement(driver, '#promptResult')

        self.btn_time_alert = WebElement(driver, '#timerAlertButton')

