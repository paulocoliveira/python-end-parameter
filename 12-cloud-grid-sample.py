from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import os
from datetime import datetime

@pytest.fixture(params=["chrome-Windows11", "firefox-macOSVentura"],scope="class")
def driver(request):
    username = os.getenv("LT_USERNAME")
    accessToken = os.getenv("LT_ACCESS_KEY")
    gridUrl = "hub.lambdatest.com/wd/hub"

    if request.param == "chrome-Windows11":
        web_driver = webdriver.ChromeOptions()
        platform = "Windows 11"
        name = "Chrome"
    if request.param == "firefox-macOSVentura":
        web_driver = webdriver.FirefoxOptions()
        platform = "MacOS Ventura"
        name = "Firefox"

    lt_options = {
        "user": username,
        "accessKey": accessToken,
        "build": "monkey patching build",
        "name": "monkey patching test",
        "platformName": platform,
        "w3c": True,
        "browserName": name,
        "browserVersion": "latest",
        "selenium_version": "4.8.0",
    }
    options = web_driver
    options.set_capability('LT:Options', lt_options)

    url = "https://"+username+":"+accessToken+"@"+gridUrl
    
    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    yield driver
    
    driver.quit

def log_test_execution(platform, browser, step, element, action, details):
    with open("cloudgrid.log", "a") as file:
        print("Timestamp", datetime.now(), "Platform", platform, "Browser", browser, "Step #", step, "Element", element, "Action", action, "Details", details, sep=' | ', end=';\n', file=file)

def test_simple_demo_form(driver):
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    platform_name = driver.capabilities['platformName']
    browser_name = driver.capabilities['browserName']

    # Find an input element by its ID and enter text
    input_element = driver.find_element(By.ID, "user-message")
    input_element.send_keys("This is an end parameter text!")
    log_test_execution(platform_name, browser_name, "1", "user-message", "send_keys", "This is an end parameter text!")

    # Find an element by its ID and click on it
    element = driver.find_element(By.ID, "showInput")
    element.click()
    log_test_execution(platform_name, browser_name, "2", "showInput", "click", "")

    # Find an element by its ID and extract its text
    element = driver.find_element(By.ID, "message")
    assert element.text == "This is an end parameter text!"
    log_test_execution(platform_name, browser_name, "3", "message", ".text", "This is an end parameter text!")