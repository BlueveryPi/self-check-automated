#!D:\anaconda3\envs\py39\
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import threading
import time

options = webdriver.ChromeOptions()
#prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#options.add_experimental_option("prefs", prefs)
options.add_argument("--mute-audio")
driver = webdriver.Chrome(r'codes\funhack\chromedriver.exe', options=options)
driver.implicitly_wait(15)
driver.get('https://hcs.eduro.go.kr/#/loginWithUserInfo')
action=ActionChains(driver)

region=""
school=""
guegep=""
name=""
birth=""

def run():
    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//button[@id='btnConfirm2']")
    action.move_to_element_with_offset(e, 165, 35)
    action.click().perform()
    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//button[@title='학교 검색']")
    action.move_to_element_with_offset(e, 40, 40)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//select[@id='sidolabel']")
    action.move_to_element_with_offset(e, 40, 20)
    action.click().perform()
    action = ActionChains(driver)
    ddelement= Select(driver.find_element_by_xpath("//select[@id='sidolabel']"))
    ddelement.select_by_visible_text(region)
    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//select[@id='sidolabel']")
    action.move_to_element_with_offset(e, 40, 20)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//select[@id='crseScCode']")
    action.move_to_element_with_offset(e, 40, 20)
    action.click().perform()
    action = ActionChains(driver)
    ddelement= Select(driver.find_element_by_xpath("//select[@id='crseScCode']"))
    ddelement.select_by_visible_text(guegep)
    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//select[@id='crseScCode']")
    action.move_to_element_with_offset(e, 40, 20)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//input[@id='orgname']")
    action.move_to_element_with_offset(e, 10, 10)
    action.click().perform()

    e.send_keys(school + Keys.ENTER)

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//ul[@role='radiogroup']")
    action.move_to_element_with_offset(e, 10, 10)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//div[@class='layerBtnWrap']")
    action.move_to_element_with_offset(e, 10, 10)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//input[@id='user_name_input']")
    action.move_to_element_with_offset(e, 10, 10)
    action.click().perform()

    e.send_keys(name + Keys.TAB)

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//input[@id='birthday_input']")
    e.send_keys(birth + Keys.ENTER)

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//input[@id='password']")
    action.move_to_element_with_offset(e, 10, 10)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//a[@aria-label='0']")
    action.move_to_element(e)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//a[@aria-label='4']")
    action.move_to_element(e)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//a[@aria-label='2']")
    action.move_to_element(e)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//a[@aria-label='1']")
    action.move_to_element(e)
    action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//input[@id='btnConfirm']")
    action.move_to_element(e)
    action.click().perform()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//section[@class='memberWrap']//li[1]"))
    )

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//section[@class='memberWrap']//li[1]")
    action.move_to_element_with_offset(e, 300,50)
    action.click().perform()
    driver.implicitly_wait(15)

    for i in range(3):
        action = ActionChains(driver)
        e = driver.find_element_by_xpath(f"//input[@id='survey_q{i+1}a1']")
        action.move_to_element(e)
        action.click().perform()

    action = ActionChains(driver)
    e = driver.find_element_by_xpath("//input[@id='btnConfirm']")
    action.move_to_element(e)
    action.click().perform()

run()