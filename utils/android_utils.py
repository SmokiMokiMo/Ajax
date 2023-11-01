import subprocess
from   utils.logger  import MyLogger







class AppCapabilitys():
    
    def __init__(self):
        self.log = MyLogger()
        
        
    def read_appium_output(self, process):
        for line in process.stdout:
            self.log.logger.debug(f"Method: [run_appium_server] - Appium stdout: {line.strip()}")        
   
    def android_get_uiid(self):
        try:
            result = subprocess.run("adb devices | grep 'device' | grep -v 'List of devices attached'", stdout=subprocess.PIPE, text=True, shell=True)
            output = result.stdout
            if result.returncode == 0:
                output = (result.stdout).split()
                if len(output) >= 2:
                    devices = [device for device in output if device != 'device']                    
                    self.log.logger.debug(f"Method: [android_get_uiid] - get device list: {devices}")
                    return devices
                else:
                    self.log.logger.warning(f"Method: [android_get_uiid] - device list is empty: {output}")
                    return None
            else:
                self.log.logger.warning(f"Method: [android_get_uiid] - operation unsuccessful. Stdout: {output}")
                return None
        except Exception as e:
            self.log.logger.error(f"Method: [android_get_uiid] - Error: {e}")

    def android_get_desired_capabilities(self, udid=None):
        android_data = {
            "autoGrantPermissions": True,
            "automationName": "uiautomator2",
            "newCommandTimeout": 500,
            "noSign": True,
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "platformVersion": "14",
            "resetKeyboard": True,
            "systemPort": 8301,
            "takesScreenshot": True,
            "udid": "emulator-5554",
            "appPackage": "com.ajaxsystems",
            "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity"
        }        
        # udid = self.android_get_desired_capabilities()
        # self.logger.info(udid)
        if udid is not None:
            android_data['udid'] = udid
            self.log.logger.info(f"Method: [android_get_desired_capabilities] - 'udid' is '{udid}' passed in method 'android_get_desired_capabilities'")
        return android_data
    


# app_cap = AppCapabilitys()
# app_cap.is_appium_server_running()
#print(app_cap.android_get_uiid()) # This will print the list of UIIDs