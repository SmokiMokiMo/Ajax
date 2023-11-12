from utils.logger import MyLogger
import json
import configparser
import os


# This class encapsulates methods for handling JSON data and preparing data for user login tests.
class FilesExtractor(MyLogger):   
    def __init__(self):
        super().__init__()     
        self.config = configparser.ConfigParser()

    # Extract data from a 'selector' and return them as a dict. 
    def extract_data_from_ini_files(self, file_name: str="login_selectors.ini", section_name: str = "resource-id") -> dict:
        try:
            project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../selectors/',file_name))           
            data_dict = {}
            self.config.read(project_directory)  
            section = self.config[section_name]
            for key, value in section.items():
                data_dict[key] = value
                self.logger.debug(f"Name: {key}, Value: {value}")
            self.logger.debug(f"Return 'Data_dict': '{data_dict}' from ['{project_directory}']")
            return data_dict
                       
        except Exception as e:
            self.logger.error(f"Error occurred {e}")
        
             
    # Extract keys from a JSON string and return them as a list.  
    def get_keys_from_json(self, json_values) -> list:
        try:            
            data = json.loads(json_values)
            keys = list(data.keys())
            self.log.logger.info(f"Data extracted list of keys: {keys}")
            return keys
        except (json.JSONDecodeError, AttributeError) as e:
            self.logger.error(f"Got error: {e}")
            
        
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

            self.logger.info(f"Data extracted dict: {resource_ids}")
            return resource_ids
        except Exception as e:
            self.logger.error(f"Got error: {e}")
            
    
    # Prepare test data by opening and extracting data from JSON files. 
    def preper_data(self, file_path_test_json, file_path_credentials_json, resourceid):
        try:          
            json_data = self.open_json_file(file_path_test_json)
            self.logger.debug(f"Opened successfully JSON with test_login_data.json 'json_data'")          
            credentials:dict = json.loads(self.open_json_file(file_path_credentials_json))
            self.logger.debug(f"Opened successfully JSON with credentials.json {credentials}")
            main_keys:list = self.get_keys_from_json(json_data)  
            self.logger.info(f"Extracted data 'main_keys' is: {main_keys}")
            element_ids = self.get_resource_id_from_json(main_keys, json_data, resourceid)  
            self.logger.info(f"Extracted data 'element_ids' is: {element_ids}")
            return credentials, main_keys, element_ids
        
        except Exception as e:
            self.logger.error(f"Returned error '{e}'")
            
            
    # Open and read the contents of a JSON file.
    def open_json_file(self, file_path):     
        try:
            with open(file_path, mode='r', encoding='UTF-8') as file:
                data_from_file = file.read()
                self.logger.debug(f"Data extracted: 'data_from_file'")
                return data_from_file
            
        except FileNotFoundError:
            self.logger.warning(f"The file '{file_path}' was not found.")
            return None 