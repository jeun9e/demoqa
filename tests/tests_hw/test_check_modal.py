from pages.modal_dialogs import ModalDialogs
import time


def test_check_modal(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()
    assert modal_dialogs.large_modal.exist()
    assert modal_dialogs.small_modal.exist()
    modal_dialogs.large_modal.click()
    time.sleep(2)
    assert modal_dialogs.modal_windows.exist()
    modal_dialogs.close_large_modal.click()
    assert not modal_dialogs.modal_windows.exist()
    time.sleep(2)
    modal_dialogs.small_modal.click()
    assert modal_dialogs.modal_windows.exist()
    modal_dialogs.close_small_modal.click()
    assert not modal_dialogs.modal_windows.exist()



