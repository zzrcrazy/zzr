from selenium import webdriver

wd = webdriver.Chrome(r'f:\mytools\chromedriver.exe')
wd.implicitly_wait(5)

wd.get('http://cdn1.python3.vip/files/selenium/sample3.html')
# 选择链接并点击进入
wd.find_element_by_css_selector('a[target="_blank"]').click()
mainWindow = wd.current_window_handle  # 保存当前窗口handle
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break
print(wd.title)
wd.switch_to.window(mainWindow)     # 切换到原窗口
print(wd.title)
