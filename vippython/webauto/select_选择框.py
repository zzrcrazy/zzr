from selenium import webdriver
from selenium.webdriver.support.ui import Select

wd = webdriver.Chrome(r'f:\mytools\chromedriver.exe')
wd.get('http://cdn1.python3.vip/files/selenium/test2.html')

# 创建Select对象
# select = Select(wd.find_element_by_id("ss_single"))
# 通过 Select 对象选中小雷老师
# select.select_by_visible_text("小雷老师")
# select.select_by_index(1) # 从0开始
# wd.quit()
select = Select(wd.find_element_by_id("ss_multi"))
select.deselect_all()
select.select_by_index(0)
select.select_by_index(1)