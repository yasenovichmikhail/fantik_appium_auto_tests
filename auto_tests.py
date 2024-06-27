import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from config.config import *


class TestLoginPage:

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

    # def test_user_can_go_to_boost_section(self, driver):
    #     boost_tab = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.ImageView[2]'
    #     )
    #     boost_tab.click()
    #     boost_tab_title = driver.find_element(
    #         by=AppiumBy.ACCESSIBILITY_ID,
    #         value='Boost'
    #     )
    #     boost_title = boost_tab_title.get_attribute('content-desc')
    #     assert boost_title == 'Boost', f"Boost title doesn't match"

    # def test_user_can_go_to_download_section(self, driver):
    #     download_tab = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.ImageView[4]'
    #     )
    #     download_tab.click()
    #     download_tab_title = driver.find_element(
    #         by=AppiumBy.ACCESSIBILITY_ID,
    #         value='Download'
    #     )
    #     download_title = download_tab_title.get_attribute('content-desc')
    #     assert download_title == 'Download', f"Download title doesn't match"

    def test_user_can_go_to_profile_section(self, driver):
        profile_tab = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/'
                  'android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/'
                  'android.view.View[2]/android.widget.ImageView[5]'
        )
        profile_tab.click()
        profile_tab_title = driver.find_element(
            by=AppiumBy.XPATH,
            value='//android.view.View[@content-desc="Profile"]'
        )
        profile_title = profile_tab_title.get_attribute('content-desc')
        assert profile_title == 'Profile', f"Profile title doesn't match"
        time.sleep(5)

    # def test_user_can_go_to_tasks_section(self, driver):
    #     tasks_tab = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.ImageView[1]'
    #     )
    #     tasks_tab.click()
    #     tasks_tab_title = driver.find_element(
    #         by=AppiumBy.ACCESSIBILITY_ID,
    #         value='Tasks'
    #     )
    #     tasks_title = tasks_tab_title.get_attribute('content-desc')
    #     assert tasks_title == 'Tasks', f"Tasks title doesn't match"
    # def test_user_can_go_to_deposit(self, driver):
    #     deposit_btn = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.ImageView[@content-desc="Deposit"]'
    #     )
    #     deposit_btn.click()
    #
    # def test_user_can_buy_coins(self, driver):
    #     coins_pack = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.ImageView[3]'
    #     )
    #     coins_pack.click()
    #     buy_coins_btn = driver.find_element(
    #         by=AppiumBy.ACCESSIBILITY_ID,
    #         value='//android.widget.Button[@content-desc="Buy 500 coins"]'
    #     )
    #     buy_coins_btn.click()
        # tap1_buy_btn = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]'
        # )
        # tap1_buy_btn.click()
        # time.sleep(5)
        # tap1_buy_btn = driver.find_element(
        #     by=AppiumBy.XPATH,
        #     value='//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]'
        # )
        # tap1_buy_btn = tap1_buy_btn.get_attribute('text')
        # print(tap1_buy_btn)
        # time.sleep(7)

    #
    # def test_tap_forgot_password(self, driver):
    #     forgot_password_btn = driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value='//android.widget.Button[@content-desc="Forgot password?"]'
    #     )
    #     forgot_password_btn.click()


