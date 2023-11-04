import pytest
from tests.conftest import appium_driver
from utils.logger import MyLogger


# Logging the appium driver instance in the user_login_fixture method
@pytest.fixture(scope='function')
def user_login_fixture(appium_driver):      
    try:
        lgn = MyLogger()
        lgn.logger.info(f"Method: [user_login_fixture] - Initializing the appium driver: {appium_driver}")
        yield appium_driver
        
    except Exception as e:
        lgn.logger.error(f"Method: [user_login_fixture] - An error occurred during fixture setup: {e}")
        raise
    finally:          
        lgn.logger.info("Method: [user_login_fixture] - 'Login' fixture teardown")
        #tearDown(driver)