import yaml
import os
import configparser
from pages import BasePage
from pages.workbench_page import WorkbenchPage

file_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.dirname(os.path.abspath(__file__)).replace(r'pages/main_page', '')

cf = configparser.ConfigParser()
cf.read(f'{project_path}/config.ini')


class MainPage(BasePage):
    def __init__(self):
        device_type = cf.get('Device', 'type')
        if device_type == 'Android':
            self.eles = yaml.safe_load(open(f'{file_path}/and_eles.yaml'))
        elif device_type == 'iOS':
            self.eles = yaml.safe_load(open(f'{file_path}/ios_eles.yaml'))
        else:
            print('warning: Device type not be defined, default to use Android type.')
            self.eles = yaml.safe_load(open(f'{file_path}/and_eles.yaml'))

    def goto_workbench_page(self):
        self.find_ele(self.eles['tab_workbench']).click()
        return WorkbenchPage()
