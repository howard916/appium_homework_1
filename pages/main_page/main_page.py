import yaml
import os
from pages import BasePage
from pages.workbench_page import WorkbenchPage
from pages.contacts_page import ContactsPage

file_path = os.path.dirname(os.path.abspath(__file__))


class MainPage(BasePage):
    def __init__(self):
        if self._device_type == 'Android':
            self.__eles = yaml.safe_load(open(f'{file_path}/and_eles.yaml'))
        elif self._device_type == 'iOS':
            self.__eles = yaml.safe_load(open(f'{file_path}/ios_eles.yaml'))
        else:
            print('warning: Device type not be defined, default to use Android type.')
            self.__eles = yaml.safe_load(open(f'{file_path}/and_eles.yaml'))

    def goto_workbench_page(self):
        self.find_ele(self.__eles['tab_workbench']).click()
        return WorkbenchPage()

    def goto_contacts_page(self):
        self.find_ele(self.__eles['tab_contacts']).click()
        return ContactsPage()
