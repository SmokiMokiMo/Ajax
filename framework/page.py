from utils.logger import MyLogger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException

class Page(MyLogger):
    def __init__(self, driver):
        super().__init__()  
        self.driver = driver
        self._time_out: int = 10

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
        
        
    def send_keys_to_element(self, element_name: str, element_ids: dict, keys_to_send: str, by=By.ID, timeout=10) -> bool:
        try:
            element_id = element_ids.get(element_name)
            if element_id:
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, element_id)))
                element.clear()  
                element.send_keys(keys_to_send)
                self.logger.info(f"Method: [send_keys_to_element] - Sent keys '{keys_to_send}' to element '{element_id}'.")
                return True
            else:
                self.logger.error(f"Method: [send_keys_to_element] - Element '{element_name}' not found in element_ids. Element id is {element_id}.")
                return False
        except TimeoutException:
            self.logger.error(f"Method: [send_keys_to_element] - Element '{element_name}' not found within the specified timeout. Element id is {element_id}")
            return False



    def tearDown(self):
        self.driver.quit()