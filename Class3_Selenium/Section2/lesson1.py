#checkbox и radiobutton
#option1 = browser.find_element_by_css_selector("[value='python']")
#option1.click()

# <div>
  #<input type="radio" id="python" name="language" checked>
 # <label for="python">Python</label>
#</div>
#<div>
  #<input type="radio" id="java" name="language">
 # <label for="java">Java</label>
#</div>
option1 = browser.find_element_by_css_selector("[for='python']")
option1.click()