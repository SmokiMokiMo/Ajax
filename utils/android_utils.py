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
            result = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE, text=True)
            
            if result.returncode == 0:
                output_lines = result.stdout.strip().split('\n')
                devices = []

                for line in output_lines:
                    parts = line.split()
                    if len(parts) == 2:
                        status = parts[0]
                        devices.append(status)

                if devices:
                    self.logger.info(f"Connected devices: {devices}")
                    return devices
                else:
                    self.logger.warning("No connected devices found.")
                    return None
            else:
                self.logger.warning(f"ADB command unsuccessful. Stdout: {result.stdout}")
                return None
        except Exception as e:
            self.logger.error(f"Error: {e}")
            return None
            

    # Get the desired capabilities for an Android device.
    def android_get_desired_capabilities(self):
        try:
            android_data = {
                "autoGrantPermissions": True,
                "automationName": "uiautomator2",
                "newCommandTimeout": 500,
                "noSign": True, 
                "platformName": "Android",
                "deviceName": "None",
                "platformVersion": "14",
                "resetKeyboard": True,
                "systemPort": 8301,
                "takesScreenshot": True,
                "udid": "None",
                "appPackage": "com.ajaxsystems",
                "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity"
            }
            
            # Get the UDID automatically
            udid = self.android_get_uiid()
            self.logger.info(f"Actual list of list available Devices - '{udid}'")
            if udid:
                android_data['udid'] = udid[0]
                android_data['deviceName'] = udid[0]
                self.logger.info(f"'udid' is '{udid}' passed.")
            else:
                self.logger.error(f"Failed to retrieve UDID. Please check your device connection. Device list is {udid}")            
            return android_data
        except Exception as e:
            self.logger.error(f"Error: {e}")