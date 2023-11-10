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

stop_threads = False


# Stop appium server after tests executing
def stop_appium_server(appium_process):
    global stop_threads
    stop_threads = True
    appium_process.terminate()

# Define the fixture to start the Appium server
@pytest.fixture(scope='session', autouse=True)
def run_appium_server():    
    app_cap = AppCapabilitys()
    appium_process = None
    try:
        appium_process = subprocess.Popen(
            ['appium'],
            stdout=subprocess.PIPE,  
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            shell=True,
            text=True)        
        
        #output_reader = threading.Thread(target=app_cap.read_appium_output, args=(appium_process,))
        #output_reader.start()  
        time.sleep(5)       
        
        log.logger.debug("Timer is ower.")
        
    except Exception as e:
        log.logger.error(f"Failed to start Appium server: {e}")
    finally:
        stop_appium_server(appium_process)
    return appium_process

# Fixture for initializing the Appium driver
@pytest.fixture(scope='session')
def appium_driver(run_appium_server):    
    app_cap = AppCapabilitys()
    try:        
        options = UiAutomator2Options()
        log.logger.info("Try capabilities")
        options.load_capabilities(app_cap.android_get_desired_capabilities())        
        appium_driver = webdriver.Remote('http://127.0.0.1:4723', options=options)       
        
        log.logger.info(f"Appium driver initialized successfully with desired_caps: {appium_driver}")
        yield appium_driver        
    except WebDriverException as e:
        log.logger.error(f"WebDriverException occurred: {e}")        
    except Exception as e:
        log.logger.error(f"An error occurred while setting up the Appium driver: {e}")
        #tearDown(driver)    