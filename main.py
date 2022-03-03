# https://demoqa.com/

from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


from termcolor import cprint
import essentials
import platform
import sys
import os
import time

global_log = essentials.Logger()


def message(typeMessage, text):
    if typeMessage == "info":
        global_log.info(text)
        cprint(text, "green")
    elif typeMessage == "warning":
        global_log.warning(text)
        cprint(text, "yellow")
    elif typeMessage == "error":
        global_log.error(text)
        cprint(text, "red")


DATA_info = {
    'fname': 'TUAN',
    'lname': 'LE',
    'email': "letuan317@gmail.com",
    'address': '123 street, city, zip code',
    'age': '99',
    'salary': '123',
    'department': 'development',
    'file_path': '/Users/letuan/Downloads/sampleFile.jpg'
}


def WaitingMode(seconds):
    for i in range(5, 0, -1):
        print(f"Wait ... {str(i)}")
        time.sleep(1)


class AutoFilling:
    def __init__(self):
        self.sleeptimer = 3
        self.timeout = 3
        self.waitingtime = 5

    def run(self):
        self.OpenBrowser()
        # self.TaskElements()
        # self.TaskForms()
        self.TaskAlertsFrameWindows()
        self.TaskWidgets()
        self.TaskInteractions()
        self.TaskBookStoreApplication()
        input('Continue?')
        self.driver.quit()

    # Create a session
    def OpenBrowser(self):
        message("info", "Open chromedriver")
        options = Options()
        # options.add_argument('headless')
        options.add_argument("disable-gpu")
        options.add_argument(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")

        if platform.system() == "Windows":
            message("warning", "Selenium run on Windows")
            chrome_path = './drivers/chromedriver96.exe'
        elif platform.system() == "Darwin":
            message("warning", "Selenium run on Mac OS")
            chrome_path = './drivers/chromedriver98'
        else:
            message("error", "Missing chromedriver")
            sys.exit()
        try:
            ser = Service(chrome_path)
            self.driver = webdriver.Chrome(options=options, service=ser)
            self.driver.set_window_position(0, 0)
            self.driver.set_window_size(800, 500)
        except Exception as e:
            message("error", e)
            sys.exit()

    def IsPageLoaded(self, name_page, link):
        message("info", f"[##] Working on {name_page}...")
        self.driver.get(link)
        time.sleep(self.sleeptimer)
        try:
            element_present = EC.presence_of_element_located(
                (By.ID, 'app'))
            WebDriverWait(self.driver, self.timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        finally:
            message("info", "[!] {} Page loaded".format(name_page))
            return True
        return False

    def IsSuccessfull(self, type_check, element_check, name_page):
        # POM compare results
        try:
            element_present = EC.presence_of_element_located(
                (type_check, element_check))
            WebDriverWait(self.driver, self.timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        finally:
            message("info", f"[*] {name_page} Successcully")
            return True

    def TaskElements(self):
        message("info", "[#] Working on section Elements...")

        def TextBox():
            isLoad = self.IsPageLoaded(
                "TextBox", 'https://demoqa.com/text-box')
            if isLoad:
                # Full Name
                self.driver.find_element(
                    By.XPATH, '//*[@id="userName"]').send_keys(DATA_info['fname']+' '+DATA_info['lname'])
                message("warning", "[+] TextBox full name filled")
                # Email
                self.driver.find_element(
                    By.XPATH, '//*[@id="userEmail"]').send_keys(DATA_info['email'])
                message("warning", "[+] TextBox email filled")
                # Current Address
                self.driver.find_element(
                    By.XPATH, '//*[@id="currentAddress"]').send_keys(DATA_info['address'])
                message("warning", "[+] TextBox current address filled ")
                # Permannent Address
                self.driver.find_element(
                    By.XPATH, '//*[@id="permanentAddress"]').send_keys(DATA_info['address'])
                message("warning", "[+] TextBox permannent address filled")
                # Submit
                submit_button = self.driver.find_element(
                    By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div/button')
                self.driver.execute_script(
                    "arguments[0].click();", submit_button)
                message("warning", "[+] TextBox summit clicked")

                self.IsSuccessfull(By.ID, 'name', 'TextBox')

        def CheckBox():
            isLoad = self.IsPageLoaded(
                'CheckBox', 'https://demoqa.com/checkbox')
            if isLoad:
                # Check Box
                self.driver.find_element(
                    By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/ol/li/span/label/span[1]').click()
                message("warning", "[+] Check Box ticked")

                self.IsSuccessfull(By.ID, 'result', 'CheckBox')

        def RadioButton():
            isLoad = self.IsPageLoaded(
                "RadioButton", 'https://demoqa.com/radio-button')
            if isLoad:
                option_yes = self.driver.find_element(
                    By.XPATH, '//*[@id="yesRadio"]')
                self.driver.execute_script("arguments[0].click();", option_yes)
                message("warning", "[+] RadioButton: Select yes option")
                WaitingMode(self.waitingtime)
                if self.IsSuccessfull(By.XPATH,
                                      '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/p/span', 'RadioButton yes'):
                    option_impressive = self.driver.find_element(
                        By.XPATH, '//*[@id="impressiveRadio"]')
                    self.driver.execute_script(
                        "arguments[0].click();", option_impressive)
                    message(
                        "warning", "[+] RadioButton: Select Impressive option")
                    self.IsSuccessfull(By.XPATH,
                                       '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/p/span', 'RadioButton impressive')

        def WebTables():
            isLoad = self.IsPageLoaded(
                "RadioButton", 'https://demoqa.com/webtables')
            if isLoad:
                add_button = self.driver.find_element(
                    By.XPATH, '//*[@id="addNewRecordButton"]')
                self.driver.execute_script("arguments[0].click();", add_button)
                message("warning", "[+] WebTables: Add button clicked")
                if self.IsSuccessfull(By.CLASS_NAME, 'modal-content', 'WebTables: Add button found'):
                    temp_element = self.driver.find_element(
                        By.CLASS_NAME, 'modal-content')
                    temp_element.find_element(
                        By.XPATH, '//*[@id="firstName"]').send_keys(DATA_info['fname'])
                    temp_element.find_element(
                        By.XPATH, '//*[@id="lastName"]').send_keys(DATA_info['lname'])
                    temp_element.find_element(
                        By.XPATH, '//*[@id="userEmail"]').send_keys(DATA_info['email'])
                    temp_element.find_element(
                        By.XPATH, '//*[@id="age"]').send_keys(DATA_info['age'])
                    temp_element.find_element(
                        By.XPATH, '//*[@id="salary"]').send_keys(DATA_info['salary'])
                    temp_element.find_element(
                        By.XPATH, '//*[@id="department"]').send_keys(DATA_info['department'])

                    submit_button = temp_element.find_element(
                        By.XPATH, '//*[@id="submit"]')
                    self.driver.execute_script(
                        "arguments[0].click();", submit_button)

                    WaitingMode(self.waitingtime)

                    # Edit
                    message("warning", "Edit mode")
                    edit_button = self.driver.find_element(
                        By.XPATH, '//*[@id="edit-record-1"]')
                    self.driver.execute_script(
                        "arguments[0].click();", edit_button)
                    if self.IsSuccessfull(By.CLASS_NAME, 'modal-content', 'WebTables: Form found'):
                        temp_element = self.driver.find_element(
                            By.CLASS_NAME, 'modal-content')
                        temp = temp_element.find_element(
                            By.XPATH, '//*[@id="firstName"]')
                        temp.clear()
                        temp.send_keys(DATA_info['fname'])
                        temp = temp_element.find_element(
                            By.XPATH, '//*[@id="lastName"]')
                        temp.clear()
                        temp.send_keys(DATA_info['lname'])
                        temp = temp_element.find_element(
                            By.XPATH, '//*[@id="userEmail"]')
                        temp.clear()
                        temp.send_keys(DATA_info['email'])
                        temp = temp_element.find_element(
                            By.XPATH, '//*[@id="age"]')
                        temp.clear()
                        temp.send_keys(DATA_info['age'])
                        temp = temp_element.find_element(
                            By.XPATH, '//*[@id="salary"]')
                        temp.clear()
                        temp.send_keys(DATA_info['salary'])
                        temp = temp_element.find_element(
                            By.XPATH, '//*[@id="department"]')
                        temp.clear()
                        temp.send_keys(DATA_info['department'])

                        submit_button = temp_element.find_element(
                            By.XPATH, '//*[@id="submit"]')
                        self.driver.execute_script(
                            "arguments[0].click();", submit_button)

                    WaitingMode(self.waitingtime)

                    # Delete
                    message('warning', "Delete mode")
                    delete_button = self.driver.find_element(
                        By.XPATH, '//*[@id="delete-record-1"]')
                    self.driver.execute_script(
                        "arguments[0].click();", delete_button)

                    WaitingMode(self.waitingtime)

                    # Search Query
                    message('warning', "Search Mode")
                    self.driver.find_element(
                        By.XPATH, '//*[@id="searchBox"]').send_keys("Alden")

        def Buttons():
            isLoad = self.IsPageLoaded('Buttons', 'https://demoqa.com/buttons')
            if isLoad:
                button_double_click = self.driver.find_element(
                    By.XPATH, '//*[@id="doubleClickBtn"]')
                action = ActionChains(self.driver)
                action.double_click(button_double_click).perform()
                cprint('Double Click Successful') if self.IsSuccessfull(
                    By.ID, 'doubleClickMessage', 'Buttons') else cprint('Double Click Fail')

                button_right_click = self.driver.find_element(
                    By.XPATH, '//*[@id="rightClickBtn"]')
                action = ActionChains(self.driver)
                action.context_click(button_right_click).perform()
                cprint('Right Click Successful') if self.IsSuccessfull(
                    By.ID, 'rightClickMessage', 'Buttons') else cprint('Right Click Fail')

                button_click = self.driver.find_element(
                    By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button')
                action = ActionChains(self.driver)
                action.click(button_click).perform()
                cprint('Click Successful') if self.IsSuccessfull(
                    By.ID, 'dynamicClickMessage', 'Buttons') else cprint('Click Fail')

        def Links():
            isLoad = self.IsPageLoaded('Buttons', 'https://demoqa.com/links')
            if isLoad:
                message("info", '[+] Open Home')
                self.driver.find_element(
                    By.XPATH, '//*[@id="simpleLink"]').click()
                # get current window handle
                p = self.driver.current_window_handle
                # get first child window
                chwd = self.driver.window_handles
                for w in chwd:
                    # switch focus to child window
                    if(w != p):
                        self.driver.switch_to.window(w)
                        break
                WaitingMode(self.waitingtime)
                self.driver.close()
                self.driver.switch_to.window(p)

                message("info", '[+] Open HomeG9RK')
                self.driver.find_element(
                    By.XPATH, '//*[@id="dynamicLink"]').click()
                # get first child window
                chwd = self.driver.window_handles
                for w in chwd:
                    # switch focus to child window
                    if(w != p):
                        self.driver.switch_to.window(w)
                        break
                WaitingMode(self.waitingtime)
                self.driver.close()
                self.driver.switch_to.window(p)

                for i in ['created', 'no-content', 'moved', 'bad-request', 'unauthorized', 'forbidden', 'invalid-url']:
                    try:
                        self.driver.find_elements(
                            By.XPATH, '//*[@id="'+i+'"]').click()
                    except Exception as e:
                        button_click = self.driver.find_element(
                            By.XPATH, '//*[@id="'+i+'"]')
                        action = ActionChains(self.driver)
                        action.click(button_click).perform()

                    message("info", "Clicked "+i)
                    # WaitingMode(self.waitingtime)

        def BrokenLinksImages():
            if self.IsPageLoaded('Broken Links - Images', 'https://demoqa.com/broken'):
                temp_link = self.driver.find_element(
                    By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/a[1]')
                self.driver.execute_script(
                    "arguments[0].click();", temp_link)
                message('info', "[+] Clicked on first link")
                WaitingMode(self.waitingtime)
                if self.IsPageLoaded('Broken Links - Images', 'https://demoqa.com/broken'):
                    temp_link = self.driver.find_element(
                        By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/a[2]')
                    self.driver.execute_script(
                        "arguments[0].click();", temp_link)
                    message('info', "[+] Clicked on second link")
                    WaitingMode(self.waitingtime)

        def UploadAndDownload():
            if self.IsPageLoaded('Uplolad and Download', 'https://demoqa.com/upload-download'):
                self.driver.find_element(
                    By.XPATH, '//*[@id="downloadButton"]').click()
                WaitingMode(self.waitingtime)
                temp_button = self.driver.find_element(
                    By.XPATH, '//input[@id="uploadFile"]')
                temp_button.send_keys(DATA_info['file_path'])

        def DynamicProperties():
            if self.IsPageLoaded('Dynamoic Properties', 'https://demoqa.com/dynamic-properties'):
                while True:
                    classname = self.driver.find_element(
                        By.XPATH, '//*[@id="colorChange"]').get_attribute("class")
                    if 'text-danger' in classname:
                        message(
                            "warning", "[+] Dynamic Properties: color changed")
                        break
                    time.sleep(1)
                WaitingMode(self.waitingtime)

        TextBox()
        WaitingMode(self.waitingtime)
        CheckBox()
        WaitingMode(self.waitingtime)
        RadioButton()
        WaitingMode(self.waitingtime)
        WebTables()
        WaitingMode(self.waitingtime)
        Buttons()
        WaitingMode(self.waitingtime)
        Links()
        WaitingMode(self.waitingtime)
        BrokenLinksImages()
        WaitingMode(self.waitingtime)
        UploadAndDownload()
        WaitingMode(self.waitingtime)
        DynamicProperties()
        WaitingMode(self.waitingtime)

    def TaskForms(self):
        def PracticForm():
            if self.IsPageLoaded('Practice Form', 'https://demoqa.com/automation-practice-form'):
                # Full Name
                self.driver.find_element(
                    By.XPATH, '//*[@id="firstName"]').send_keys(DATA_info['fname'])
                self.driver.find_element(
                    By.XPATH, '//*[@id="lastName"]').send_keys(DATA_info['lname'])
                message("warning", "[+] PracticeForm full name filled")
                # Email
                self.driver.find_element(
                    By.XPATH, '//*[@id="userEmail"]').send_keys(DATA_info['email'])
                message("warning", "[+] PracticeForm email filled")
                # Gender
                element_gender = self.driver.find_element(
                    By.XPATH, '//*[@id="gender-radio-1"]')
                self.driver.execute_script(
                    "arguments[0].click();", element_gender)
                message("warning", "[+] PracticeForm gender filled")
                # Mobile
                self.driver.find_element(
                    By.XPATH, '//*[@id="userNumber"]').send_keys("0123456789")
                message("warning", "[+] PracticeForm mobile filled")
                # Date of birth
                self.driver.find_element(
                    By.XPATH, '//*[@id="dateOfBirthInput"]').send_keys(" ")
                message("warning", "[+] PracticeForm dateofbirth filled")
                # Subjects
                self.driver.find_element(
                    By.XPATH, '//*[@id="subjectsInput"]').send_keys('math')
                self.driver.find_element(
                    By.XPATH, '//*[@id="subjectsInput"]').send_keys(Keys.ENTER)
                message("warning", "[+] PracticeForm Subjects filled")
                # Hobbies
                temp01 = self.driver.find_element(
                    By.XPATH, '//*[@id="hobbies-checkbox-1"]')
                self.driver.execute_script(
                    "arguments[0].click();", temp01)
                temp02 = self.driver.find_element(
                    By.XPATH, '//*[@id="hobbies-checkbox-2"]')
                self.driver.execute_script(
                    "arguments[0].click();", temp02)
                temp03 = self.driver.find_element(
                    By.XPATH, '//*[@id="hobbies-checkbox-3"]')
                self.driver.execute_script(
                    "arguments[0].click();", temp03)
                message("warning", "[+] PracticeForm Hobbies filled ")
                # Picture
                self.driver.find_element(
                    By.XPATH, '//*[@id="uploadPicture"]').send_keys(DATA_info['file_path'])
                message("warning", "[+] PracticeForm Picture filled ")
                # Current Address
                self.driver.find_element(
                    By.XPATH, '//*[@id="currentAddress"]').send_keys(DATA_info['address'])
                message("warning", "[+] PracticeForm current address filled ")
                # TODO Select options from divs
                # State
                #select = Select(self.driver.find_element(By.ID, 'state'))
                #select.select_by_visible_text('Uttar Pradesh')
                temp = self.driver.find_element(
                    By.XPATH, '///*[@id="react-select-3-input"]')
                temp.send_keys('NCR')
                temp.send_keys(Keys.ENTER)
                #self.driver.execute_script( "arguments[0].click();", temp)
                message("warning", "[+] PracticeForm state filled ")
                # City
                #select = Select(self.driver.find_element(By.ID, 'city'))
                # select.select_by_visible_text('Agra')
                message("warning", "[+] PracticeForm city filled ")

        PracticForm()

    def TaskAlertsFrameWindows(self):
        def BrowserWindows():
            if self.IsPageLoaded("BrowserWindows", 'https://demoqa.com/browser-windows'):
                p = self.driver.current_window_handle
                self.driver.find_element(
                    By.XPATH, '//*[@id="tabButton"]').click()
                chwd = self.driver.window_handles
                for w in chwd:
                    if(w != p):
                        self.driver.switch_to.window(w)
                        break
                WaitingMode(self.waitingtime)
                self.driver.close()
                self.driver.switch_to.window(p)
                message("warning", "[+] BrowserWindows button01 clicked")

                temp = self.driver.find_element(
                    By.XPATH, '//*[@id="windowButton"]')
                self.driver.execute_script(
                    "arguments[0].click();", temp)
                chwd = self.driver.window_handles
                for w in chwd:
                    if(w != p):
                        self.driver.switch_to.window(w)
                        break
                WaitingMode(self.waitingtime)
                self.driver.close()
                self.driver.switch_to.window(p)
                message("warning", "[+] BrowserWindows button01 clicked")

                temp = self.driver.find_element(
                    By.XPATH, '//*[@id="messageWindowButton"]')
                self.driver.execute_script(
                    "arguments[0].click();", temp)
                chwd = self.driver.window_handles
                for w in chwd:
                    if(w != p):
                        self.driver.switch_to.window(w)
                        break
                WaitingMode(self.waitingtime)
                self.driver.close()
                self.driver.switch_to.window(p)
                message("warning", "[+] BrowserWindows button01 clicked")

        def Alerts():
            if self.IsPageLoaded("Alerts", 'https://demoqa.com/alerts'):
                self.driver.find_element(
                    By.XPATH, '//*[@id="alertButton"]').click()
                WaitingMode(self.waitingtime)
                try:
                    WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                                        'You clicked a button')

                    alert = self.driver.switch_to.alert
                    alert.accept()
                    print("alert accepted")
                except TimeoutException:
                    print("no alert")

        def Frames(): pass
        def NestedFrames(): pass
        def ModalDialogs(): pass

        # BrowserWindows()
        Alerts()
        Frames()
        NestedFrames()
        ModalDialogs()

    def TaskWidgets(self):
        def Accordian(): pass
        def AutoComplete(): pass
        def DatePicker(): pass
        def Slider(): pass
        def ProgressBar(): pass
        def Tabs(): pass
        def ToolTips(): pass
        def Menu(): pass
        def SelectMenu(): pass

    def TaskInteractions(self):
        def Sortable(): pass
        def Selectable(): pass
        def Resizable(): pass
        def Droppable(): pass
        def Draabble(): pass

    def TaskBookStoreApplication(self):
        def Login(): pass
        def BookStore(): pass
        def Profile(): pass
        def BookStoreAPI(): pass


if __name__ == '__main__':
    at = AutoFilling()
    at.run()
