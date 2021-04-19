from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import *

F = open('C:\\Users\\moham\\AppData\\Roaming\\JetBrains\\PyCharmCE2020.2\\scratches\\credentials.txt', mode='r')
text = F.readline()
Username, Passphrase, DriverPath = text.split(",")

while True:
    driver = webdriver.Chrome(DriverPath)
    driver.get('https://cse.rgpvonline.org/login/index.php')

    log_button = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div/div/section/div/div[3]/div/div/div/div/div[2]/form/div[1]/input')
    pass_button = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div/div/section/div/div[3]/div/div/div/div/div[2]/form/div[2]/input')
    submit_button = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div/div/section/div/div[3]/div/div/div/div/div[2]/form/button')

    def LogIn():
        log_button.send_keys(Username)
        sleep(1)

        pass_button.send_keys(Passphrase)
        sleep(1)

        submit_button.click()
        sleep(1)


    LogIn()
    # driver.maximize_window()
    driver.implicitly_wait(5)


    # drawer = driver.find_element_by_id("sidepreopen-control")     ###Carefully use as per need
    # drawer.click()

    def Check(element_choosing_criteria):  ##Modify the function according to the criteria
        try:
            driver.find_element_by_partial_link_text(element_choosing_criteria)
        except NoSuchElementException:
            return False
        return True


    def Attending():
        if Check("Attendance"):
            current_attendance_link = driver.find_element_by_partial_link_text(
                'Attendance')
            driver.execute_script("arguments[0].scrollIntoView(true);", current_attendance_link)
            current_attendance_link.click()
            driver.implicitly_wait(10)

            try:
                goto = driver.find_element_by_link_text("Go to activity")
                goto.click()
            except:
                pass

            if Check("Submit attendance"):
                try:
                    Submit = driver.find_element_by_link_text("Submit attendance")
                    Submit.click()
                except ElementClickInterceptedException:
                    Submit = driver.find_element_by_link_text("Submit attendance")
                    driver.execute_script("arguments[0].scrollIntoView(true);", Submit)
                    Submit.click()
                driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/section/div[1]/div/div/form/fieldset/div/div/div[2]/fieldset/div//span[contains(text(),'Present')]").click() ##Present radio button
                Save = driver.find_element_by_css_selector("input[type='submit'][name='submitbutton']")
                Save.click()
                sleep(3)
            else:  ## Code for returning to dashboard
                driver.implicitly_wait(3)

    def LogOut():
        driver.find_element_by_xpath("/html/body/nav/ul[2]/li[2]/div/div/div/div/a").click()  ##Top-Right dropdown menu
        driver.implicitly_wait(5)
        driver.find_element_by_link_text("Log out").click()  ##Logout button

    Attending()
    sleep(3)
    try:
        LogOut()
        driver.close()
    except:
        driver.close()

###fgroup_id_statusarray > div.col-md-9.form-inline.felement > fieldset > div > label:nth-child(1) > span
##//*[@id="fgroup_id_statusarray"]/div[2]/fieldset/div/label[1]/span
##/html/body/div[2]/div[2]/div/div/section/div[1]/div/div/form/div[2]/div[2]/fieldset/div/div[1]/span[2]/input {"Save Changes" input typ= "submit"}