import yaml
import os
import configparser
from pages import BasePage
from pages.clock_page import ClockPage

file_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.dirname(os.path.abspath(__file__)).replace(r'pages/workbench_page', '')
print('workbench_page: ', os.path)

cf = configparser.ConfigParser()
cf.read(f'{project_path}/config.ini')

class WorkbenchPage(BasePage):
    def __init__(self):
        device_type = cf.get(f'Device', 'type')
        if device_type == 'Android':
            self.eles = yaml.safe_load(open(f'{file_path}/and_eles.yaml'))
        elif device_type == 'iOS':
            self.eles = yaml.safe_load(open(f'{file_path}/ios_eles.yaml'))
        else:
            print('warning: Device type not be defined, default to use Android type.')
            self.eles = yaml.safe_load(open(f'{file_path}/and_eles.yaml'))

    def goto_clock_page(self):
        self.find_ele(self.eles['clock_off_bt']).click()
        return ClockPage()
