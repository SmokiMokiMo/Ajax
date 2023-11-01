from tests.login.conftest import user_login_fixture
from utils.logger import MyLogger
from framework.login_page import Login

def test_user_login(user_login_fixture):   
    log = MyLogger()    
    try:
        log.logger.info("Method: [test_user_login] - Before login")
        lgn = Login()
        driver = user_login_fixture  
        log.logger.info(f"Method: [test_user_login] - Driver is {driver} and its type is {type(driver)}")
        
        # Create an instance of the LoginPage       
        login_result = lgn.test_login(driver)
        log.logger.info("Method: [test_user_login] - Login was successful")
        if not login_result:
            log.logger.error("Method: [test_user_login] - Login failed")
            assert False
        else:
            log.logger.info("Method: [test_user_login] - Login was successful")
            return False
        assert True
    except Exception as e:
        log.logger.error(f"Method: [test_user_login] - An error occurred: {e}")
        raise
    finally:
        log.logger.error("Method: [test_user_login] - module 'test_user.py' fixture teardown")