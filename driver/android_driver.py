from appium import webdriver
from appium.webdriver.webdriver import WebDriver
import configparser
import os

project_path = os.path.dirname(os.path.abspath(__file__)).replace(r'driver', '')

cf = configparser.ConfigParser()
cf.read(f'{project_path}/config.ini')


class Android:
    driver: WebDriver = None

    @classmethod
    def start(cls):
        caps = dict()
        caps['platformName'] = 'android'
        caps['deviceName'] = cf.get('Android', 'deviceName')
        caps['appPackage'] = cf.get('Android', 'appPackage')
        caps['appActivity'] = cf.get('Android', 'appActivity')
        caps['noReset'] = 'true'
        caps['autoGrantPermissions'] = 'true'
        caps['settings[waitForIdleTimeout]'] = 0

        # 判断当driver为空时, 则启动driver, 不为空时, 则忽略
        if not cls.driver:
            host = cf.get('Appium', 'host')
            port = cf.get('Appium', 'port')
            cls.driver = webdriver.Remote(f'http://{host}:{port}/wd/hub', caps)
            cls.driver.implicitly_wait(5)
