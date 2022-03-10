from selenium import webdriver

wd = webdriver.Chrome(r'f:\mytools\chromedriver.exe')
wd.get('http:\\www.baidu.com')
wd.find_element_by_id('kw').send_keys('白月黑羽 ')
wd.find_element_by_id('su').click()
wd.implicitly_wait(10)
element = wd.find_element_by_id(1)
print(element.get_attribute('srcid'))
wd.quit()