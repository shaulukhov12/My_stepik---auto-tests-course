import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()


@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1/"
    browser.get(link)
    browser.implicitly_wait(5)
    input1 = browser.find_element_by_css_selector(".textarea.string-quiz__textarea")
    input1.click()
    answer = math.log(int(time.time()))
    input1.send_keys(str(answer))

    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    browser.implicitly_wait(5)

    button2 = browser.find_element_by_css_selector(".smart-hints__hint")
    words = button2.text
    assert "Correct!" in words
