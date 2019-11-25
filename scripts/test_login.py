import allure
import pytest
class TestLogin:

    # @allure.step(title="输入")
    def test_login1(self):
        # self.driver = driver
        # allure.attach("关键字", "pass")
        assert 1
        # allure.attach("截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    def test_login2(self):
        assert 1

    # @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_login3(self):
        assert 0

    def test_login4(self):
        assert 1


