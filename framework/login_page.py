from utils.logger import MyLogger
from framework.page import Page
from utils.file_utils import FilesExtractor
from framework.sidebar_page import SideBar

# The Login class is responsible for automating the login process for an existing user with valid credentials, invalid data, etc...
# It interacts with the application's user interface elements to log in, navigate through the app, and log out.
class Login(Page, MyLogger):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.file_extractor = FilesExtractor()
        self.driver = driver
        self.data_from_ini_files = None
        self.sidebar = SideBar()
    
    
        self.data_from_ini_files = self.file_extractor.extract_data_from_ini_files()
        
    
    # Find and click the 'log_in' element  
    def click_log_in_button(self) -> bool:        
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
    def login_app(self, username, password) -> bool:
        
        if self.click_log_in_button():
            if self.set_username(username):
                self.set_password(password)
                self.click_on_button_to_login()
                self.logger.debug(f"Login application successfull!")
                return True
        else:
            self.logger.error("Failed to log into app!")
            return False
            