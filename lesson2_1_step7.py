import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    a = a_element.get_attribute("valuex")
    y = calc(a)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check.click()
    button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    button.click()
    submit = browser.find_element(By.CSS_SELECTOR, "button")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
