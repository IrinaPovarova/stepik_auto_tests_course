from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    input1 = browser.find_element(
        By.XPATH, "//input[contains(@placeholder , 'first')]")
    input1.send_keys("Irina")
    input2 = browser.find_element(
        By.XPATH, "//input[contains(@placeholder , 'last')]")
    input2.send_keys("Povarova")
    input3 = browser.find_element(
        By.XPATH, "//input[contains(@placeholder , 'email')]")
    input3.send_keys("iip12345@yandex.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
