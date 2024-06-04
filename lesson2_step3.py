from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Находим элементы с числами
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)

    # Считаем сумму чисел
    total = str(num1 + num2)

    # Выбираем значение равное сумме в выпадающем списке
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(total)

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
