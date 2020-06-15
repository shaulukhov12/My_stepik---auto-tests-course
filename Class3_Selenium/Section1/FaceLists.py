from selenium import webdriver
import time, random


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

        time.sleep(1)
        #Переходим на страницу списков лиц
        button = browser.find_element_by_id("at-dashboard_page-appbar_goto_face_button")
        button.click()

        time.sleep(1)
        #Кликаю на добавление списка
        button = browser.find_element_by_css_selector(".MuiButton-sizeSmall")
        button.click()

        time.sleep(1)
        # Ввожу имя списка
        input3 = browser.find_element_by_name('[name="name"]')
        time.sleep(1)
        input3.send_keys('New')
        #button.click(input3)

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
