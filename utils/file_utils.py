from utils.logger import MyLogger
import json


# This class encapsulates methods for handling JSON data and preparing data for user login tests.
class LoginPage():    
    # Initialize the logger
    def __init__(self):        
        self.log = MyLogger() 
        
             
    # Extract keys from a JSON string and return them as a list.  
    def get_keys_from_json(self, json_values) -> list:
        try:            
            data = json.loads(json_values)
            keys = list(data.keys())
            self.log.logger.info(f"Method: [get_keys_from_json] - Data extracted list of keys: {keys}")
            return keys
        except (json.JSONDecodeError, AttributeError) as e:
            self.log.logger.error(f"Method: [get_keys_from_json] got error: {e}")
            
        
    # Extract resource IDs from JSON data based on main keys and expected values.          
    def get_resource_id_from_json(self, main_keys, json_data, expected_values):        
        try:
            if isinstance(json_data, str):
                json_data = json.loads(json_data)
            
            resource_ids = {}

            for key in main_keys:
                if key in json_data:
                    element_data = json_data[key]
                    resource_id = None

                    for item in element_data:
                        if item['key'] == expected_values:
                            resource_id = item['value']
                            break
                    resource_ids[key] = resource_id
                else:
                    pass

            self.log.logger.info(f"Method: [get_resource_id_from_json] - Data extracted dict: {resource_ids}")
            return resource_ids
        except Exception as e:
            self.log.logger.error(f"Method: [get_resource_id_from_json] - got error: {e}")
            
    
    # Prepare test data by opening and extracting data from JSON files. 
    def preper_data(self, file_path_test_json, file_path_credentials_json, resourceid):
        try:          
            json_data = self.open_json_file(file_path_test_json)
            self.log.logger.debug(f"Method: [data preparation] - Opened successfully JSON with test_login_data.json 'json_data'")          
            credentials:dict = json.loads(self.open_json_file(file_path_credentials_json))
            self.log.logger.debug(f"Method: [data preparation] - Opened successfully JSON with credentials.json {credentials}")
            main_keys:list = self.get_keys_from_json(json_data)  
            self.log.logger.info(f"Method: [data preparation] - extracted data 'main_keys' is: {main_keys}")
            element_ids = self.get_resource_id_from_json(main_keys, json_data, resourceid)  
            self.log.logger.info(f"Method: [data preparation] - extracted data 'element_ids' is: {element_ids}")
            return credentials, main_keys, element_ids
        
        except Exception as e:
            self.log.logger.error(f"Method: [data preparation] - returned error '{e}'")
            
            
    # Open and read the contents of a JSON file.
    def open_json_file(self, file_path):     
        try:
            with open(file_path, mode='r', encoding='UTF-8') as file:
                data_from_file = file.read()
                self.log.logger.debug(f"Method: [open_json_file] - Data extracted: 'data_from_file'")
                return data_from_file
            
        except FileNotFoundError:
            self.log.logger.warning(f"Method: [open_json_file] - The file '{file_path}' was not found.")
            return None       