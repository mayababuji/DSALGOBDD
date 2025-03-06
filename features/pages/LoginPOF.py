import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from utilities  import excelreader

class LoginPage(PageFactory):

    def __init__(self, driver):
        # It is necessary to initialise driver as page class member to implement Page Factory

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # define locators dictionary where key name will become WebElement using PageFactory
    locators = {
        "getstarted": ("XPATH", '//button[@class="btn"]'),
        "sign_in_button":("LINK_TEXT", 'Sign in'),
        "user_name": ("ID", 'id_username'),
        "password": ("ID",'id_password'),
        "login_button":("XPATH",'//input[contains(@value,"Login")]'),
        "login_success_message_css":("CSS",'div[role="alert"]')

    }

    # Methods to interact with the page
    def click_on_getstarted(self):
        #click_button() methods are extended methods in PageFactory
        self.getstarted.click_button()


    def click_on_signin(self):
        self.sign_in_button.click_button()
    def get_title(self):

        title_attribute = self.driver.title

        return title_attribute
    def click_on_login(self):
        sheetname = 'Login'
        data = excelreader.excelReader(sheetname)
        username = data[0]['Username']
        password = data[0]['password']
        self.user_name.clear_text()
        self.user_name.send_keys(username)
        self.password.clear_text()
        self.password.send_keys(password)
        self.login_button.click_button()
    def validate_login(self):

        log_success_message_element_css = self.login_success_message_css
        log_success_message =  log_success_message_element_css.get_text()
        return log_success_message

