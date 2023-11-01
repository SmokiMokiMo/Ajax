#from tests.login.conftest import user_login_fixture
import Page
#from appium import webdriver
from utils.android_utils import AppCapabilitys
from utils.logger import MyLogger
import pytest
import subprocess
import time
#from selenium.common.exceptions import WebDriverException
#from appium.options.android import UiAutomator2Options
import threading
import allure


class LoginPage(Page, MyLogger):
    def __init__(self, driver):
        super().__init__(driver)
        self.log = MyLogger()
        self.page = Page(driver)
        
        
        self.elements = [
        'log_in', 'email_input_field', 'password_input_field', 'log_in_confirm', 'buger',
        'app_setings', 'help', 'report_proble', 'add_hub', 'terms_of_service', 'build_ver']
        
        step = ['log_in', 'email_input_field', 'password_input_field', 'log_in_confirm',
                'buger', 'app_setings', 'help', 'report_proble', 'add_hub', 'terms_of_service', 'build_ver'
        ]
        dict_id = {
        'log_in': 'e6837ae4-b6a5-4c05-973c-fe408802216b', 'email_input_field': 'b04398c8-f5c4-41b0-8bbc-48ec0a80a668', 
        'password_input_field': '10a1dab2-8677-464e-a3de-4be142a3aa47', 'log_in_confirm': '50b959bb-6002-4648-9019-88ec37a6a5b0', 
        'buger': '2c57ca08-e6a4-44b7-8a03-e07cd5f89cbc', 'app_setings': '782c7264-e4cc-47bd-b70e-de1633100121', 
        'help': 'd643b49c-24d7-4803-badb-e442e2c3f2d8', 'report_proble': 'ca253721-4a00-45d1-ba73-295feb307a6c',
        'add_hub': 'ceec55e7-d2e2-422b-ae8b-83593a2b1eb4', 'terms_of_service': '8f5d3c2c-e84f-4b06-bd61-4d0983c7a687',
        'build_ver': 'd7dbebd5-c8ec-4542-9e87-7674acd6b7f4'
        }
        
        self.credentials = {
            "login": "qa.ajax.app.automation@gmail.com",
            "password": "qa_automation_password"
            }
    
    
    def test_login(self) -> bool:
        try:
            
            page = Page(self.driver)
            self.logger.info("Method: [login] - Starting the login process.")

            # Step 1: Find and click the 'log_in' element
            if 'log_in' in self.element_ids:
                if not self.page.click_element('com.ajaxsystems:id/authHelloLogin'):
                    self.logger.error("Failed to click on 'log_in' element.")
                    return False

                # Step 2: Find the 'email_input_field' and send keys
                if 'email_input_field' in self.element_ids:
                    email_input_element = WebDriverWait(self.page.driver, 10).until(
                        EC.presence_of_element_located((By.ID, 'b04398c8-f5c4-41b0-8bbc-48ec0a80a668'))
                    )
                    email_input_element.send_keys(self.credentials['login'])
                else:
                    self.logger.error("Failed to find or send keys to 'email_input_field'.")
                    return False

                # Step 3: Find the 'password_input_field' and send keys
                if 'password_input_field' in self.element_ids:
                    password_input_element = WebDriverWait(self.page.driver, 10).until(
                        EC.presence_of_element_located((By.ID, '10a1dab2-8677-464e-a3de-4be142a3aa47'))
                    )
                    password_input_element.send_keys(self.credentials['password'])
                else:
                    self.logger.error("Failed to find or send keys to 'password_input_field'.")
                    return False

                # Step 4: Find and click the 'log_in_confirm' element
                if 'log_in_confirm' in self.element_ids:
                    if not self.page.click_element('50b959bb-6002-4648-9019-88ec37a6a5b0'):
                        self.logger.error("Failed to click on 'log_in_confirm' element.")
                        return False
                else:
                    self.logger.error("Failed to find 'log_in_confirm' element.")
                    return False            

            return True
        except Exception as e:
            self.logger.error(f"An error occurred during login: {e}")
            return False
        
    def run(self):
        if self.preper_data():
            return True
        else:
            False


@allure.feature("Gmail Login")
class TestGmailLogin:
    lpt = None

    @classmethod
    def setup_class(cls, user_login_fixture):
        if not cls.lpt:
            cls.lpt = LoginPage(user_login_fixture.driver)            

    @pytest.fixture(scope='session', autouse=True)
    def run_appium_server():
        app_cap = AppCapabilitys()
        try:
            appium_process = subprocess.Popen(
                ['appium'],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL,
                shell=True,
                text=True
            )
            # Read and print the stdout from the appium process
            output_reader = threading.Thread(target=app_cap.read_appium_output, args=(appium_process,))
            output_reader.start()

            time.sleep(5)
            allure.logger.debug("Method: [run_appium_server] - timer is over.")

        except Exception as e:
            allure.logger.error(f"Method: [run_appium_server] - Failed to start Appium server: {e}")

    # # Fixture for initializing the Appium driver
    # @pytest.fixture(scope='session')
    # def appium_driver(run_appium_server):
    #     app_cap = AppCapabilitys()
    #     try:
    #         options = UiAutomator2Options()
    #         options.load_capabilities(app_cap.android_get_desired_capabilities())
    #         appium_driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

    #         lpt.logger.info(f"Method: [appium_driver] - Appium driver initialized successfully with desired_caps: {appium_driver}\n")
    #         yield appium_driver
    #     except WebDriverException as e:
    #         lpt.logger.error(f"Method: [appium_driver] - WebDriverException occurred: {e}")
    #     except Exception as e:
    #         allure.logger.error(f"Method: [appium_driver] - An error occurred while setting up the Appium driver: {e}")

    # @pytest.fixture(scope='function')
    # def user_login_fixture(appium_driver):
    #     try:
    #         login_page = LoginPageTest(appium_driver)  # Create an instance of 'LoginPageTest'
    #         login_page.log.logger.info("Running Test1 - [user_login_fixture]: launching login test")
    #         yield login_page
    #     except Exception as e:
    #         allure.logger.exception(f"Method: [user_login_fixture] - Error in fixture setup: {e}")

    # @allure.feature("Your Test Feature")
    # @allure.story("Your Test Story")
    # def test_user_login(self, user_login_fixture):
    #     login_page = user_login_fixture
    #     login_page.log.logger.info("Method: [test_user_login] - Before login")
    #     login_result = login_page.test_login()
    #     login_page.log.logger.info("Method: [test_user_login] - Login was successful")
    #     if not login_result:
    #         login_page.log.logger.error("Method: [test_user_login] - Login failed")
    #         assert False  # This will explicitly fail the test
    #     else:
    #         login_page.log.logger.info("Method: [test_user_login] - Login was successful")