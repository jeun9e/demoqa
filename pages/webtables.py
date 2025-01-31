from pages.base_page import BasePage
from components.components import WebElement

class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables/'
        super().__init__(driver, self.base_url)

        self.rows_found = WebElement (driver, 'div.rt-noData')
        self.btn_delete = WebElement(driver, '[title *= Delete]')
        self.btn_add = WebElement (driver, '#addNewRecordButton')
        self.first_name = WebElement (driver, '#firstName')
        self.last_name = WebElement (driver, '#lastName')
        self.email = WebElement (driver, '#userEmail')
        self.age = WebElement (driver, '#age')
        self.salary = WebElement (driver, '#salary')
        self.departament = WebElement (driver, '#department')
        self.btn_submit = WebElement (driver, '#submit')
        self.modal = WebElement (driver, 'body > div.fade.modal.show > div > div')
        self.edit = WebElement (driver, '#edit-record-1 > svg > path')
        self.btn_delete_1 = WebElement(driver, '#delete-record-1 > svg > path')
        self.line = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div')
        self.first_name_line = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(1)')


        self.row_5 = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select > option:nth-child(1)')
        self.btn_next = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')
        self.btn_previous = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')

        self.sort = WebElement (driver, ".rt-th")
        self.sort_first_name = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div.rt-th.rt-resizable-header.-sort-desc.-cursor-pointer > div.rt-resizable-header-content')