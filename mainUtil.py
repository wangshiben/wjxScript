import random
import time

import requests
from selenium import webdriver


def setting1(ip):
    ipp = requests.get(ip).text
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    option.add_argument(f"--proxy-server=http://{ipp}")
    broswer = webdriver.Chrome(options=option)

    broswer.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                            {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    return broswer


def setting2():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)

    broswer = webdriver.Chrome(options=option)
    broswer.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                            {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    return broswer


def SingleChoiceInTwo(broswer, num, weight=None):  ## 二选一单选
    h = broswer.find_elements(by='css selector',
                              value=f'#div{num}  > .ui-controlgroup.column1 > div:nth-child(n) > span > a')
    a = random.choices(list(range(len(h))), weights=weight)
    # a = h[weight]
    h[a[0]].click()
    time.sleep(0.5)
    # div7 > div.ui-controlgroup.column1 > div:nth-child(1) > span > a


def LateralSelection(broswer, num, weight=None):  ## 横向选择  满意度选择0(不满意)->5(满意)
    h = broswer.find_elements(by='css selector',
                              value=f'#div{num} > .scale-div.defaultScale > .scale-rating > .modlen5 > li:nth-child(n) > a')
    a = random.choices(list(range(len(h))), weights=weight)
    h[a[0]].click()


def SingleChoice(broswer, num, weight=None): ## 单选
    h = broswer.find_elements(by='css selector',
                              value=f'#div{num} > div.ui-controlgroup.column1 > div:nth-child(n) > span > a')
    a = random.choices(list(range(len(h))), weights=weight)
    h[a[0]].click()



def NextPage(broswer):## 下一页
    broswer.find_element('css selector', '#divNext > a').click()


def MultiChoice(broswer, num, weight=None, k=2):## 多选
    h = broswer.find_elements(by='css selector',
                              value=f'#div{num} > div.ui-controlgroup.column1 > div:nth-child(n) > span > a')
    a = random.choices(list(range(len(h))), weights=weight, k=k)
    while a[0] == a[1]:
        a = random.choices(list(range(len((h)))), weights=weight, k=2)
    h[a[0]].click()
    h[a[1]].click()


def FillBlank(broswer, data, list):## 填空
    answer = random.choice(list)
    broswer.find_elements(by='id', value=f'q{data}')[0].send_keys(answer)


def SubmitResult(broswer):  ## 提交结果
    numb2 = broswer.find_elements(by='class name', value='voteDiv')
    time.sleep(0.5)
    numb2[0].click()
    try:
        numb2 = broswer.find_element(by='css selector', value='#ctlNext').click()
        numb2[0].click()
    except:
        pass
    time.sleep(3)
    # 结束
    broswer.quit()

# drv2_1 > td:nth-child(2) > a
