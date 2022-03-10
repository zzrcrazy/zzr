from selenium import webdriver

wd = webdriver.Chrome(r'f:\mytools\chromedriver.exe')
wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')

# wd.switch_to.frame('frame1')  通过ID
# wd.switch_to.frame('innerFrame')  通过name
wd.switch_to.frame(wd.find_element_by_css_selector('iframe[src="sample1.html"]'))   # 通过其他元素
elements = wd.find_elements_by_css_selector('.plant')
for element in elements:
    print(element.get_attribute('outerHTML'))
wd.switch_to.default_content()
wd.find_element_by_id('outerbutton').click()
wd.quit()