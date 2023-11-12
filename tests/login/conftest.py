import pytest
from tests.conftest import appium_driver
from utils.logger import MyLogger

lgn = MyLogger()
# Logging the appium driver instance in the user_login_fixture method
@pytest.fixture(scope='function')
def user_login_fixture(appium_driver):      
    try:        
        lgn.logger.info(f"Initializing the appium driver: {appium_driver}")
        yield appium_driver
    except Exception as e:
        lgn.logger.error(f"An error occurred during fixture setup: {e}")
        raise
    finally:
        lgn.logger.info("'Terminate app and restart appium server")
        # appium_driver.quit()