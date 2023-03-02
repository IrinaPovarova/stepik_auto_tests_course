# Открыть страницу http://suninjuly.github.io/wait1.html
# Нажать на кнопку "Verify"
# Проверить, что появилась надпись "Verification was successful!"

from selenium import webdriver
# from selenium import webdriver_manager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome import ChromeDriverManager
import time

try:
    link = "http://suninjuly.github.io/wait2.html"

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(
        options=options, executable_path=r'C:\chromedriver\chromedriver.exe')

    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()
    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
