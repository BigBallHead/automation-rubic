import click
from selenium import webdriver
from time import sleep

from functions import connect_to_chrome_with_mm
from functions import wait_elements_clicable

METAMASK_PATH = "/Users/ivankondratev/Desktop/automation.rubic/metamaskextgeneral.crx"
op = webdriver.ChromeOptions()
op.add_extension(METAMASK_PATH)
op.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
op.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="/Users/ivankondratev/Desktop/automation.rubic/chromedriver-3",options=op)
driver.maximize_window()

connect_to_chrome_with_mm(driver)
driver.switch_to.window(driver.window_handles[2])
sleep(3)

try:
    swap_button = wait_elements_clicable(xpath="//span[contains(text(),'Swap')]",driver=driver).click()
except TimeoutError:
    driver.refresh()


sleep(2)
driver.switch_to.window(driver.window_handles[3])
sleep(2)
result = wait_elements_clicable(xpath="//button[text()='Confirm']",driver=driver).click()
