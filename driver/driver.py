from appium.webdriver.webdriver import WebDriver
from .android_driver import Android
from .ios_driver import iOS
import configparser
import os

project_path = os.path.dirname(os.path.abspath(__file__)).replace(r'driver', '')

cf = configparser.ConfigParser()
cf.read(f'{project_path}/config.ini')

class Driver:
    driver: WebDriver = None

    @classmethod
    def start(cls):
        device_type = cf.get('Device', 'type')
        if not cls.driver:
            if device_type == 'Android':
                Android.start()
                cls.driver = Android.driver
            elif device_type == 'iOS':
                iOS.start()
                cls.driver = iOS.driver
            else:
                print(f': Not accept device type -> {device_type}')
                raise

