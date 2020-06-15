from selenium import webdriver

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)


browser.find_element_by_tag_name("#dropdown").click()
browser.find_element_by_css_selector("[value='45']").click()