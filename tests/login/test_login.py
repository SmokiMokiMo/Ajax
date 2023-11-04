from tests.login.conftest import user_login_fixture
from utils.logger import MyLogger
from framework.login_page import Login
import pytest

lgn = Login()

# Define a dictionary of test parameters
test_params = {
    'test_user_login': {
        'file_path': 'tests/login/files/test_login_data.json',
        'credentials_path': 'tests/login/files/credentials.json',
    },
    'test_login_invalid_pass': {
        'file_path': 'tests/login/files/test_login_invalid.json',
        'credentials_path': 'tests/login/files/invalid_credentials.json',
    },
    'test_user_sidebar': {
        'file_path': 'tests/login/files/test_burger.json',
        'credentials_path': 'tests/login/files/credentials.json',
    },
}


# Use pytest's parametrize decorator to run test functions with different test data
@pytest.mark.parametrize("test_function, test_data", test_params.items())
def test_user_login(user_login_fixture, test_function, test_data):
    try:
        lgn.log.logger.info(f"{test_data}\n\n")
        driver = user_login_fixture

        file_path = test_data['file_path']
        credentials_path = test_data['credentials_path']

        if test_function == 'test_user_login':
            login_result = lgn.test_login(driver, file_path, credentials_path)
        elif test_function == 'test_login_invalid_pass':
            login_result = lgn.test_login_invalid_pass(driver, file_path, credentials_path)
        elif test_function == 'test_user_sidebar':
             login_result = lgn.test_burger(driver, file_path, credentials_path)

        if login_result:
            lgn.log.logger.info(f"Method: [{test_function}] - Was successful")
            reset_to_initial_state(driver)
            assert login_result is True
        else:
            lgn.log.logger.error(f"Method: [{test_function}] - Was failed")
            reset_to_initial_state(driver)
            assert False

    except Exception as e:
        lgn.log.logger.error(f"Method: [{test_function}] - An error occurred: {e}")
        raise
    finally:        
        lgn.log.logger.error(f"Method: [{test_function}] - module 'test_user.py' fixture teardown")
        #tearDown(driver)


# Define the tearDown function
def tearDown(driver):
        driver.quit()


# Define a function to reset the app to its initial state   
def reset_to_initial_state(driver):
    try:               
        app_package = driver.current_package
               
        driver.terminate_app(app_package)
        
        driver.activate_app(app_package)
        
        lgn.log.logger.info("Method: [reset_to_initial_state] - App state reset")
    except Exception as e:
        lgn.log.logger.error(f"Method: [reset_to_initial_state] - An error occurred while resetting the app state: {str(e)}")