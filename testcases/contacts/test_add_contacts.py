import pytest
import allure
import yaml
import os
from pages.main_page import MainPage

file_path = os.path.dirname(os.path.abspath(__file__))
test_data = yaml.safe_load(open(f'{file_path}/data.yaml'))

@allure.feature("联系人添加")
class TestAddContacts:
    @classmethod
    def setup_class(cls):
        cls.contact_page = MainPage().goto_contacts_page().goto_add_contacts_page()

    @allure.title("手动添加联系人")
    @pytest.mark.parametrize('name, sex, phone', test_data['add_contacts']['data'],
                             ids=test_data['add_contacts']['ids'])
    def test_manual_add_contacts(self, name, sex, phone):
        self.contact_page.goto_manual_add_page()
        self.contact_page.input_name(name)
        self.contact_page.select_sex(sex)
        self.contact_page.input_phone(phone)
        self.contact_page.save()
        assert self.contact_page.check_result() == "添加成功"
