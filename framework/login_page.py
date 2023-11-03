from utils.logger import MyLogger
from framework.page import Page
from utils.file_utils import LoginPage


class Login(LoginPage):
    def __init__(self):
        super().__init__()
        self.log = MyLogger()
        self.driver = None         
       
        self.resourceid = "resource-id"
        self.swipe_coordinates = {
            'start_x': 545,
            'start_y': 241,
            'end_x': 570,
            'end_y': 1700,
        }
        
    def test_login(self, driver, file_path, credentials_path) -> bool:
        try:
            credentials, main_keys, element_ids  =  self.preper_data(file_path, credentials_path, self.resourceid)
            page = Page(driver)
            
            # Step 1: Find and click the 'log_in' element
            if page.click_element(main_keys[0], element_ids):
                page.logger.info(f"Method: [test_login] - Clicked on: {main_keys[0]} element.")
                
            
                # Step 2: Find the 'email_input_field' and send keys
                if page.click_element(main_keys[1], element_ids):
                    page.send_keys_to_element(main_keys[1], element_ids, credentials['login'])
                    page.logger.info(f"Method: [test_login] - Cliked key: {main_keys[1]} '{element_ids[main_keys[1]]}' and sended  keys to '{credentials['login']}'.")              

                    # Step 3: Find the 'password_input_field' and send keys
                    if page.click_element(main_keys[2], element_ids):
                        page.send_keys_to_element(main_keys[1], element_ids, credentials['password'])
                        page.logger.info(f"Method: [test_login] - Cliked key: {main_keys[2]} '{element_ids[main_keys[2]]}' and sended  keys to '{credentials['password']}'.")
            
                        # Step 4: Find and click the 'log_in_confirm' element
                        if page.click_element(main_keys[3], element_ids):
                            page.logger.info(f"Method: [test_login] - Clicked on: {main_keys[3]} element.")
                            
                            # Step 4: Find and click the 'burger' element
                            if page.click_element(main_keys[4], element_ids):
                                page.logger.info(f"Method: [test_login] - Clicked on: {main_keys[4]} element.")
                                
                                # Step 5: Find and click the 'app_setings' element
                                if page.click_element(main_keys[5], element_ids):
                                    page.logger.info(f"Method: [test_login] - Clicked on: {main_keys[5]} element.")
                                    
                                    # Step 4: Find and click the 'sing_out' element
                                    if page.click_element(main_keys[6], element_ids):
                                        page.logger.info(f"Method: [test_login] - Clicked on: {main_keys[6]} element.")
                                        
                                        if page.find_element(main_keys[0], element_ids):                                       
                                            page.logger.info(f"Method: [test_login] - Autorization successful.")
                                            return True                          
                                            
            else:
                page.logger.error("Method: [test_login] - Failed to find or send keys.")
                return False
                   
        except Exception as e:
            self.log.logger.error(f"Method: [test_login] - Error occurred during login: {e}")
            return False    
            
    def test_login_invalid_pass(self, driver, file_path, credentials_path):
        try:            
            credentials, main_keys, element_ids  =  self.preper_data(file_path, credentials_path, self.resourceid)
            page = Page(driver)
            
            # Step 1: Find and click the 'log_in' element
            if page.click_element(main_keys[0], element_ids):
                page.logger.info(f"Method: [test_login_invalid_pass] - Clicked on: {main_keys[0]}.")
            
                # Step 2: Find the 'email_input_field' and send keys
                if page.click_element(main_keys[1], element_ids):
                    page.send_keys_to_element(main_keys[1], element_ids, credentials['login'], clear=True)
                    page.logger.info(f"Method: [test_login_invalid_pass] - Cliked key: {main_keys[1]} '{element_ids[main_keys[1]]}' and sended  keys to '{credentials['login']}'.")
                      

                    # Step 3: Find the 'password_input_field' and send keys
                    if page.click_element(main_keys[2], element_ids):
                        page.send_keys_to_element(main_keys[1], element_ids, credentials['password'])
                        page.logger.info(f"Method: [test_login_invalid_pass] - Cliked key: {main_keys[2]} '{element_ids[main_keys[2]]}' and sended  keys to '{credentials['password']}'.")
            
                        # Step 4: Find and click the 'log_in_confirm' element
                        if page.click_element(main_keys[3], element_ids):
                            page.logger.info(f"Method: [test_login_invalid_pass] - Clicked on: {main_keys[3]} element.")
                                                        
                            # Step 5: Find and click the 'burger' element                           
                            if not page.click_element(main_keys[4], element_ids):
                                page.logger.info(f"Method: [test_login_invalid_pass] - Clicked on: {main_keys[4]} element.") 
                            
                                page.logger.error(f"Method: [test_login_invalid_pass] - Autorization not successful.")
                                return True
                                    
            else:
                page.logger.info("Method: [test_login_invalid_pass] - Failed to find or send keys.")
                return False
                   
        except Exception as e:
            self.log.logger.info(f"Method: [test_login_invalid_pass] - Error occurred during login: {e}")
            return False
                                 
    def test_burger(self, driver, file_path, credentials_path):
        
        try:
            credentials, main_keys, element_ids  =  self.preper_data(file_path, credentials_path, self.resourceid)
            
            page = Page(driver)
            
            # Step 1: Find and click the 'log_in' element
            if page.click_element(main_keys[0], element_ids):
                page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[0]}.")
            
                # Step 2: Find the 'email_input_field' and send keys
                if page.click_element(main_keys[1], element_ids):
                    page.send_keys_to_element(main_keys[1], element_ids, credentials['login'], clear=True)
                    page.logger.info(f"Method: [test_burger] - Cliked key: {main_keys[1]} '{element_ids[main_keys[1]]}' and sended  keys to '{credentials['login']}'.")
                      

                    # Step 3: Find the 'password_input_field' and send keys
                    if page.click_element(main_keys[2], element_ids):
                        page.send_keys_to_element(main_keys[2], element_ids, credentials['password'])
                        page.logger.info(f"Method: [test_burger] - Cliked key: {main_keys[2]} '{element_ids[main_keys[2]]}' and sended  keys to '{credentials['password']}'.")
            
                        # Step 4: Find and click the 'log_in_confirm' element
                        if page.click_element(main_keys[3], element_ids):
                            page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[3]} element.")
                            
                            # Step 5: Find and click the 'burger' element                           
                            if page.click_element(main_keys[4], element_ids):
                                page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[4]} element.")
                                
                                # Step 6: Find and click the 'app_setings' element                           
                                if page.click_element(main_keys[5], element_ids):
                                    page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[5]} element.")
                                    
                                    # Step 7: Find and click the 'back' element                           
                                    if page.click_element(main_keys[6], element_ids):
                                        page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[6]} element.")
                                        
                                        # Step 8: Find and click the 'burger' element                           
                                        if page.click_element(main_keys[4], element_ids):
                                            page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[4]} element.")
                                        
                                            # Step 9: Find and click the 'help' element                           
                                            if page.click_element(main_keys[7], element_ids):
                                                page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[7]} element.")
                                            
                                                # Step 10: Find and click the 'back' element                           
                                                if page.click_element(main_keys[6], element_ids):
                                                    page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[6]} element.")
                                                    
                                                    # Step 11: Find and click the 'burger' element                           
                                                    if page.click_element(main_keys[4], element_ids):
                                                        page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[4]} element.")

                                                        # Step 12: Find and click the 'help' element                           
                                                        if page.click_element(main_keys[8], element_ids):
                                                            page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[8]} element.")
                                                            
                                                            # Step 13: Find and click the 'swipe' element                           
                                                            if page.swipe(self.swipe_coordinates):
                                                                page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[8]} element.")
                                                                
                                                                # Step 14: Find and click the 'burger' element                           
                                                                if page.click_element(main_keys[4], element_ids):
                                                                    page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[4]} element.")  
                                                                    
                                                                    # Step 15: Find and click the 'add_hub' element                           
                                                                    if page.click_element(main_keys[9], element_ids):
                                                                        page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[9]} element.")
                                                                        
                                                                        # Step 16 Find and click the 'close' element                           
                                                                        if page.click_element(main_keys[12], element_ids):
                                                                            page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[12]} element.")

                                                                            # Step 17: Find and click the 'burger' element                           
                                                                            if page.click_element(main_keys[4], element_ids):
                                                                                page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[4]} element.")
                                                                                
                                                                                # Step 18: Find and click the 'terms_of_service' element                           
                                                                                if page.click_element(main_keys[10], element_ids):
                                                                                    page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[10]} element.") 
                                                                                    
                                                                                    # Step 19 Find and click the 'back' element                           
                                                                                    if page.click_element(main_keys[6], element_ids):
                                                                                        page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[6]} element.")
                                                                                        
                                                                                        # Step 20: Find and click the 'burger' element                           
                                                                                        if page.click_element(main_keys[4], element_ids):
                                                                                            page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[4]} element.")
                                                                                            
                                                                                            # Step 21: Find and click the 'app_setings' element
                                                                                            if page.click_element(main_keys[5], element_ids):
                                                                                                page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[5]} element.")
                                                                                                
                                                                                                # Step 22: Find and click the 'sing_out' element
                                                                                                if page.click_element(main_keys[13], element_ids):
                                                                                                    page.logger.info(f"Method: [test_burger] - Clicked on: {main_keys[13]} element.")
                                                                                                    
                                                                                                    if page.find_element(main_keys[0], element_ids):                                       
                                                                                                        page.logger.info(f"Method: [test_burger] - Autorization successful.")
                                                                                                                                
                                                                                
                                                                                                        page.logger.info(f"Method: [test_burger] - Test successful.")
                                                                                                        return True 
                                    
            else:
                page.logger.error("Method: [test_login_invalid] - Failed to find or send keys.")
                return False
                   
        except Exception as e:
            self.log.logger.error(f"Method: [test_login_invalid] - Error occurred during login: {e}")
            return False
    
   