from utils.logger import MyLogger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains

import time
class Page(MyLogger):
    def __init__(self, driver):
        super().__init__()  
        self.driver = driver
        self._time_out: int = 15

    def check_clickable_element(self, element_name, by=By.ID) -> bool:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, element_name)))
            self.logger.info(f"Method: [check_clickable_element] - Element '{element_name}' is clickable.")
            return True
        except TimeoutException:
            self.logger.info(f"Method: [check_clickable_element] - Element '{element_name}' is not clickable or not found.")
            return False

    def find_element(self, element_name: str, element_ids: dict, by=By.ID, timeout=10) -> bool:        
        try:
            element_id = element_ids.get(element_name)
            if element_id:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, element_id)))
                self.logger.info(f"Method: [find_element] - Element key: '{element_name}', value: '{element_id}' was successfully found.")
                return True
            else:
                self.logger.error(f"Method: [find_element] - Element  key: '{element_name}', value: '{element_id}' not found in element_ids. Element id is {element_id}.")
                return False
        except TimeoutException:
            self.logger.error(f"Method: [find_element] - Element key: '{element_name}', value: '{element_id}' not found within the specified timeout.")
            return False

    def click_element(self, element_name: str, element_ids: dict, by=By.ID, timeout=10) -> bool:
        try:
            element_id = element_ids.get(element_name)
            if element_id:
                element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, element_id)))
                element.click()
                self.logger.info(f"Method: [click_element] - Clicked on element key: '{element_name}', value: '{element_id}'.")
                return True
            else:
                self.logger.error(f"Method: [click_element] - Element '{element_name}' not found in element_ids. Element id is {element_id}.")
                return False
        except TimeoutException:
            self.logger.error(f"Method: [click_element] - Element '{element_name}' not clickable or not found. Element id is {element_id}.")
            return False        

        
    def tap_element(self, element_name: str, element_ids: dict, by=By.ID, timeout=10) -> bool:
        try:
            element_id = element_ids.get(element_name)
            if element_id:
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, element_id)))
                action = TouchAction(self.driver)
                action.tap(element).perform()
                self.logger.info(f"Method: [tap_element] - Tapped on element key: '{element_name}', value: '{element_id}'.")
                return True
            else:
                self.logger.error(f"Method: [tap_element] - Element '{element_name}' not found in element_ids. Element id is {element_id}.")
                return False
        except TimeoutException:
            self.logger.error(f"Method: [tap_element] - Element key: '{element_name}', value: '{element_id}' not found within the specified timeout.")
            return False


    def send_keys_to_element(self, element_name: str, element_ids: dict, keys_to_send: str, by=By.ID, timeout=10) -> bool:
        try:
            self.logger.info(f"Method: [send_keys_to_element] - Sent keys '{keys_to_send}'")
            element_id = element_ids.get(element_name)
            if element_id:
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, element_id)))
                
                action = ActionChains(self.driver)
                time.sleep(1)
                element.clear()
                action.send_keys(keys_to_send)
                action.perform()
                self.logger.info(f"Method: [send_keys_to_element] - Sent keys '{keys_to_send}' to element '{element_id}'.")
                return True
            else:
                self.logger.error(f"Method: [send_keys_to_element] - Element '{element_name}' not found in element_ids.")
                return False
        except Exception as e:
            self.logger.error(f"Method: [send_keys_to_element] - An error occurred: {e}")
            return False
        
        
    def swipe(self, coordinats: dict):
        try:
            self.driver.swipe(coordinats['start_x'], coordinats['start_y'], coordinats['end_x'], coordinats['end_y'], 500)
            self.logger.info("Method: [swipe] - Swipe completed successfully.")
            return True
        except Exception as e:
            self.logger.error(f"Method: [swipe] - An error occurred: {e}")
            return False


    
    
    def tearDown(self):
        self.driver.quit()