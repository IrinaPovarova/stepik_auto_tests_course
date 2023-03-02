# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответом

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/redirect_accept.html"

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(
        options=options, executable_path=r'C:\chromedriver\chromedriver.exe')
    browser.get(link)

    btn_submit = browser.find_element(By.CLASS_NAME, "trollface.btn")
    btn_submit.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    new_link = "http://suninjuly.github.io/redirect_page.html?"
    browser.get(new_link)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer_value = browser.find_element(By.ID, "answer")
    answer_value.send_keys(y)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
