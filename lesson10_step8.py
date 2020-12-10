from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    #задаём кнопку
    button = browser.find_element_by_css_selector('button.btn')
    # потом говорим Selenium проверяй в течение 15 секунд, пока цена не станет 100$
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    submit = browser.find_element_by_css_selector('button#solve')

    x_value = browser.find_element_by_css_selector('span#input_value')
    x = x_value.text
    n = calc(x)

    input = browser.find_element_by_css_selector('input#answer')
    input.send_keys(n)

    submit.click()

finally:
    time.sleep(10)
    browser.quit()
