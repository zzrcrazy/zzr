from selenium import webdriver

wd = webdriver.Chrome(r'f:\mytools\chromedriver.exe')

wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')

# 根据属性选择元素
element = wd.find_element_by_css_selector('[href="http://www.miitbeian.gov.cn"]')

# 打印出元素对应的html
print(element.get_attribute('outerHTML'))