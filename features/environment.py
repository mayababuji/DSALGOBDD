import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from selenium import webdriver
from utilities import configreader
import allure
from allure_commons.types import AttachmentType


def before_all(context):
    """
    This hook runs before all features and scenarios.
    """
    # Access environment variables from behave.ini
    browser = context.config.userdata["browser"]
    os_name = context.config.userdata["os"]
    version = context.config.userdata["version"]
    env = context.config.userdata["env"]

    # Define the path for the environment.properties file
    allure_results_dir = "reports/allure-results"
    os.makedirs(allure_results_dir, exist_ok=True)
    env_file = os.path.join(allure_results_dir, "environment.properties")

    # Write environment variables to the file
    with open(env_file, "w") as f:
        f.write(f"Browser={browser}\n")
        f.write(f"OS={os_name}\n")
        f.write(f"Version={version}\n")
        f.write(f"Environment={env}\n")


def before_scenario(context, scenario):
    """
    This hook runs before each scenario.
    """
    # Example: Initialize a web driver for UI tests
    logger.info(f"Starting scenario: {scenario.name}")
    if "login" in scenario.tags:
        config_file_path = 'utilities/config.ini'
        section = 'DEFAULT'
        key = 'browser'
        browser_name = configreader.read_config(config_file_path, section, key)
        logger.info(f"Opening the browser: {browser_name}")
        if browser_name == 'chrome':
            context.driver = webdriver.Chrome()  # Initialize a Chrome driver
        elif browser_name == 'edge':
            context.driver = webdriver.Edge()
        elif browser_name == 'firefox':
            context.driver = webdriver.Firefox()
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)  # Set implicit wait


def after_step(context, step):
    """
       This hook runs after each step if the step is failed the screenshot is attached.
       """
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      , name="failed_screenshot"
                      , attachment_type=AttachmentType.PNG)


def after_scenario(context, scenario):
    """
    This hook runs after each scenario to clean the resources and close the browser
    """
    logger.info(f"Finished scenario: {scenario.name}")
    context.driver.quit()
