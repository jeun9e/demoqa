import time
from pages.webtables import WebTables


def test_webtables(browser):
    webtables = WebTables(browser)

    webtables.visit()
    assert not webtables.rows_found.exist()

    while webtables.btn_delete.exist():
        webtables.btn_delete.click()
    time.sleep(2)
    assert webtables.rows_found.exist()

# нажать кнопку add, попробовать сохранить пустую форму, проверяем, что окно осталось
    webtables.btn_add.click()
    time.sleep(2)
    webtables.btn_submit.click()
    assert webtables.modal.exist()

# заполнить все поля и нажать кнопку Submit, проверяем, что окно закрылось
    webtables.first_name.send_keys('Ivan')
    webtables.last_name.send_keys('Ivanov')
    webtables.email.send_keys('test@test.ru')
    webtables.age.send_keys('30')
    webtables.salary.send_keys('10000')
    webtables.departament.send_keys('Testing')
    webtables.btn_submit.click()
    time.sleep(2)
    assert not webtables.modal.exist()

# проверяем что строка добавилась
    assert webtables.line.exist()

# кликаем на карандаш, проверяем, что окно с формой открылось, изменяем имя
    webtables.edit.click()
    assert webtables.modal.exist()
    time.sleep(2)
    webtables.first_name.clear()
    time.sleep(2)
    webtables.first_name.send_keys('Testov')
    webtables.btn_submit.click()
# проверяем, что в таблице данные изменились
    assert webtables.first_name_line.get_text() == 'Testov'

# удаляем запись и проверяем, что записей нет
    webtables.btn_delete_1.click()
    assert webtables.rows_found.exist()

