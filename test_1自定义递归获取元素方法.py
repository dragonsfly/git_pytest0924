import time

from appium import webdriver

# server 启动参数
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
# 设备信息
# 大小写无所谓
desired_caps['platformName'] = 'Android'
# 比如版本是5.2.3，可以写成 “5.2.3”，“5.2”，“5”
desired_caps['platformVersion'] = '4'
# android随便写，但是不能不写，也不能为空字符串
# iOS不能随便写，写成“iPhone 8”
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# 自定义查找元素
def get_element(feature):
    """
    如果没找到元素，返回None，找到了返回该元素
    :return:
    """
    wait = WebDriverWait(driver, 5, 1)
    try:
        ele = wait.until(lambda x: x.find_element(*feature))
    except Exception:
        return None
    else:
        return ele


# 自定义获取屏幕尺寸
def get_size():
    return driver.get_window_size()


# 自定义向上滑动
def swipe_up():
    w = get_size()["width"]
    h = get_size()["height"]
    driver.swipe(w * 3 / 4, h / 2, w / 4, h / 2)


# 自定义向左滑动
def swipe_left():
    w = get_size()["width"]
    h = get_size()["height"]
    driver.swipe(w / 2, h*3 / 4, w / 2, h / 4)

# 自定义工具方法实现元素点击
def execute_tap(feature):
    action=ActionChains(driver)
    # 判断传入是是否为元祖
    if isinstance(feature,tuple):
        feature = get_element(feature)
    action.tap(feature).perform()

# 自定义方法实现滑屏查找元素
def get_ele_recusion(feature):
    obj = get_element(feature)
    if obj:
        return obj
    # 如果没有找到，滑屏再查找
    else:
        swipe_up()
        get_ele_recusion(feature)


btn_more=By.XPATH,"//*[@text='更多']"

get_ele_recusion(btn_more)
execute_tap(btn_more)
