link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
# В конфиг файле создаем правило скажем так на то что через команду сможем выбирать в какой браузере запускать тест