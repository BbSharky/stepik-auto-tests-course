from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x, y):
  return str(int(x) + int(y))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('h2>span#num1')
    x = x_element.text
    y_element = browser.find_element_by_css_selector('h2>span#num2')
    y = y_element.text
    c = calc(x, y)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(c)

    button = browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()



