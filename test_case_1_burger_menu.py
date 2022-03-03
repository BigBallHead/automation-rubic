from selenium import webdriver
from functions import wait_elements_clicable
from functions import wait_elements_located
from functions import back_to_burger_and_click

driver = webdriver.Chrome(executable_path="/Users/ivankondratev/Desktop/automation.rubic/chromedriver-3")
driver.maximize_window()
driver.get("https://app.rubic.exchange/")

"""
Тест ссылки "О компании"
"""
wait_elements_clicable(xpath="//*[@class='burger-menu']",driver=driver).click()
driver.find_element_by_xpath("//button[contains(text(), 'О компании')]").click()
link1 = wait_elements_located("//button[contains(text(), 'Start Trading')]", driver=driver)
if link1:
    print('ССЫЛКА "О КОМПАНИИ" РАБОТАЕТ')
    back_to_burger_and_click(driver)

"""
Тест ссылки "Онрампер"
"""
driver.find_element_by_xpath("//button[contains(text(), 'Fiat on-ramp')]").click()
iframe = driver.find_elements_by_tag_name('iframe')
driver.switch_to.frame(iframe[0])
print(iframe)
link2 = wait_elements_located("//button[text()='Buy ETH']",driver=driver)
if link2:
    print('РЕДИРЕКТ НА ОНРАМПЕР РАБОТАЕТ')
    back_to_burger_and_click()

"""
Тест ссылки "FAQ"
"""
driver.find_element_by_xpath("//button[contains(text(), 'FAQ')]").click()
link3 = wait_elements_located("//*[text()='FAQ']",driver=driver)
if link3:
    print("РЕДИРЕКТ НА СТРАНИЦУ FAQ РАБОТАЕТ")
    driver.execute_script("history.back();")

print("ВЫХОД ИЗ БРАУЗЕРА")
driver.quit()