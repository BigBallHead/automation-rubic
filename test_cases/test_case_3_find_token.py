from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager

from utils.base import wait_elements_clicable


def check_token():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://app.rubic.exchange/")
    wait_elements_clicable(xpath="//*[@id='token1']", driver=driver).click()
    driver.find_element(by='xpath', value="//input[@tabindex='0']").send_keys("USDC")
    try:
        usdc_coin = driver.find_element(
            by='xpath',
            value="//*[@alt='USD Coin']"
        )

        print("Token search is alive!!!")
    except NoSuchElementException:
        print("I cannot find this coin ((")

    driver.quit()


if __name__ == '__main__':

    while True:
        check_token()
        sleep(3600)
