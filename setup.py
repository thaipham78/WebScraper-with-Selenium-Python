from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# This is Selenium version 4
# Set up BrowserDriver
def prepareBrowser():
    # Download chrome driver
    chromeDriver = ChromeDriverManager().install()
    # Config chrome driver
    chromeService = ChromeService(executable_path=chromeDriver)
    browser = webdriver.Chrome(service=chromeService)
    return browser