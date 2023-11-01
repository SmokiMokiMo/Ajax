from utils.logger import MyLogger
import json
import os
from framework.page import Page
from utils.file_utils import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Login(LoginPage):
    def __init__(self):
        super().__init__()
        self.log = MyLogger()
        self.driver = None 
        
        self.file_path_test_json = "tests/login/files/test_login_data.json"
        self.file_path_credentials_json = "tests/login/files/credentials.json"
        self.resourceid = "resource-id"
        self.elements = [
        'log_in', 'email_input_field', 'password_input_field', 'log_in_confirm', 'buger',
        'app_setings', 'help', 'report_proble', 'add_hub', 'terms_of_service', 'build_ver']

        step = ['log_in', 'email_input_field', 'password_input_field', 'log_in_confirm',
                'buger', 'app_setings', 'help', 'report_proble', 'add_hub', 'terms_of_service', 'build_ver'
        ]
        self.dict_id = {
        'log_in': 'com.ajaxsystems:id/authHelloLogin', 'email_input_field': 'b04398c8-f5c4-41b0-8bbc-48ec0a80a668', 
        'password_input_field': '10a1dab2-8677-464e-a3de-4be142a3aa47', 'log_in_confirm': '50b959bb-6002-4648-9019-88ec37a6a5b0', 
        'buger': '2c57ca08-e6a4-44b7-8a03-e07cd5f89cbc', 'app_setings': '782c7264-e4cc-47bd-b70e-de1633100121', 
        'help': 'd643b49c-24d7-4803-badb-e442e2c3f2d8', 'report_proble': 'ca253721-4a00-45d1-ba73-295feb307a6c',
        'add_hub': 'ceec55e7-d2e2-422b-ae8b-83593a2b1eb4', 'terms_of_service': '8f5d3c2c-e84f-4b06-bd61-4d0983c7a687',
        'build_ver': 'd7dbebd5-c8ec-4542-9e87-7674acd6b7f4'
        }
            
    def test_login(self, driver) -> bool:
        try:
            credentials, main_keys, element_ids  =  self.preper_data(self.file_path_test_json, self.file_path_credentials_json, self.resourceid)
            page = Page(driver)
            
            # Step 1: Find and click the 'log_in' element
            if page.click_element(main_keys[0], element_ids):                
            
                # Step 2: Find the 'email_input_field' and send keys
                if page.click_element(main_keys[1], element_ids):
                    page.send_keys_to_element(main_keys[1], element_ids, credentials['login'])
                    #page.logger.info(f"Method: [test_login] - Found key: {main_keys[1]} '{element_ids[main_keys[1]]}' and sended  keys to '{credentials['login']}'.")
                      

                    # Step 3: Find the 'password_input_field' and send keys
                    if page.find_element(main_keys[2], element_ids):
                        page.send_keys_to_element(main_keys[1], element_ids, credentials['password']) 
                        #page.logger.info(f"Method: [test_login] - Found key: {main_keys[2]} '{element_ids[main_keys[2]]}' and sended  keys to '{credentials['password']}'.")
            
                        # Step 4: Find and click the 'log_in_confirm' element
                        if page.click_element(main_keys[3], element_ids):
                            page.logger.info(f"Method: [test_login] - click on {main_keys[3]} element.")
                            page.logger.info(f"Method: [test_login] - autorization successful.")
                            return True
                    
            else:
                page.logger.error("Method: [test_login] - Failed to find or send keys.")
                return False            
                   
        except Exception as e:
            self.log.logger.error(f"Method: [test_login] - Error occurred during login: {e}")
            return False
        return True
        
    def run(self, driver):
        
        self.log.logger.info(f"Nethod run: try run")
        self.driver = driver
        
        if self.preper_data():
            self.log.logger.info(f"Method [run]:")
            return True
        else:
            False



        
        
        
        
        
        # self.credentials = {
        #     "login": "qa.ajax.app.automation@gmail.com",
        #     "password": "qa_automation_password"
        #     }





                      



# if __name__ in '__main__':
#     lp = Login()
#     lp.run()