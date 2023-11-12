from framework.page import Page
from utils.file_utils import FilesExtractor
from utils.logger import MyLogger

class SideBar(MyLogger):

    def __init__(self, driver) -> None:
        super().__init__()        
        self.driver = driver
        self.pg = Page(driver=driver)       
        self.swipe_coordinates: dict = {
            'start_x': 545,
            'start_y': 241,
            'end_x': 570,
            'end_y': 1700,
        }    
                
          
    # Find and click the 'burger' element
    def click_burger(self) -> bool:
        return self.pg.click_element('buger')

    # Find and click the 'app_setings' element
    def click_app_setings(self) -> bool:
        return self.pg.click_element('app_setings')
       

    # Find and click the 'back' element  
    def click_button_back(self)-> bool:
        return self.pg.click_element('back')
    
    
    # Find and click the 'help' element
    def click_button_help(self)-> bool:
        return self.pg.click_element('help')
        
    # Find and click the 'sign_out' element
    def click_sing_out(self)-> bool:
        return self.pg.click_element('sing_out')
 

    # Find and click the 'add_hub' element    
    def click_button_add_hub(self)-> bool:
        return self.pg.click_element('add_hub')
     

    # Find and click the 'terms_of_service' element  
    def  click_button_terms_of_service(self)-> bool:                             
        return self.pg.click_element('terms_of_service')

    # Find and click the 'swipe' element 
    def swip_down(self)-> bool:                              
        return self.pg.swipe(self.swipe_coordinates)     

    # Find and click the 'find_log_in' elemen
    def find_log_in(self) -> bool:
        return self.pg.find_element('log_in')
    
    # Find and click the 'click_button_report_problem' elemen
    def click_button_report_problem(self) -> bool:
        return self.pg.click_element('report_problem')
    
    # Find and click the 'close' elemen
    def click_button_close(self) -> bool:
        return self.pg.click_element('close')  