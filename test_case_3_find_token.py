from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from main import wait_elements_clicable
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def check_token():
    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.get("https://app.rubic.exchange/")
    wait_elements_clicable(xpath="//*[@id='token1']", driver=browser).click()
    browser.find_element(by='xpath', value=("//input[@tabindex='0']")).send_keys("USDC")
    sleep(2)
    try:
        usdc_coin = browser.find_element(by='xpath', value=("//*[@alt='USD Coin']"))
        print("Token search is alive!!!")
    except NoSuchElementException:
        print("I cannot find this coin ((")

    browser.quit()

check_token()

if __name__ == '__main__':

    while True:
        check_token()
        sleep(3600)
