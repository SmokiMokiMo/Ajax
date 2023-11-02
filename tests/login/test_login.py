from tests.login.conftest import user_login_fixture
from utils.logger import MyLogger
from framework.login_page import Login


lgn = Login()

def reset_to_initial_state(driver):
    try:
        lgn.log.logger.info("Before resetting app state")
        
        # Get the current package name
        app_package = driver.current_package
        
        # Terminate the app
        driver.terminate_app(app_package)
        
        # Activate the app to relaunch it
        driver.activate_app(app_package)
        
        lgn.log.logger.info("App state reset")
    except Exception as e:
        lgn.log.logger.error(f"An error occurred while resetting the app state: {str(e)}")
        
test_params = {
    'file_path_test_json': 'tests/login/files/test_login_data.json',        
    'file_path_test_login_invalid_json': 'tests/login/files/test_login_invalid.json',
    'file_path_test_burger_json': 'tests/login/files/test_burger.json',
    'file_path_credentials_json': 'tests/login/files/credentials.json',
    'file_path_invalid_credentials_json': 'tests/login/files/invalid_credentials.json'
}
  
def test_user_login(user_login_fixture):       
    try:        
        driver = user_login_fixture          
        login_result = lgn.test_login(driver) 
               
        if login_result:            
            lgn.log.logger.info("Method: [test_user_login] - Login was successful")
            reset_to_initial_state(driver)
            assert login_result is True 
                               
        else:
            lgn.log.logger.error("Method: [test_user_login] - Login failed")
            reset_to_initial_state(driver)
            assert False
                              
    except Exception as e:
        lgn.log.logger.error(f"Method: [test_user_login] - An error occurred: {e}")
        raise
    finally:
        lgn.log.logger.error("Method: [test_user_login] - module 'test_user.py' fixture teardown")     
        
        
        
        
def test_user_login_invalid(user_login_fixture):     
    try:       
        driver = user_login_fixture                          
        login_result = lgn.test_login(driver)
        
        if not login_result:
            lgn.log.logger.error("Method: [test_user_login_invalid] - Login failed")
            reset_to_initial_state(driver)
            assert True
        else:
            lgn.log.logger.info("Method: [test_user_login_invalid] - Login was successful")
            reset_to_initial_state(driver)
            assert login_result is False           
      
    except Exception as e:
        lgn.log.logger.error(f"Method: [test_user_login_invalid] - An error occurred: {e}")
        raise
    finally:
        lgn.log.logger.error("Method: [test_user_login_invalid] - module 'test_user.py' fixture teardown")

def test_user_sidebar(user_login_fixture):       
    try:       
        driver = user_login_fixture        
        login_result = lgn.test_burger(driver)       
        if login_result:
            lgn.log.logger.info("Method: [test_user_sidebar] - Test was successful")
            reset_to_initial_state(driver)
            assert login_result is True
        else:
            lgn.log.logger.error("Method: [test_user_sidebar] - Test failed")            
            assert False
    except Exception as e:
        lgn.log.logger.error(f"Method: [test_user_sidebar] - An error occurred: {e}")
        raise
    finally:
        lgn.log.logger.error("Method: [test_user_sidebar] - module 'test_user.py' fixture teardown")