import yaml
import os
from pages import BasePage

file_path = os.path.dirname(os.path.abspath(__file__))


class AddContactsPage(BasePage):
    def __init__(self):
        if self._device_type == 'Android':
            self.__eles = yaml.safe_load(open(f'{file_path}/and_eles.yaml'))
        elif self._device_type == 'iOS':
            self.__eles = yaml.safe_load(open(f'{file_path}/ios_eles.yaml'))
        else:
            print('warning: Device type not be defined, default to use Android type.')
            self.__eles = yaml.safe_load(open(f'{file_path}/and_eles.yaml'))

    def goto_manual_add_page(self):
        self.find_ele(self.__eles['manual_add_bt']).click()
        return self

    def input_name(self, name):
        self.find_ele(self.__eles['name_box']).send_keys(name)
        return self

    def select_sex(self, sex):
        self.find_ele(self.__eles['sex_select']).click()
        goal_sex_ele = self.__eles['sex_list'][:]
        print(goal_sex_ele)
        goal_sex_ele[1] = goal_sex_ele[1] % sex
        print(goal_sex_ele)
        self.wait_until(goal_sex_ele)
        self.find_ele(goal_sex_ele).click()
        return self

    def input_phone(self, phone):
        self.find_ele(self.__eles['phone_box']).send_keys(phone)
        return self

    def save(self):
        self.wait_until(self.__eles['save_bt'], wait_type='click')
        self.find_ele(self.__eles['save_bt']).click()
        return self

    def check_result(self):
        return self.toast_actions(t_type='text')


