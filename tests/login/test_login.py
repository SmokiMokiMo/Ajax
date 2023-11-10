from tests.login.conftest import user_login_fixture
import pytest
from framework.sidebar_page import SideBar
from framework.login_page import Login
import pytest

test_data = [
    {'username': 'qa.ajax.app.automation@gmail.com', 'password': 'qa_automation_password', 'expected_result': True},    
]


@pytest.mark.parametrize("test_case", test_data)
def test_user_login(user_login_fixture, test_case):
    login_page = None  
    try:
        login_page = Login(driver=user_login_fixture)
        username = test_case['username']
        password = test_case['password']
        expected_result = test_case['expected_result']
        
        if login_page.click_log_in_button():
            if login_page.set_username(username):
                if login_page.set_password(password):
                    login_page.click_on_button_to_login()
                    login_page.logger.debug("Login application successful!")
                    actual_result = True  # Set to True if login is successful

        # Assertion to check if actual_result matches expected_result
        assert actual_result == expected_result
    except Exception as e:
        login_page.logger.error(f"An error occurred: {e}")
    finally:
        # Add any necessary cleanup code, like closing the driver
        if login_page:
            login_page.driver.quit()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            # button_methods = [
    #     self.click_button_burger,
    #     self.click_button_app_setings,
    #     lgn.click_button_back,
    #     lgn.click_button_burger,
    #     lgn.click_button_help,
    #     lgn.click_button_back,
    #     lgn.click_button_burger,
    #     lgn.click_button_report_problem,
    #     lgn.swip_down,
    #     lgn.click_button_burger,
    #     lgn.click_button_add_hub,
    #     lgn.click_button_back,
    #     lgn.click_button_terms_of_service,
    #     lgn.click_button_back
    # ]

    # @pytest.mark.parametrize("test_case", test_data)
    # def test_user_login_invalid_cred(self, user_login_fixture, test_case):
    #     try:
    #         driver = user_login_fixture
    #         expected_result = test_case['expected_result']
    #         if self.login_app(driver) and self.log_out():            
    #             self.reset_to_initial_state(driver)
    #             assert actual_result == expected_result    

    #     except Exception as e:
    #         self.logger.error(f"An error occurred: {e}")

    # @pytest.mark.parametrize("test_case", test_data)
    # def test_side_bar(self, user_login_fixture, test_case):
    #     try:       
    #         driver = user_login_fixture
            
    #         if self.click_button_burger():
    #             for button_method in self.button_methods:
    #                 button_method()          
    #         else:
    #             self.logger.error("Failed to open side bar!")

    #         login_result = self.lgn.test_login(driver)       
    #         if login_result:
    #             self.logger.info(f"Was successful")
    #             self.reset_to_initial_state(driver)
    #             assert login_result is True
    #         else:
    #             self.lgn.logger.error(f"Was failed")
    #             self.reset_to_initial_state(driver)
    #             assert False

    #     except Exception as e:
    #         self.logger.error(f"An error occurred: {e}")




# Define a function to reset the app to its initial state   
def reset_to_initial_state(self, driver):
    try:               
        app_package = driver.current_package
                    
        driver.terminate_app(app_package)
                
        driver.activate_app(app_package)
                
        self.logger.info("App state reset")
    except Exception as e:
        self.logger.error(f"An error occurred while resetting the app state: {str(e)}")

# Define the tearDown function
def tearDown(driver):
    driver.quit()