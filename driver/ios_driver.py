from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class iOS:
    driver: WebDriver = None

    @classmethod
    def start(cls):
        ...
