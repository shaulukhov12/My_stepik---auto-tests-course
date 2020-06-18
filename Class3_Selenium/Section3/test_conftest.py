link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
# Тест с запуском фикстуры browser из внешнего конфиг файла который в идеале должен распологаться в той же папке.
#selenium_course_solutions/
#├── section3
#│   └── conftest.py
#│   └── test_languages.py
#├── section4
#│   └── conftest.py
#│   └── test_main_page.py
#
#правильно!