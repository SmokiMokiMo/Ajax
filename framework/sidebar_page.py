from framework.page import Page
from utils.file_utils import FilesExtractor
from utils.logger import MyLogger

class SideBar(Page, MyLogger):

    def __init__(self) -> None:
        super().__init__()
        self.file_extractor = FilesExtractor()
        self.driver = None

        self.swipe_coordinates: dict = {
            'start_x': 545,
            'start_y': 241,
            'end_x': 570,
            'end_y': 1700,
        }
           
        #self.data_from_ini_files = self.file_extractor.extract_data_from_ini_files()
                
          
    # Find and click the 'burger' element
    def click_burger(self):        
        self.click_element(self.data_from_ini_files['buger'])
        self.logger.info(f"Clicked on: {self.data_from_ini_files['buger']} element.")

    # Find and click the 'app_setings' element
    def click_app_setings(self):        
        self.click_element(self.data_from_ini_files['app_setings'])
        self.logger.info(f"Clicked on: {self.data_from_ini_files['app_setings']} element.")

    # Find and click the 'back' element  
    def click_button_back(self):                                 
        self.click_element(self.data_from_ini_files['back'])
        self.logger.info(f"Clicked on: {self.data_from_ini_files['back']} element.")

    # Find and click the 'help' element
    def click_help(self):       
        self.click_element(self.data_from_ini_files['help'])
        self.logger.info(f"Clicked on: {self.data_from_ini_files['help']} element.")
        
    # Find and click the 'sign_out' element
    def click_sign_out(self):        
        self.click_element(self.data_from_ini_files['sing_out'])
        self.logger.info(f"Clicked on: {self.data_from_ini_files['sign_out']} element.")

    # Find and click the 'add_hub' element    
    def click_add_hub(self):                               
        self.click_element(self.data_from_ini_files['add_hub'])
        self.logger.info(f"Clicked on: {self.data_from_ini_files['add_hub']} element.")

    def  click_terms_of_service(self):
    # Find and click the 'terms_of_service' element                           
        self.click_element(self.data_from_ini_files['terms_of_service'])
        self.logger.info(f"Clicked on: {self.data_from_ini_files['terms_of_service']} element.")

    def swip_down(self):
    # Find and click the 'swipe' element                           
        self.swipe(self.swipe_coordinates)
        self.logger.info(f"Clicked on: {self.swipe_coordinates} element.")

    # Find and click the 'find_log_in' elemen
    def find_log_in(self):
        self.find_element(self.data_from_ini_files['log_in'])
        self.logger.info(f"Found: {self.data_from_ini_files['log_in']} element.")
        
    
    def log_out(self):
        self.click_burger()
        self.click_app_setings()
        self.click_sign_out()
        self.find_log_in()
        self.logger.debug(f"Log out successfull!")