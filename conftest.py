
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from config.config import *

capabilities = ANDROID_13_DEVICE_WIFI
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
appium_server_url = 'http://localhost:4723'


@pytest.fixture(scope="class")
def driver():
    auto_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    auto_driver.implicitly_wait(5)
    notification_permission_not_allow_el = auto_driver.find_element(
        by=AppiumBy.ID,
        value='com.android.permissioncontroller:id/permission_deny_button'
    )
    notification_permission_not_allow_el.click()

    onboarding1_got_it_btn = auto_driver.find_element(
        by=AppiumBy.XPATH,
        value='//android.widget.Button[@content-desc="Got it"]'
    )
    onboarding1_got_it_btn.click()

    onboarding2_let_try_btn = auto_driver.find_element(
        by=AppiumBy.XPATH,
        value="""//android.widget.Button[@content-desc="Let's try"]"""
    )
    onboarding2_let_try_btn.click()

    onboarding3_sheeesh_btn = auto_driver.find_element(
        by=AppiumBy.XPATH,
        value='//android.widget.Button[@content-desc="Sheeesh!"]'
    )
    onboarding3_sheeesh_btn.click()
    yield auto_driver
    if auto_driver:
        auto_driver.quit()
