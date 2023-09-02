from test_page import OperationsHelper
import logging
import time


def test_step_1_bad_login(browser):
    logging.info("Test_01 Starting...")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_btn()
    time.sleep(2)
    assert testpage.get_error_text() == "401"


def test_step_2_good_login(browser):
    logging.info("Test_02 Starting...")
    testpage = OperationsHelper(browser)
    testpage.enter_login("Ivan1234")
    testpage.enter_pass("416b69ce0b")
    testpage.click_login_btn()
    time.sleep(2)
    assert testpage.get_good_text() == "Hello, Ivan1234"


def test_step_3_new_post(browser):
    logging.info("Test_03 Starting...")
    testpage = OperationsHelper(browser)
    testpage.click_create_btn()
    testpage.enter_title("Test")
    testpage.enter_description("Test")
    testpage.enter_content("Test")
    testpage.enter_data("01.09.2023")
    Imagepath = """D:\\OneDrive\\Рабочий стол\\1234.jpg"""
    testpage.enter_image(Imagepath)
    time.sleep(2)
    testpage.click_send_btn()
    time.sleep(2)
    assert testpage.get_new_post() == "Test"


def test_step_4_cont_us(browser):
    logging.info("Test_04 Starting...")
    testpage = OperationsHelper(browser)
    testpage.click_contact_btn()
    time.sleep(2)
    testpage.enter_name("test")
    testpage.enter_email("1234@test.ru")
    testpage.enter_cont_us("test")
    time.sleep(2)
    testpage.click_cont_us_btn()
    time.sleep(3)
    assert testpage.get_alert() == "Form successfully submitted"

''' 
Запуск тестов с отправкой на email:
pytest -v test_01.py ; python email_report.py
'''