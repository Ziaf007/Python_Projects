this script is a basic Automation Script made using the Selenium.Webdriver Module primarily. the Script uses Chromedriver for opening up a Google Chrome window. It then Navigates
to the Moodle portal Dashboard and then logs in the user. It opens the side-Drawer which houses all the attendance links and clicks the upcoming one to check whether the
"Submit Attendance" link has been activated or not. If true it clicks the link and marks the user present. If false, it logouts the user, and closes the driver window. the script
is enclosed in a While True loop and so will run till eternity until the user manually stops the script or closes the driver window while running.

the script requires an additional .txt file from which it shall read the credentials of the user and the path of the chromedriver. The file is not included in the repository and
needs to be manually created by the user in the format of USERNAME,PASSWORD,CHROMEDRIVER_PATH and then link the file to the script by specifying the file path in the F holder(line 5).
