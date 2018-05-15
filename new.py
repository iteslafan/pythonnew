# -*- coding:utf-8 -*-
#  -$ i'm TeslaT $-
# from clod import create_word_cloud as cw
from selenium import webdriver
import time
from bs4 import BeautifulSoup
driver=webdriver.Chrome()
driver.delete_all_cookies()
id="767008453"
pw='tss123121'
friend_qq=input("请输入好友的QQ")
driver.maximize_window()
driver.get('http://i.qq.com')
driver.switch_to.frame('login_frame')
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys(id)
driver.find_element_by_id('p').send_keys(pw)
driver.find_element_by_id('login_button').click()
driver.switch_to.default_content()
driver.get('https://user.qzone.qq.com/'+friend_qq+'/311')

# try:
#     button=driver.find_element_by_id('dialog_button_111').click()
# except:
#     pass
next_num=0
while True:
    for i in range(0,5):
        height=20000*i
        strWord='window.scrollBy(0,'+str(height)+')'
        driver.execute_script(strWord)
        time.sleep(2)
    driver.switch_to.frame('app_canvas_frame')
    content=BeautifulSoup(driver.page_source,'html5lib')
    # print(content)
    # print('======')
    ol=content.find('div',class_='feed_wrap').ol
    # print(type(oll))
    # print(oll)
    lis= ol.find_all('li',class_='feed')
    with open('l_word.txt','a',encoding='utf-8') as f:
        for li in lis:
            bd=li.find('div',class_='bd')
            ss_content=bd.pre.get_text()
            f.write(ss_content+'\n')
    # if driver.page_source.find('page_next_' +str(next_num))== -1:
    #     break
    if next_num>40:
        break

    driver.find_element_by_id('pager_next_'+str(next_num)).click()
    next_num += 1
    driver.switch_to.parent_frame()
