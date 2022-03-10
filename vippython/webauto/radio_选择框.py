from selenium import webdriver

wd = webdriver.Chrome(r'f:\mytools\chromedriver.exe')
wd.get('http://cdn1.python3.vip/files/selenium/test2.html')
element = wd.find_element_by_css_selector('#s_radio input[value="小雷老师"]')
element.click()
print('当前选中的是:'+element.get_attribute('value'))
wd.quit()