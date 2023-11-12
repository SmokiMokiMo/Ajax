from utils.logger import MyLogger
from framework.page import Page


# The Login class is responsible for automating the login process for an existing user with valid credentials, invalid data, etc...
# It interacts with the application's user interface elements to log in, navigate through the app, and log out.
class Login(MyLogger):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver  
        self.pg = Page(driver=driver)
              
    
    # Find and click the 'log_in' element  
    def click_log_in_button(self) -> bool:         
        return self.pg.click_element('log_in')          
        
        
    # Find the 'email_input_field' and send keys
    def set_username(self, username) -> bool:
        # Using 'click_element' to make sure the input field is focused before sending keys
        return self.pg.click_element('email_input_field') and self.pg.send_keys_to_element('email_input_field', username)                    

        
    # Find the 'password_input_field' and send keys
    def set_password(self, password) -> bool:
        # Using 'click_element' to make sure the input field is focused before sending keys
        return self.pg.click_element('password_input_field') and self.pg.send_keys_to_element('password_input_field', password)        

    
    # Find and click the 'log_in_confirm' element
    def click_on_button_to_login(self) -> bool:
        return self.pg.check_clickable_element('log_in_confirm') and self.pg.click_element('log_in_confirm')