from appium import webdriver
from utils.android_utils import AppCapabilitys
from utils.logger import MyLogger
import pytest
import subprocess
import time
from selenium.common.exceptions import WebDriverException
from appium.options.android import UiAutomator2Options
import threading

log = MyLogger()
# Define the fixture to start the Appium server
@pytest.fixture(scope='session', autouse=True)
def run_appium_server():    
    app_cap = AppCapabilitys()
    try:
        appium_process = subprocess.Popen(
            ['appium'],
            stdout=subprocess.PIPE,  
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            shell=True,
            text=True)        
        #Read and print the stdout from the appium process
        output_reader = threading.Thread(target=app_cap.read_appium_output, args=(appium_process,))
        output_reader.start()    
        
        time.sleep(5)
        log.logger.debug("Method: [run_appium_server] - timer is ower.")
        
    except Exception as e:
        log.logger.error(f"Method: [run_appium_server] - Failed to start Appium server: {e}")
      

# Fixture for initializing the Appium driver
@pytest.fixture(scope='session')
def appium_driver(run_appium_server):    
    app_cap = AppCapabilitys()
    try:        
        options = UiAutomator2Options()
        options.load_capabilities(app_cap.android_get_desired_capabilities())        
        appium_driver = webdriver.Remote('http://127.0.0.1:4723', options=options)       
        
        log.logger.info(f"Method: [appium_driver] - Appium driver initialized successfully with desired_caps: {appium_driver}\n")
        yield appium_driver        
    except WebDriverException as e:
        log.logger.error(f"Method: [appium_driver] - WebDriverException occurred: {e}")        
    except Exception as e:
        log.logger.error(f"Method: [appium_driver] - An error occurred while setting up the Appium driver: {e}")