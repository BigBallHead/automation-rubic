from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from main import wait_elements_clicable
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def check_token():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://app.rubic.exchange/")
    wait_elements_clicable(xpath="//*[@id='token1']", driver=driver).click()
    driver.find_element(by='xpath', value=("//input[@tabindex='0']")).send_keys("USDC")
    sleep(2)
    try:
        usdc_coin = driver.find_element(by='xpath', value=("//*[@alt='USD Coin']"))
        print("Token search is alive!!!")
    except NoSuchElementException:
        print("I cannot find this coin ((")

    driver.quit()

if __name__ == '__main__':

    while True:
        check_token()
        sleep(3600)
