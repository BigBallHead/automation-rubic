from selenium import webdriver
from time import sleep
from env import *

from main import wait_elements_clicable
from main import wait_elements_located

COINBASE_PATH = "/Users/ivankondratev/Desktop/automation-rubic/coinbase.crx"
op = webdriver.ChromeOptions()
op.add_extension(COINBASE_PATH)
op.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
op.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='/Users/ivankondratev/Desktop/automation-rubic/chromedriver',options=op)
driver.maximize_window()
driver.switch_to.window(driver.window_handles[0])
wait_elements_clicable(driver=driver,xpath="//*[text()='I already have a wallet']").click()
wait_elements_clicable(driver=driver,xpath="//*[text()='Use your 12 word recovery phrase to securely access your wallet.']").click()
wait_elements_clicable(driver=driver,xpath="//input[@placeholder='12 word seed phrase']").send_keys("brave solid blush mixed bounce skull decorate call hair alpha awkward element")
wait_elements_clicable(xpath="//span[text()='Import wallet']",driver=driver).click()
wait_elements_located(xpath="//input[@placeholder='Enter password']",driver=driver).send_keys("d1c7b182")
wait_elements_located(xpath="//input[@placeholder='Enter password again']",driver=driver).send_keys("d1c7b182")
wait_elements_clicable(xpath="//*[@type='checkbox']",driver=driver).click()
wait_elements_clicable(xpath="//*[text()='Submit']",driver=driver).click()

driver.execute_script("window.open('https://app.rubic.exchange')")

driver.switch_to.window(driver.window_handles[2])
wait_elements_clicable(xpath="//button[@id='details-button']",driver=driver).click()
wait_elements_clicable(xpath="//button[@id='proceed-link']",driver=driver).click()
wait_elements_clicable(xpath="//span[text()='Connect Wallet']", driver=driver).click()
