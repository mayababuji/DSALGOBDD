import logging
import time

from behave import given
from behave import when
from behave import then

from selenium import webdriver

from utilities import configreader
from utilities import excelreader

from features.pages.LoginPOF import LoginPage


@given(u'The user is on the DS Algo Home Page')
def openDSAlgoPortal(context):
    file_path = 'utilities/config.ini'
    section = 'DEFAULT'
    key = 'application_url'
    value = configreader.read_config(file_path, section, key)
    application_url = value.lstrip('"').rstrip('"')
    logging.info("The application url is: {application_url}")
    context.driver.get(application_url)


@when(u'The user should click the Sign in link')
def clickOnSignIn(context):
    signin = LoginPage(context.driver)
    signin.click_on_getstarted()
    signin.click_on_signin()
    logging.info("User is clicked in Signin Button")


@then(u'The user should be redirected to Sign in page and the title of the page should be "{title_page}"')
def validateLoginPage(context, title_page):
    signin = LoginPage(context.driver)
    actual_title = signin.get_title()
    expected_title = title_page
    assert expected_title == actual_title
    logging.info(f"The expected and actual result of page title is same")
    logging.info("The expected title is: expected_title = {} and actual title is actual_title = {}".format(
        expected_title, actual_title))


@then(u'The user should be able to able to login with valid credentials and verify the results')
def loginWithValidCredentials(context):
    sheetname = 'Login'
    data = excelreader.excelReader(sheetname)
    expected_result = data[0]['Expected Message']
    signin = LoginPage(context.driver)
    signin.click_on_login()
    login_success_message = signin.validate_login()
    logging.info("The expected message is: expectedresult = {} and actual message is  logsuccessmessage = {}".format(
        expected_result, login_success_message))
    assert expected_result == login_success_message
