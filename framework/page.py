from utils.logger import MyLogger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains


# Basic modules for working with application objects
class Page(MyLogger):
    def __init__(self, driver):
        super().__init__()  
        self.driver = driver
        self._time_out: int = 15
        
        
    # Checks if an element is clickable within a specified timeout.
    # Returns True if the element is clickable, False otherwise.
    def check_clickable_element(self, element_id, by=By.ID) -> bool:
        try:            
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, element_id)))
            self.logger.info(f"Element '{element_id}' is clickable.")
            return True
            
        except TimeoutException:
            self.logger.info(f"Element '{element_id}' is not clickable or not found.")
            return False
        

    # Finds an element by its name, clicks it, and logs the result.
    def find_element(self, element_id: dict, by=By.ID, timeout=10) -> bool:        
        try:           
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, element_id)))
            element.click()
            self.logger.info(f"Method: [find_element] - Element '{element_id}' was successfully found.")
            return True            
        except TimeoutException:
            self.logger.error(f"Method: [find_element] - Element '{element_id}' not found within the specified timeout.")
            return False
        
        
    # Clicks an element by its name and logs the result.
    def click_element(self, element_id: str, by=By.ID, timeout=10) -> bool:
        try:            
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, element_id)))
            element.click()
            self.logger.info(f"Clicked on element '{element_id}'.")
            return True             
        except TimeoutException:
            self.logger.error(f"Element '{element_id}' not clickable or not found.")
            return False        

    # Taps on an element by its name and logs the result.  
    def tap_element(self, element_id: dict, by=By.ID, timeout=10) -> bool:
        try:
            
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, element_id)))
            action = TouchAction(self.driver)
            action.tap(element).perform()
            self.logger.info(f"Tapped on element '{element_id}'.")
            return True           
        except TimeoutException:
            self.logger.error(f"Element '{element_id}' not found within the specified timeout.")
            return False

    
    # Sends keys to an element and logs the result.
    def send_keys_to_element(self, element_id: dict, keys_to_send: str, by=By.ID, timeout=10, clear:bool=False) -> bool:
        try:
            self.logger.debug(f"Sent keys '{keys_to_send}'")           
            if clear is True:
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, element_id)))
                self.logger.info(f"Skip  input '{element_id}'.")
                action = ActionChains(self.driver)                
                self.driver.press_keycode(123)                               
                action.perform()                
                self.logger.info(f"Sent keys '{keys_to_send}' to element '{element_id}'.")
                return True    
                    
            else: 
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, element_id)))
                self.logger.info(f"Clearing element '{element_id}'.")
                action = ActionChains(self.driver)        
                action.send_keys(keys_to_send)
                action.perform()                
                self.logger.info(f"Sent keys '{keys_to_send}' to element '{element_id}'.")
                return True          
                
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return False

     
    # Swipes on the screen based on provided coordinates.   
    def swipe(self, coordinats: dict) -> bool:
        try:
            self.driver.swipe(coordinats['start_x'], coordinats['start_y'], coordinats['end_x'], coordinats['end_y'], 220)
            self.logger.info("Method: [swipe] - Swipe completed successfully.")
            return True
        except Exception as e:
            self.logger.error(f"Method: [swipe] - An error occurred: {e}")
            return False