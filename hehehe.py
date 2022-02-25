from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import threading
import time

name=""
birth=""
school_location=""
school_type=""
school_name=""
passwd=""


#service = ChromeService(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
#prefs = {"profile.managed_default_content_settings.images": 2}
#options.BinaryLocation = "/usr/bin/chromium-browser"
# we use custom chromedriver for raspberry
driver_path = "/usr/bin/chromedriver"
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#options.add_experimental_option("prefs", prefs)
options.add_argument("--mute-audio")
driver = webdriver.Chrome(options=options, service=Service(driver_path))
driver.implicitly_wait(15)
driver.get('https://hcs.eduro.go.kr/#/loginWithUserInfo')
action=ActionChains(driver)


def run():
    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//button[@id='btnConfirm2']")
    action.move_to_element_with_offset(e, 165, 35)
    action.click().perform()
    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//button[@title='학교 검색']")
    action.move_to_element_with_offset(e, 40, 40)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//select[@id='sidolabel']")
    action.move_to_element_with_offset(e, 40, 20)
    action.click().perform()
    action = ActionChains(driver)
    ddelement= Select(driver.find_element(By.XPATH, "//select[@id='sidolabel']"))
    ddelement.select_by_visible_text(school_location)
    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//select[@id='sidolabel']")
    action.move_to_element_with_offset(e, 40, 20)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//select[@id='crseScCode']")
    action.move_to_element_with_offset(e, 40, 20)
    action.click().perform()
    action = ActionChains(driver)
    ddelement= Select(driver.find_element(By.XPATH, "//select[@id='crseScCode']"))
    ddelement.select_by_visible_text(school_type)
    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//select[@id='crseScCode']")
    action.move_to_element_with_offset(e, 40, 20)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//input[@id='orgname']")
    action.move_to_element_with_offset(e, 10, 10)
    action.click().perform()

    e.send_keys(school_name + Keys.ENTER)

    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//ul[@role='radiogroup']")
    action.move_to_element_with_offset(e, 10, 10)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//div[@class='layerBtnWrap']")
    action.move_to_element_with_offset(e, 10, 10)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//input[@id='user_name_input']")
    action.move_to_element_with_offset(e, 10, 10)
    action.click().perform()

    e.send_keys(name + Keys.TAB)

    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//input[@id='birthday_input']")
    e.send_keys(birth + Keys.ENTER)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@title='가상키패드열기']"))
    )

    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//button[@title='가상키패드열기']").send_keys(Keys.ENTER)
    #action.move_to_element_with_offset(e, 10, 10)
    #action.click().perform()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@aria-label='0']"))
    )

    for i in passwd:
        action = ActionChains(driver)
        e = driver.find_element(By.XPATH, f"//a[@aria-label='{i}']")
        action.move_to_element(e)
        action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//input[@id='btnConfirm']")
    action.move_to_element(e)
    action.click().perform()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//section[@class='memberWrap']//li[1]"))
    )

    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//section[@class='memberWrap']//li[1]")
    action.move_to_element_with_offset(e, 300,50)
    action.click().perform()
    driver.implicitly_wait(15)

    for i in range(5):
        action = ActionChains(driver)
        e = driver.find_element(By.XPATH, f"//input[@id='survey_q{i+1}a1']")
        action.move_to_element(e)
        action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element(By.XPATH, "//input[@id='btnConfirm']")
    action.move_to_element(e)
    action.click().perform()

try:
    run()
    driver.close()
except UnexpectedAlertPresentException:
    driver.close()
