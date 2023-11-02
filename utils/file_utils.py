from utils.logger import MyLogger
import json
class LoginPage():    
    
    def __init__(self):
        
        self.log = MyLogger()    
        
        
        
        
    def get_keys_from_json(self, json_values) -> list:
        try:
            # Parse the JSON string into a dictionary
            data = json.loads(json_values)
            keys = list(data.keys())
            self.log.logger.info(f"Method: [get_keys_from_json] - Data extracted list of keys: {keys}")
            return keys
        except (json.JSONDecodeError, AttributeError) as e:
            self.log.logger.error(f"Method: [get_keys_from_json] got error: {e}")
        
                
    def get_resource_id_from_json(self, main_keys, json_data, expected_values):
        # Ensure that json_data is a dictionary, not a string
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
    
    # Define the test method for user login    
    
    def preper_data(self, file_path_test_json, file_path_credentials_json, resourceid):
        try:          
            # Load the JSON data
            json_data = self.open_json_file(file_path_test_json)
            self.log.logger.debug(f"Method: [data preparation] - Opened successfully JSON with test_login_data.json 'json_data'")
            # Load credentials from the JSON file
            credentials:dict = json.loads(self.open_json_file(file_path_credentials_json))
            self.log.logger.debug(f"Method: [data preparation] - Opened successfully JSON with credentials.json {credentials}")

            main_keys:list = self.get_keys_from_json(json_data)  # Store main_keys as an instance variable
            self.log.logger.info(f"Method: [data preparation] - extracted data 'main_keys' is: {main_keys}")
            element_ids = self.get_resource_id_from_json(main_keys, json_data, resourceid)  # Store element_ids
            self.log.logger.info(f"Method: [data preparation] - extracted data 'element_ids' is: {element_ids}")
            return credentials, main_keys, element_ids
        except Exception as e:
            self.log.logger.error(f"Method: [data preparation] - returned error '{e}'")
        
    def open_json_file(self, file_path):     
        try:
            with open(file_path, mode='r', encoding='UTF-8') as file:
                data_from_file = file.read()
                self.log.logger.debug(f"Method: [open_json_file] - Data extracted: 'data_from_file'")
                return data_from_file
            
        except FileNotFoundError:
            self.log.logger.warning(f"Method: [open_json_file] - The file '{file_path}' was not found.")
            return None   
    
    def test(self):        
        print("test_message") 