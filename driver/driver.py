from appium.webdriver.webdriver import WebDriver
from .android_driver import Android
from .ios_driver import iOS
import configparser
import os

project_path = os.path.dirname(os.path.abspath(__file__)).replace(r'driver', '')

cf = configparser.ConfigParser()
cf.read(f'{project_path}/config.ini')

class Driver:
    _driver: WebDriver = None
    _device_type = None

    @classmethod
    def _start(cls):
        device_type = cf.get('Device', 'type')
        if not cls._driver:
            if device_type == 'Android':
                Android.start()
                cls._driver = Android.driver
                cls._device_type = "Android"
            elif device_type == 'iOS':
                iOS.start()
                cls._driver = iOS.driver
                cls._device_type = "iOS"
            else:
                print(f': Not accept device type -> {device_type}')
                raise

