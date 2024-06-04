from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Функция для расчета математической функции от x
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Считываем значение переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Проскроллить страницу вниз
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 1000);")

    # Ввести ответ в текстовое поле
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Выбираем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Переключаем radiobutton "Robots rule!"
    robot_radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radiobutton)
    time.sleep(1)  # Даем время странице обновиться после скролла

    # Кликаем на радиокнопку
    robot_radiobutton.click()

    # Нажимаем на кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()
