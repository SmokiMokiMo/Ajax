from utils.logger import MyLogger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from utils.file_utils import FilesExtractor
from selenium.webdriver.common.action_chains import ActionChains


# Basic modules for working with application objects
class Page(MyLogger):
    def __init__(self, driver=None):
        super().__init__()  
        self.driver = driver
        self.file_extractor = FilesExtractor()
        self._time_out: int = 15
        self.element_data = self.file_extractor.extract_data_from_ini_files()
       
        
    # Checks if an element is clickable within a specified timeout.
    # Returns True if the element is clickable, False otherwise.
    def check_clickable_element(self, element_name: str, by=By.ID) -> bool:
        try:
            element_locator = self.element_data.get(element_name)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, element_locator)))
            self.logger.info(f"Element '{element_locator}' is clickable.")
            return True
            
        except TimeoutException:
            self.logger.error(f"Element '{element_locator}' is not clickable or not found.")
            return False
        

    # Finds an element by its name, clicks it, and logs the result.
    def find_element(self, element_name: str, by=By.ID, timeout=10):
        try:
            element_locator = self.element_data.get(element_name)
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, element_locator)))
            self.logger.info(f"Element '{element_locator}' was successfully found.")
            return True
        except TimeoutException:
            self.logger.error(f"Element '{element_locator}' not found within the specified timeout.")
            return False
        
        
    # Clicks an element by its name and logs the result.
    def click_element(self, element_name) -> bool:
        try:
            element_locator = self.element_data.get(element_name)
            if element_locator:
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, element_locator)))
                element.click()
                self.logger.info(f"Clicked on: '{element_locator}' element.")
                return True
            else:
                self.logger.warning(f"Element '{element_name}' not found in the ini files.")
                return False
        except TimeoutException:
            self.logger.error(f"TimeoutException: Element '{element_locator}' not found within the specified timeout.")
            return False
        except NoSuchElementException:
            self.logger.error(f"NoSuchElementException: Element '{element_locator}' not found on the page.")
            return False
        except Exception as e:
            self.logger.error(f"Error while clicking on the element. Element is '{element_name}' and locator - '{element_locator}'", exc_info=True)
            return False



    # Taps on an element by its name and logs the result.  
    def tap_element(self, element_name: str, by=By.ID, timeout=10) -> bool:
        try:
            element_locator = self.element_data.get(element_name)
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, element_locator)))
            action = TouchAction(self.driver)
            action.tap(element).perform()
            self.logger.info(f"Tapped on element '{element_locator}'.")
            return True           
        except TimeoutException:
            self.logger.error(f"Element '{element_locator}' not found within the specified timeout.")
            return False

  
    # Sends keys to an element and logs the result.
    def send_keys_to_element(self, element_name: str, keys_to_send: str, by=By.ID, timeout=10, clear: bool = True) -> bool:
        try:
            element_locator = self.element_data.get(element_name)            
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, element_locator)))

            if clear:                
                element.clear()
                self.logger.debug(f"Cleared element '{element_locator}'.")
            else:
                self.logger.info(f"Skip input '{element_locator}'.")
                action = ActionChains(self.driver)
                self.driver.press_keycode(123)
                action.perform()               
            
            action = ActionChains(self.driver)            
            action.send_keys(keys_to_send)           
            action.perform()
            self.logger.info(f"Sent keys '{keys_to_send}' to element '{element_locator}'.")
            return True
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            return False
                
     
    # Swipes on the screen based on provided coordinates.   
    def swipe(self, coordinats: dict) -> bool:
        try:
            self.driver.swipe(coordinats['start_x'], coordinats['start_y'], coordinats['end_x'], coordinats['end_y'], 220)
            self.logger.info("Swipe completed successfully.")
            return True
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return False