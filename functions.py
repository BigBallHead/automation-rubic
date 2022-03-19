from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from env import *

"""
Распаковка расширения и авторизация(Сеть полигон).
"""
def connect_to_chrome_with_mm(driver):
    wait = WebDriverWait(driver,30)
    handles = driver.window_handles
    driver.switch_to.window(handles[0])
    sleep(1)
    driver.refresh()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@class='button btn--rounded btn-primary first-time-flow__button']")))
    driver.find_element_by_xpath("//*[@class='button btn--rounded btn-primary first-time-flow__button']").click()
    driver.find_element_by_xpath("//button[text()='Import wallet']").click()
    driver.find_element_by_xpath("//button[text()='No Thanks']").click()
    sleep(1)
    InputsMetamask = driver.find_elements_by_xpath('//input')
    InputsMetamask[0].send_keys(secret_phrase)
    InputsMetamask[1].send_keys(password)
    InputsMetamask[2].send_keys(password)
    driver.find_element_by_xpath("//*[@class='first-time-flow__checkbox first-time-flow__terms']").click() #чек-бокс
    driver.find_element_by_xpath('//button[text()="Import"]').click()
    wait.until(EC.element_to_be_clickable((By.XPATH,'//button[text()="All Done"]')))
    driver.find_element_by_xpath('//button[text()="All Done"]').click()

    #----------Закрытие всплывающего окна
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@data-testid="popover-close"]')))
    driver.find_element_by_xpath('//*[@data-testid="popover-close"]').click() #Крестик

    #---------Смена аккаунта и создание сети
    driver.find_element_by_xpath("//*[@class='account-menu__icon']").click()
    driver.find_element_by_xpath('//*[text()="Account 3"]').click()
    driver.find_element_by_xpath("//*[@class='account-menu__icon']").click()
    driver.find_element_by_xpath('//*[text()="Settings"]').click()
    driver.find_element_by_xpath('//*[text()="Networks"]').click()
    driver.find_element_by_xpath('//*[text()="Add a network"]').click()
    Inputs = driver.find_elements_by_xpath("//*[@class='form-field__input']")
    Inputs[0].send_keys('Polygon Mainnet')
    Inputs[1].send_keys('https://polygon-rpc.com/')
    Inputs[2].send_keys('137')
    Inputs[3].send_keys('MATIC')
    Inputs[4].send_keys('https://polygonscan.com/')
    driver.find_element_by_xpath('//*[text()="Save"]').click()

"""
Функция ожидания загрузки элемента
"""
def wait_elements_located(xpath, driver):
    element = WebDriverWait(driver,20).until(
        EC.element_to_be_clickable(
            (By.XPATH,xpath)
        )
    )
    return element

"""
Функция клика на элемент после его загрузки
"""
def wait_elements_clicable(xpath, driver):
    element = WebDriverWait(driver,20).until(
        EC.presence_of_element_located(
            (By.XPATH,xpath)
        )
    )
    return element

"""
Функция возврата в бургер меню
"""
def back_to_burger_and_click(driver):
    driver.execute_script("history.back();")
    wait_elements_clicable(xpath="//*[@class='burger-menu']",driver=driver).click()


# wait_elements_clicable(xpath="//a[text()='details']",driver=driver).click()
# print('Инстант трейд прошел успешно')



# w3 = Web3(HTTPProvider(""))
# tx_hash = w3.eth.getTransactionCount('your account address')
