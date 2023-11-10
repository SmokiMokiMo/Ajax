import subprocess
from   utils.logger  import MyLogger


# This class encapsulates functions related to Appium capabilities for Android.
class AppCapabilitys(MyLogger):  
        
        
    # Read and log the output from an Appium server process.
    def read_appium_output(self, process):
        for line in process.stdout:
            self.logger.debug(f"Appium stdout: {line.strip()}")        
            
            
    # Get the UDID (Unique Device Identifier) of an Android device.
    def android_get_uiid(self) -> list:
        try:
            result = subprocess.run("adb devices | grep 'device' | grep -v 'List of devices attached'", stdout=subprocess.PIPE, text=True, shell=True)
            output = result.stdout
            if result.returncode == 0:
                output = (result.stdout).split()
                if len(output) >= 2:
                    devices = [device for device in output if device != 'device']
                    if devices:
                        self.logger.debug(f"Get device list: {devices}")
                        return devices[0] 
                    else:
                        self.logger.warning(f"Device list is empty: {output}")
                        return None
                else:
                    self.logger.warning(f"Device list is empty: {output}")
                    return None
            else:
                self.logger.warning(f"Operation unsuccessful. Stdout: {output}")
                return None
        except Exception as e:
            self.logger.error(f"Error: {e}")

            

    # Get the desired capabilities for an Android device.
    def android_get_desired_capabilities(self):
        try:
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
            
            # Get the UDID automatically
            udid = self.android_get_uiid()
            if udid:
                android_data['udid'] = udid
                #android_data['deviceName'] = udid[0]
                self.logger.debug(f"'udid' is '{udid}' passed.")
            else:
                self.logger.error(f"Failed to retrieve UDID. Please check your device connection. Device list is {udid}")            
            return android_data
        except Exception as e:
            self.logger.error(f"Error: {e}")
            
if __name__ in '__main__':
    app_ver = AppCapabilitys()
    app_ver.android_get_desired_capabilities()
