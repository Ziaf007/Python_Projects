this script is a basic Automation Script made using the Selenium.Webdriver Module primarily. the Script uses Chromedriver for opening up a Google Chrome window. It then Navigates
to the Moodle portal Dashboard and then logs in the user. It opens the side-Drawer which houses all the attendance links and clicks the upcoming one to check whether the
"Submit Attendance" link has been activated or not. If true it clicks the link and marks the user present. If false, it logouts the user, and closes the driver window. the script
is enclosed in a While True loop and so will run till eternity until the user manually stops the script or closes the driver window while running.
