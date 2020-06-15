from selenium import webdriver
import time


class Auth:
    try:
        link = "https://axxoncloud-test2.axxonnet.com/"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('[placeholder="Имя пользователя или email"]')
        input1.send_keys("shaulukhov12@gmail.com")

        input2 = browser.find_element_by_css_selector('[placeholder="Пароль"]')
        input2.send_keys("123123")

        # Отправляем заполненную форму
        button = browser.find_element_by_id("at-login_page-login_button")
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
