from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Чтение значения для переменной x
    x_element = browser.find_element(By.ID, 'input_value')  # Исправлено на ID
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")  # Убран символ #
    input1.send_keys(y)

    input2 = browser.find_element(By.ID, 'robotCheckbox')  # Убран символ #
    input2.click()

    input3 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    input3.click()

    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
