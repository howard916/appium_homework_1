import allure
from pages.main_page import MainPage


@allure.feature('打卡功能')
class TestClockOff:
    @classmethod
    def setup_class(cls):
        cls.main_page = MainPage()

    @allure.story('外出打开功能')
    def test_clock_off(self):
        workbench_page = self.main_page.goto_workbench_page()
        clock_page = workbench_page.goto_clock_page()
        clock_page.switch_to_off_office()
        clock_page.clock_off()
        assert clock_page.check_result()
