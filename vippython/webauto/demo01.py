from selenium import webdriver
from time import sleep

wd = webdriver.Chrome(r'f:\mytools\chromedriver.exe')

wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
sleep(5)
elements =wd.find_elements_by_class_name('animal')
element = wd.find_element_by_css_selector('#searchtext')
print(element.get_attribute('outerHTML'))

wd.quit()