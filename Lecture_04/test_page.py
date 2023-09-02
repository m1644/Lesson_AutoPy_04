from base_app import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:

    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["XPATH"].keys():
        ids[locator] = (By.XPATH, locators["XPATH"][locator])
    for locator in locators["CSS"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["CSS"][locator])
        


class OperationsHelper(BasePage):

    def enter_text_info_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f'We find text "{text}" in field {element_name}')
        return text

# ENTER TEXT
    def enter_login(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def enter_title(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_TITLE_FIELD"], word, description="title form")

    def enter_description(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION_FIELD"], word, description="description form")

    def enter_content(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTENT_FIELD"], word, description="content form")

    def enter_data(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_DATA_FIELD"], word, description="data form")

    def enter_image(self, file):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_IMAGE_FIELD"], file, description="image form")

    def enter_name(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_NAME_FIELD"], word, description="name form")

    def enter_email(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_EMAIL_FIELD"], word, description="email form")

    def enter_cont_us(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONT_US_FIELD"], word, description="content form")

# CLICK BUTTON
    def click_login_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_send_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SEND_BTN"], description="send")

    def click_create_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_BTN"], description="create")

    def click_contact_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="CONTACT")

    def click_cont_us_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONT_US_BTN"], description="CONTACT US")

# GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error text")

    def get_good_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_GOOD_FIELD"], description="good text")

    def get_new_post(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_SEND_FIELD"], description="new post text")

    def get_alert(self):
        text = self.get_alert_text()
        logging.info(f'Get alert text "{text}" to alert')
        return text
