from selenium import webdriver
import time
import unittest


class Test(unittest.TestCase):
    def test_reg(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('.form-control.first')
        input1.send_keys("Ivan")

        input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        input2.send_keys("Petrov")

        input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        input3.send_keys("shaulukhov12@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('.form-control.first')
        input1.send_keys("Ivan")

        input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        input2.send_keys("Petrov")

        input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        input3.send_keys("shaulukhov12@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, welcome_text_elt, "Некорректный результат")
        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    unittest.main()