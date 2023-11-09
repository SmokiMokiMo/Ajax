from tests.login.conftest import user_login_fixture
import pytest
from framework.sidebar_page import SideBar

class TestLogin(SideBar):
    def __init__():
        super().__init__()

    # Initialize the Appium driver
    test_data = [
        {'username': 'qa.ajax.app.automation@gmail.com', 'password': 'qa_automation_password', 'expected_result': True},
        {'username': 'qa.ajax.app.automation@gmail.com', 'password': 'qa_automation_password_invalid', 'expected_result': False},
    ]

    button_methods = [
        self..click_button_burger,
        self.click_button_app_setings,
        lgn.click_button_back,
        lgn.click_button_burger,
        lgn.click_button_help,
        lgn.click_button_back,
        lgn.click_button_burger,
        lgn.click_button_report_problem,
        lgn.swip_down,
        lgn.click_button_burger,
        lgn.click_button_add_hub,
        lgn.click_button_back,
        lgn.click_button_terms_of_service,
        lgn.click_button_back
    ]

    @pytest.mark.parametrize("test_case", test_data)
    def test_user_login(self, user_login_fixture, test_case):
        try:
            driver = user_login_fixture
            expected_result = test_case['expected_result']       
            if self.lgn.login_app(driver) and self.lgn.log_out():            
                self.reset_to_initial_state(driver)
                assert actual_result == expected_result    

        except Exception as e:
            self.lgn.logger.error(f"An error occurred: {e}")

    @pytest.mark.parametrize("test_case", test_data)
    def test_user_login_invalid_cred(self, user_login_fixture, test_case):
        try:
            driver = user_login_fixture
            expected_result = test_case['expected_result']
            if self.lgn.login_app(driver) and self.lgn.log_out():            
                self.reset_to_initial_state(driver)
                assert actual_result == expected_result    

        except Exception as e:
            self.lgn.logger.error(f"An error occurred: {e}")

    @pytest.mark.parametrize("test_case", test_data)
    def test_side_bar(self, user_login_fixture, test_case):
        try:       
            driver = user_login_fixture
            
            if self.lgn.click_button_burger():
                for button_method in self.button_methods:
                    button_method()          
            else:
                self.lgn.logger.error("Failed to open side bar!")

            login_result = self.lgn.test_login(driver)       
            if login_result:
                self.lgn.logger.info(f"Was successful")
                self.reset_to_initial_state(driver)
                assert login_result is True
            else:
                self.lgn.logger.error(f"Was failed")
                self.reset_to_initial_state(driver)
                assert False

        except Exception as e:
            self.lgn.logger.error(f"An error occurred: {e}")




# Define a function to reset the app to its initial state   
def reset_to_initial_state(driver):
    try:               
        app_package = driver.current_package
                
        driver.terminate_app(app_package)
            
        driver.activate_app(app_package)
            
        lgn.logger.info("App state reset")
    except Exception as e:
        lgn.logger.error(f"An error occurred while resetting the app state: {str(e)}")

# Define the tearDown function
def tearDown(driver):
    driver.quit()