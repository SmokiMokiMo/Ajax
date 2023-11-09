from utils.logger import MyLogger
from framework.page import Page
from utils.file_utils import FilesExtractor
from framework.sidebar_page import SideBar

# The Login class is responsible for automating the login process for an existing user with valid credentials, invalid data, etc...
# It interacts with the application's user interface elements to log in, navigate through the app, and log out.
class Login(Page, MyLogger):


    def __init__(self) -> None:
        super().__init__()
        self.file_extractop = FilesExtractor()      
        self.driver = None
       
        self.data_from_ini_files = self.file_extractop.extract_data_from_ini_files()
        self.sidebar = SideBar()
    
    # Find and click the 'log_in' element  
    def click_log_in_button(self):        
        self.click_element(self.data_from_ini_files['log_in'])
        self.logger.debug(f"Method: [click_log_in_button] - Clicked on: {self.data_from_ini_files[0]} element.")
    
    # Find the 'email_input_field' and send keys
    def set_username(self, username):        
        self.click_element(self.data_from_ini_files['email_input_field'])
        self.send_keys_to_element(self.data_from_ini_files['email_input_field'], username)
        self.logger.debug(f"Method: [set_username] - Cliked on: '{self.data_from_ini_files[1]}' and sended  keys to '{username}'.")
    
    # Find the 'password_input_field' and send keys
    def set_password(self, password):        
        self.click_element(self.data_from_ini_files['password_input_field'])
        self.send_keys_to_element(self.data_from_ini_files['password_input_field'], password)
        self.logger.debug(f"Method: [set_username] - Cliked on: '{self.data_from_ini_files[1]}' and sended  keys to '{password}'.")
    
    # Find and click the 'log_in_confirm' element
    def click_on_button_to_login(self):        
        self.click_element(self.data_from_ini_files['log_in_confirm'],)
        self.logger.debug(f"Method: [test_login] - Clicked on: {self.data_from_ini_files[3]} element.") 

    
    
    
    # Authorization in application
    def login_app(self,username, password):
        self.click_log_in_button()
        self.set_username(username)
        self.set_password(password)
        self.click_on_button_to_login()        
        self.logger.debug(f"Login application successfull!")    


    
    # Authorization of an existing user with invalid data (incorrect password)       
    def test_login_invalid_pass(self, driver, file_path, credentials_path):
        try:            
            credentials, self.data_from_ini_files, element_ids  =  self.preper_data(file_path, credentials_path, self.resourceid)
            page = Page(driver)
            
            # Step 1: Find and click the 'log_in' element
            if page.click_element(self.data_from_ini_files[0], element_ids):
                page.logger.info(f"Clicked on: {self.data_from_ini_files[0]}.")
            
                # Step 2: Find the 'email_input_field' and send keys
                if page.click_element(self.data_from_ini_files[1], element_ids):
                    page.send_keys_to_element(self.data_from_ini_files[1], element_ids, credentials['login'], clear=True)
                    page.logger.info(f"Cliked key: {self.data_from_ini_files[1]} '{element_ids[self.data_from_ini_files[1]]}' and sended  keys to '{credentials['login']}'.")
                      

                    # Step 3: Find the 'password_input_field' and send keys
                    if page.click_element(self.data_from_ini_files[2], element_ids):
                        page.send_keys_to_element(self.data_from_ini_files[1], element_ids, credentials['password'])
                        page.logger.info(f"Cliked key: {self.data_from_ini_files[2]} '{element_ids[self.data_from_ini_files[2]]}' and sended  keys to '{credentials['password']}'.")
            
                        # Step 4: Find and click the 'log_in_confirm' element
                        if page.click_element(self.data_from_ini_files[3], element_ids):
                            page.logger.info(f"Clicked on: {self.data_from_ini_files[3]} element.")
                                                        
                            # Step 5: Find and click the 'burger' element                           
                            if not page.click_element(self.data_from_ini_files[4], element_ids):
                                page.logger.info(f"Clicked on: {self.data_from_ini_files[4]} element.") 
                            
                                page.logger.error(f"Autorization not successful.")
                                return True
                                    
            else:
                page.logger.info("Failed to find or send keys.")
                return False
                   
        except Exception as e:
            self.logger.info(f"Error occurred during login: {e}")
            return False
    
    
    # Checking the presence of Sidebar elements               
    def test_burger(self, driver, file_path, credentials_path):
        
        try:
            credentials, self.data_from_ini_files, element_ids  =  self.preper_data(file_path, credentials_path, self.resourceid)
            
            page = Page(driver)
            
            # Step 1: Find and click the 'log_in' element
            if page.click_element(self.data_from_ini_files[0], element_ids):
                page.logger.info(f"Clicked on: {self.data_from_ini_files[0]}.")
            
                # Step 2: Find the 'email_input_field' and send keys
                if page.click_element(self.data_from_ini_files[1], element_ids):
                    page.send_keys_to_element(self.data_from_ini_files[1], element_ids, credentials['login'], clear=True)
                    page.logger.info(f"Cliked key: {self.data_from_ini_files[1]} '{element_ids[self.data_from_ini_files[1]]}' and sended  keys to '{credentials['login']}'.")
                      

                    # Step 3: Find the 'password_input_field' and send keys
                    if page.click_element(self.data_from_ini_files[2], element_ids):
                        page.send_keys_to_element(self.data_from_ini_files[2], element_ids, credentials['password'])
                        page.logger.info(f"Method: [test_burger] - Cliked key: {self.data_from_ini_files[2]} '{element_ids[self.data_from_ini_files[2]]}' and sended  keys to '{credentials['password']}'.")
            
                        # Step 4: Find and click the 'log_in_confirm' element
                        if page.click_element(self.data_from_ini_files[3], element_ids):
                            page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[3]} element.")
                            
                            # Step 5: Find and click the 'burger' element                           
                            if page.click_element(self.data_from_ini_files[4], element_ids):
                                page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[4]} element.")
                                
                                # Step 6: Find and click the 'app_setings' element                           
                                if page.click_element(self.data_from_ini_files[5], element_ids):
                                    page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[5]} element.")
                                    
                                    # Step 7: Find and click the 'back' element                           
                                    if page.click_element(self.data_from_ini_files[6], element_ids):
                                        page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[6]} element.")
                                        
                                        # Step 8: Find and click the 'burger' element                           
                                        if page.click_element(self.data_from_ini_files[4], element_ids):
                                            page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[4]} element.")
                                        
                                            # Step 9: Find and click the 'help' element                           
                                            if page.click_element(self.data_from_ini_files[7], element_ids):
                                                page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[7]} element.")
                                            
                                                # Step 10: Find and click the 'back' element                           
                                                if page.click_element(self.data_from_ini_files[6], element_ids):
                                                    page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[6]} element.")
                                                    
                                                    # Step 11: Find and click the 'burger' element                           
                                                    if page.click_element(self.data_from_ini_files[4], element_ids):
                                                        page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[4]} element.")

                                                        # Step 12: Find and click the 'help' element                           
                                                        if page.click_element(self.data_from_ini_files[8], element_ids):
                                                            page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[8]} element.")
                                                            
                                                            # Step 13: Find and click the 'swipe' element                           
                                                            if page.swipe(self.swipe_coordinates):
                                                                page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[8]} element.")
                                                                
                                                                # Step 14: Find and click the 'burger' element                           
                                                                if page.click_element(self.data_from_ini_files[4], element_ids):
                                                                    page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[4]} element.")  
                                                                    
                                                                    # Step 15: Find and click the 'add_hub' element                           
                                                                    if page.click_element(self.data_from_ini_files[9], element_ids):
                                                                        page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[9]} element.")
                                                                        
                                                                        # Step 16 Find and click the 'close' element                           
                                                                        if page.click_element(self.data_from_ini_files[12], element_ids):
                                                                            page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[12]} element.")

                                                                            # Step 17: Find and click the 'burger' element                           
                                                                            if page.click_element(self.data_from_ini_files[4], element_ids):
                                                                                page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[4]} element.")
                                                                                
                                                                                # Step 18: Find and click the 'terms_of_service' element                           
                                                                                if page.click_element(self.data_from_ini_files[10], element_ids):
                                                                                    page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[10]} element.") 
                                                                                    
                                                                                    # Step 19 Find and click the 'back' element                           
                                                                                    if page.click_element(self.data_from_ini_files[6], element_ids):
                                                                                        page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[6]} element.")
                                                                                        
                                                                                        # Step 20: Find and click the 'burger' element                           
                                                                                        if page.click_element(self.data_from_ini_files[4], element_ids):
                                                                                            page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[4]} element.")
                                                                                            
                                                                                            # Step 21: Find and click the 'app_setings' element
                                                                                            if page.click_element(self.data_from_ini_files[5], element_ids):
                                                                                                page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[5]} element.")
                                                                                                
                                                                                                # Step 22: Find and click the 'sing_out' element
                                                                                                if page.click_element(self.data_from_ini_files[13], element_ids):
                                                                                                    page.logger.info(f"Method: [test_burger] - Clicked on: {self.data_from_ini_files[13]} element.")
                                                                                                    
                                                                                                    if page.find_element(self.data_from_ini_files[0], element_ids):                                       
                                                                                                        page.logger.info(f"Method: [test_burger] - Autorization successful.")
                                                                                                                                
                                                                                
                                                                                                        page.logger.info(f"Method: [test_burger] - Test successful.")
                                                                                                        return True 
                                    
            else:
                page.logger.error("Method: [test_login_invalid] - Failed to find or send keys.")
                return False
                   
        except Exception as e:
            self.logger.error(f"Method: [test_login_invalid] - Error occurred during login: {e}")
            return False
    
   