# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "https://SunInJuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Fedorov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("first@print.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))

    file_name = "file_example.txt"
# получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, file_name)
    print(file_path)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
