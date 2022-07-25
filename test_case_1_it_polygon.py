from selenium import webdriver
from time import sleep
from env import *

from main import connect_to_chrome_with_mm_polygon
from main import wait_elements_clicable
from main import wait_elements_located

METAMASK_PATH = metamask_path
op = webdriver.ChromeOptions()
op.add_extension(METAMASK_PATH)
op.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
op.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=chrome_path,options=op)
driver.maximize_window()

try:
    connect_to_chrome_with_mm_polygon(driver)

    driver.execute_script("window.open('https://app.rubic.exchange/?fromChain=POLYGON&toChain=POLYGON&from=MATIC&to=ALGB&amount=0.01')")
    driver.switch_to.window(driver.window_handles[2])

    wait_elements_clicable(xpath="//span[text()='Connect Wallet']", driver=driver).click()
    driver.find_element_by_xpath("//button[contains(text(), 'MetaMask')]").click()
    sleep(3)
    driver.switch_to.window(driver.window_handles[3])
    wait_elements_clicable(xpath="//*[text()='Next']",driver=driver).click()
    wait_elements_clicable(xpath="//*[text()='Connect']",driver=driver).click()
    driver.switch_to.window(driver.window_handles[2])
    sleep(1)

    swap_button = wait_elements_clicable(xpath="//span[contains(text(),'Swap')]",driver=driver).click()

    sleep(3)
    driver.switch_to.window(driver.window_handles[3])
    sleep(1)
    wait_elements_clicable(xpath="//button[text()='Confirm']",driver=driver).click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[2])
    wait_elements_clicable(xpath='//*[text()="details"]',driver=driver).click()
    driver.switch_to.window(driver.window_handles[3])

finally:
    txhash = wait_elements_located("//*[@id='spanTxHash']",driver=driver)
    if txhash:
        print('Инстант трейд прошел успешно',txhash.text)
        driver.quit()



#driver.get('https://polygonscan.com/tx/' + txhash)
#wait_elements_located(driver=driver,xpath="//*[text()='Success']")




