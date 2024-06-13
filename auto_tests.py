import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from config.config import *


class TestLoginPage:
    # def test_pass_onboarding(self, driver):
    #     notification_permission_not_allow_el = driver.find_element(
    #         by=AppiumBy.ID,
    #         value='com.android.permissioncontroller:id/permission_deny_button'
    #     )
    #     notification_permission_not_allow_el.click()
    #
    #     onboarding1_got_it_btn = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.Button[@content-desc="Got it"]'
    #     )
    #     onboarding1_got_it_btn.click()
    #
    #     onboarding2_let_try_btn = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value="""//android.widget.Button[@content-desc="Let's try"]"""
    #     )
    #     onboarding2_let_try_btn.click()
    #
    #     onboarding3_sheeesh_btn = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.Button[@content-desc="Sheeesh!"]'
    #     )
    #     onboarding3_sheeesh_btn.click()

    def test_user_can_go_to_privacy_policy(self, driver):
        privacy_policy_link = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.Button[@content-desc="Privacy Policy"]'
        )
        privacy_policy_link.click()
        privacy_policy_back_btn = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.Button[@content-desc="Back"]'
        )
        privacy_policy_back_btn.click()

    def test_user_can_go_to_terms_conditions(self, driver):
        terms_conditions_link = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.Button[@content-desc="Terms & Conditions"]'
        )
        terms_conditions_link.click()
        terms_conditions_back_btn = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.Button[@content-desc="Back"]'
        )
        terms_conditions_back_btn.click()

    def test_user_can_go_to_how_to_get_username_popup(self, driver):
        how_to_get_username_icon = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.'
                  'widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.'
                  'widget.ImageView/android.view.View/android.widget.ImageView'
        )
        how_to_get_username_icon.click()
        close_how_to_get_username_btn = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.Button[@content-desc="Close it"]'
        )
        close_how_to_get_username_btn.click()

    def test_login_flow(self, driver):
        login_text = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Find your TikTok account"]'
        ).get_attribute('content-desc')
        print(login_text)
        username_field = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.EditText'
        )
        username_field.click()
        username_field.send_keys(USER_NAME)

        search_username_btn = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.Button[@content-desc="Search"]'
        )
        search_username_btn.click()

        check_username_continue_btn = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.Button[@content-desc="Continue"]'
        )
        check_username_continue_btn.click()

        password_field = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.EditText'
        )
        password_field.click()
        password_field.send_keys(PASSWORD)

        log_in_btn = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.Button[@content-desc="Log in"]'
        )
        log_in_btn.click()

    def test_user_can_view_instructions(self, driver):
        for i in range(5):
            instructions_got_it_btn = driver.find_element(
                by=AppiumBy.XPATH,
                value='//android.widget.Button[@content-desc="Got it"]'
            )
            instructions_got_it_btn.click()

    #
    # def test_tap_forgot_password(self, driver):
    #     forgot_password_btn = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.Button[@content-desc="Forgot password?"]'
    #     )
    #     forgot_password_btn.click()


