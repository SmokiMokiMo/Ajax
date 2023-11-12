from tests.login.conftest import user_login_fixture
from tests.conftest import appium_driver
import pytest
from framework.sidebar_page import SideBar
from framework.login_page import Login
import pytest

class TestApp:

    # Method to perform the login action.
    def log_in(self, lp, login_test_case) -> bool:
        if lp.click_log_in_button():
            lp.set_username(login_test_case['username'])
            lp.set_password(login_test_case['password'])
            lp.click_on_button_to_login()
            lp.logger.debug("Login application successful!")
            return True
        else:
            lp.logger.error("Login application failed!")
            return False


    # Method to perform the logout action.
    def log_out(self, sbr):
        if sbr.click_burger():
            sbr.click_app_setings()
            sbr.click_sing_out()
            sbr.find_log_in()
            sbr.logger.debug("Log out successful!")
            return True
        else:
            sbr.logger.error("Login application failed!")
            return False
        

    @pytest.mark.parametrize("login_test_valid", [
        {'username': 'qa.ajax.app.automation@gmail.com', 'password': 'qa_automation_password', 'expected_result': True},])
    
    # Test method for user login scenario.
    def test_user_login_valid_data(self, appium_driver, login_test_valid):
        sbr = SideBar(appium_driver)
        lp = Login(appium_driver)
        expected_result = login_test_valid['expected_result']
        try:
            if self.log_in(lp, login_test_valid) and self.log_out(sbr):
                actual_result = True
            else:
                actual_result = False
            
            sbr.logger.info(f"Actual result is - {actual_result}. Expected result is - {expected_result}")
            assert actual_result == expected_result
            
        except AssertionError as ae:
            raise ae
        except Exception as e:
            sbr.logger.error(f"An error occurred: {e}")
       
         
    @pytest.mark.parametrize("login_test_invalid", [
        {'username': '_________qa.ajax.app.automation@gmail.com_________', 'password': 'qa_automation_password', 'expected_result': False},])        
    
    # Test method for user login scenario.
    def test_user_login_invalid_data(self, appium_driver, login_test_invalid):
        sbr = SideBar(appium_driver)
        lp = Login(appium_driver)         
        expected_result = login_test_invalid['expected_result']       
        try:
            if self.log_in(lp, login_test_invalid) and self.log_out(sbr):
                actual_result = True          
            else:                
                actual_result = False
            
            sbr.logger.info(f"Actual result is - {actual_result}. Expected result is - {expected_result}")            
            assert actual_result == expected_result
            
        except AssertionError as ae:
            raise ae 
        except Exception as e:
            sbr.logger.error(f"An error occurred: {e}")
            

    @pytest.mark.parametrize("sidebar_test_case", [
        {'username': 'qa.ajax.app.automation@gmail.com', 'password': 'qa_automation_password', 'expected_result': True,
         'function_list': ['click_burger', 'click_app_setings', 'click_button_back', 'click_burger', 'click_button_help', 'click_button_back',
                            'click_burger', 'click_button_report_problem', 'swip_down', 'click_burger', 'click_button_add_hub',
                            'click_button_close', 'click_burger','click_button_terms_of_service', 'click_button_back']}])
    
    # Test method for sidebar interactions.
    def test_sidebar(self, user_login_fixture, sidebar_test_case):
        sbr = SideBar(user_login_fixture)
        lp = Login(user_login_fixture)
        actual_result = False
        expected_result = sidebar_test_case['expected_result']

        try:
            if self.log_in(lp, sidebar_test_case):
                for button_method in sidebar_test_case['function_list']:
                    try:
                        if not getattr(sbr, button_method)():
                            sbr.logger.error(f"Error while executing {button_method}")
                            actual_result = False
                            break
                    except Exception as e:
                        sbr.logger.error(f"An error occurred during {button_method}: {e}")
                        actual_result = False
                        break
                actual_result = True
            else:
                actual_result = False    
            
            if actual_result:
                if self.log_out(sbr):
                    sbr.logger.debug("Checking items of SideBar successful, try logout!")
                    actual_result = True
                else:
                    sbr.logger.error("Log out unsuccessful!")
                    actual_result = False

            sbr.logger.info(f"Actual result is - {actual_result}. Expected result is - {expected_result}")
            assert actual_result is expected_result

        except (AssertionError, Exception) as ex:
            sbr.logger.error(f"An error occurred: {ex}")
            raise ex