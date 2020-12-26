import yaml
import os
import configparser
from pages import BasePage

file_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.dirname(os.path.abspath(__file__)).replace(r'pages/clock_page', '')

cf = configparser.ConfigParser()
cf.read(f'{project_path}/config.ini')


class ClockPage(BasePage):
    def __init__(self):
        device_type = cf.get(f'Device', 'type')
        if device_type == 'Android':
            self.eles = yaml.safe_load(open(f'{file_path}/and_eles.yaml'))
        elif device_type == 'iOS':
            self.eles = yaml.safe_load(open(f'{file_path}/ios_eles.yaml'))
        else:
            print('warning: Device type not be defined, default to use Android type.')
            self.eles = yaml.safe_load(open(f'{file_path}/and_eles.yaml'))

    def switch_to_off_office(self):
        self.find_ele(self.eles['tab_off_office']).click()
        return self

    def clock_off(self):
        self.find_ele(self.eles['clock_off_bt']).click()
        return self

    def check_result(self):
        return self.wait_until(self.eles['clock_off_success'], wait_type='exist')
