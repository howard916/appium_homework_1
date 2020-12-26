import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from driver import Driver
import yaml
import os

file_path = os.path.dirname(os.path.abspath(__file__))


class BasePage(Driver):
    def find_ele(self, by: list):
        try:
            return self.driver.find_element(*by)
        except:
            # 异常处理机制
            self._handle_exception(by)
            try:
                return self.driver.find_element(*by)
            except:
                print(f': 未找到元素 -> {by}')

    def find_eles(self, by: list):
        return self.driver.find_elements(*by)

    def _handle_exception(self, by):
        # 为了加快判定速度(在find_ele中已经执行过隐式等待5s), 在执行黑名单前默认将隐式等待设置为0
        self.driver.implicitly_wait(0)

        # 遍历黑名单, 如果存在则执行点击操作
        # black_list = yaml.safe_load(open(f'{file_path}/black_list.yaml'))
        # for b_ele in black_list:
        #     if len(self.find_eles(*b_ele)) >= 1:
        #         self.find_ele(*b_ele).click()

        # ui滚动查询方法
        print(':Start scroll find')
        self._ui_scroll_find_ele(by)

        # 恢复隐式等待5s
        self.driver.implicitly_wait(5)

    def wait_until(self, by: list, wait_type='view'):
        # 加快定位速度, 但同时也保证速度不至于过快
        self.driver.implicitly_wait(1)
        try:
            if wait_type == 'view':
                return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(*by))
            elif wait_type == 'click':
                return WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(*by))
            elif wait_type == 'exist':
                # xpath 和 css方式不支持直接在page source中查找
                if by[0] == 'xpath' or by[0] == 'css selector':
                    return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(*by))
                else:
                    return WebDriverWait(self.driver, 5).until(lambda driver: by[1] in driver.page_source)
            else:
                print(f': not except wait_type -> {wait_type}')
                raise

        finally:
            self.driver.implicitly_wait(5)

    def _ui_scroll_find_ele(self, by: list):  # 官方使用uiautomator定位方式
        print(': 执行UI滚动查询')
        by_name = None
        get_by = by[:]
        if get_by[0] == 'id':
            by_name = 'resourceId'
            get_by[1] = self.driver.current_package + ':id/' + get_by[1]

        if get_by[0] == 'class name':
            by_name = 'className'

        if get_by[0] == 'xpath':
            try:
                if "@text" in get_by[1]:
                    mo = re.search(r"@text=[\'\"](.*)[\'\"]", get_by[1], re.M | re.I)
                    get_by[1] = mo.groups()[0]
                    by_name = 'text'
                else:
                    print(': when using xpath to scroll find eles, it only supports "text()" attribute')
            except Exception as e:
                print(f': ui_scroll_find error {e.__class__.__name__}')

        if get_by[0] == 'name':
            by_name = 'text'

        ele_find = None
        if by_name is not None:
            cmd = 'new UiScrollable(new UiSelector().scrollable(true)' \
                  '.instance(0)).scrollIntoView(new UiSelector()' \
                  f'.{by_name}("{get_by[1]}").instance(0));'
            try:
                ele_find = self.driver.find_element_by_android_uiautomator(cmd)
            except:
                pass

            if ele_find:
                print(':Scroll find ele success')
            else:
                print(':Scroll cannot find ele')

        else:
            ele_find = None

        return ele_find
