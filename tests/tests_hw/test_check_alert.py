import time
from pages.alerts import Alerts


def test_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.btn_time_alert.click()
    time.sleep(8)
    assert alert_page.alert()
    alert_page.alert().accept()