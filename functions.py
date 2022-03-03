from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# driver = webdriver.Chrome(executable_path='/Users/ivankondratev/Desktop/automation.rubic/metamaskextgeneral.crx')
#
"""
Распаковка и авторизация в метамаске.
"""
def connect_to_chrome_with_mm(driver):
    wait = WebDriverWait(driver,30)
    handles = driver.window_handles
    driver.switch_to.window(handles[0])
    sleep(1)
    driver.refresh() #Костыльная строчка, иногда расширение метамаска открывает пустую страницу, после рефреша становится ок, закономерность установить не удалось.
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@class='button btn--rounded btn-primary first-time-flow__button']")))
    driver.find_element_by_xpath("//*[@class='button btn--rounded btn-primary first-time-flow__button']").click()
    driver.find_element_by_xpath("//button[text()='Import wallet']").click()
    driver.find_element_by_xpath("//button[text()='No Thanks']").click()
    sleep(1)
    InputsMetamask = driver.find_elements_by_xpath('//input')
    InputsMetamask[0].send_keys('') #Mnemonic phrase
    InputsMetamask[1].send_keys('') #Password
    InputsMetamask[2].send_keys('') #Password Confirmation
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

    #---------Переход на рубик и подключение метамаска
    driver.execute_script("window.open('https://app.rubic.exchange/?fromChain=POLYGON&toChain=POLYGON&from=MATIC&to=USDC&amount=0.1')")
    driver.switch_to.window(handles[2])

    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Connect Wallet']")))
    driver.find_element_by_xpath("//span[text()='Connect Wallet']").click()
    driver.find_element_by_xpath("//button[contains(text(), 'MetaMask')]").click()
    sleep(2)
    driver.switch_to.window(handles[3])
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Next']")))
    driver.find_element_by_xpath("//*[text()='Next']").click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Connect']")))
    driver.find_element_by_xpath("//*[text()='Connect']").click()



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


def back_to_burger_and_click(driver):
    driver.execute_script("history.back();")
    wait_elements_clicable(xpath="//*[@class='burger-menu']",driver=driver).click()
