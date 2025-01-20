from selenium.webdriver.common.by import By


class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator


    def click(self):
        self.find_element().click()


    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)


    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True


    def get_text(self):
        return self.find_element().text
        if get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.':
            return True
        else:
            return False


    def get_text_elements(self):
        return self.find_element().text
        if get_text_elements() == 'Please select an item from left to start practice.':
            return True
        else:
            return False
