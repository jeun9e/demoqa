from selenium.webdriver.common.by import By
from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://demoqa.com")

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")


footer = driver.find_element(By.CSS_SELECTOR, '#permanentAddress-label').text

print(footer)
