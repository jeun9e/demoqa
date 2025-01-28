import time
from pages.webtables import WebTables


def test_webtables_2(browser):
    webtables = WebTables(browser)

    webtables.visit()

# Добавляем 4 запись
    webtables.btn_add.click()
    webtables.first_name.send_keys('Ivan')
    webtables.last_name.send_keys('Ivanov')
    webtables.email.send_keys('test@test.ru')
    webtables.age.send_keys('30')
    webtables.salary.send_keys('10000')
    webtables.departament.send_keys('Testing')
    webtables.btn_submit.click()

# Добавляем 5 запись
    webtables.btn_add.click()
    webtables.first_name.send_keys('Ivan')
    webtables.last_name.send_keys('Ivanov')
    webtables.email.send_keys('test@test.ru')
    webtables.age.send_keys('30')
    webtables.salary.send_keys('20000')
    webtables.departament.send_keys('Testing')
    webtables.btn_submit.click()
    time.sleep(5)

# меняем количество строк
    webtables.row_5.click()

    assert webtables.btn_next.get_dom_attribute('disabled')
    assert webtables.btn_previous.get_dom_attribute('disabled')

# Добавляем 6 запись
    webtables.btn_add.click()
    webtables.first_name.send_keys('Ivan')
    webtables.last_name.send_keys('Ivanov')
    webtables.email.send_keys('test@test.ru')
    webtables.age.send_keys('30')
    webtables.salary.send_keys('30000')
    webtables.departament.send_keys('Testing')
    webtables.btn_submit.click()


# Добавляем 7 запись
    webtables.btn_add.click()
    webtables.first_name.send_keys('Ivan')
    webtables.last_name.send_keys('Ivanov')
    webtables.email.send_keys('test@test.ru')
    webtables.age.send_keys('30')
    webtables.salary.send_keys('40000')
    webtables.departament.send_keys('Testing')
    webtables.btn_submit.click()


# Добавляем 8 запись
    webtables.btn_add.click()
    webtables.first_name.send_keys('Ivan')
    webtables.last_name.send_keys('Ivanov')
    webtables.email.send_keys('test@test.ru')
    webtables.age.send_keys('30')
    webtables.salary.send_keys('40000')
    webtables.departament.send_keys('Testing')
    webtables.btn_submit.click()
    time.sleep(2)

    webtables.btn_next.click()
    time.sleep(4)
    webtables.btn_previous.click()


