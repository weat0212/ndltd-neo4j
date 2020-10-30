import re
import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
from time import sleep
import pandas as pd

# solution to the error message
# selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 81
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# 收集論文清單
df = []
# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://ndltd.ncl.edu.tw/')
driver.find_element_by_xpath('//a[@title="指令查詢"]').click()
driver.find_element_by_id('ysearchinput0').send_keys('sc="國立中正大學" and "資訊管理系".sdp and "吳帆".ad')
driver.find_element_by_id('gs32search').click()
cookie = re.findall(r'ccd=(.*?)/', driver.current_url)[0]

# Find the amount papers of MIS CCU
num = driver.find_element_by_xpath('//*[@id="bodyid"]/form/div/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/div[1]/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td[2]/span[2]').text
amount = int(num.strip())
print("一共有：", amount, "筆資料")

i = 1
while i <= amount:
    try:
        print('='*80)
        print('Dealing with ', str(i),'...')
        info1,   info2,  info3,  info4,  info5,  info6,  info7,  info8,  info9, info10, info11, info12, info13, info14, info15, info16, info17, info18, info19, info20, info21, info22, info23, info24, info25 = ['']*25
        driver.get('https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd={}/record?r1={}&h1=0'.format(cookie, i))
        soup = BeautifulSoup(driver.page_source)

        # 論文基本資料
        tbody = soup.find('table',{'id':'format0_disparea'})

        # 連結網址
        url = tbody.find('input',{'id':'fe_text1'})['value']
        print('連結網址：', url)

        # 研究生
        for element in tbody.select('tr'):
            if '研究生' in element.text:
                info1 = element.find('a').text
                break    
        print('研究生:', info1)

        # 研究生_外文
        for element in tbody.select('tr'):
            if '研究生(外文)' in element.text:
                info2 = element.find('a').text
                break    
    #     print('研究生_外文:', info2)

        # 論文名稱
        for element in tbody.select('tr'):
            if '論文名稱' in element.text:
                info3 = element.find('td').text
                break    
        print('論文名稱:', info3)

        # 論文名稱_外文
        for element in tbody.select('tr'):
            if '論文名稱(外文)' in element.text:
                info4 = element.find('td').text
                break   
    #     print('論文名稱_外文:', info4)

        # 指導教授
        for element in tbody.select('tr'):
            if '指導教授' in element.text:
                info5 = element.find('td').text
                break   
        print('指導教授:', info5)

        # 指導教授_外文
        for element in tbody.select('tr'):
            if '指導教授(外文)' in element.text:
                info6 = element.find('td').text
                break   
    #     print('指導教授_外文:', info6)

        # 學位類別
        for element in tbody.select('tr'):
            if '學位類別' in element.text:
                info7 = element.find('td').text
                break   
    #     print('學位類別:', info7)

        # 校院名稱
        for element in tbody.select('tr'):
            if '校院名稱' in element.text:
                info8 = element.find('td').text
                break   
        print('校院名稱:', info8)

        # 系所名稱
        for element in tbody.select('tr'):
            if '系所名稱' in element.text:
                info9 = element.find('td').text
                break   
        print('系所名稱:', info9)

        # 學門
        for element in tbody.select('tr'):
            if '學門' in element.text:
                info10 = element.find('td').text
                break   
    #     print('學門:', info10)

        # 學類
        for element in tbody.select('tr'):
            if '學類' in element.text:
                info11 = element.find('td').text
                break   
    #     print('學類:', info11)

        # 論文出版年
        for element in tbody.select('tr'):
            if '論文出版年' in element.text:
                info12 = element.find('td').text
                break   
    #     print('論文出版年:', info12)

        # 畢業學年度
        for element in tbody.select('tr'):
            if '畢業學年度' in element.text:
                info13 = element.find('td').text
                break   
    #     print('畢業學年度:', info13)

        # 語文別
        for element in tbody.select('tr'):
            if '語文別' in element.text:
                info14 = element.find('td').text
                break   
    #     print('語文別:', info14)

        # 論文頁數
        for element in tbody.select('tr'):
            if '論文頁數' in element.text:
                info15 = element.find('td').text
                break   
    #     print('論文頁數:', info15)

        # 中文關鍵詞
        for element in tbody.select('tr'):
            if '中文關鍵詞' in element.text:
                info16 = element.find('td').text
                break   
    #     print('中文關鍵詞:', info16)

        # 外文關鍵詞
        for element in tbody.select('tr'):
            if '外文關鍵詞' in element.text:
                info17 = element.find('td').text
                break   
    #     print('外文關鍵詞:', info17)

        # 被引用
        for element in tbody.select('tr'):
            if '相關次數' in element.text:
                info18 = element.findAll('li')[0].text
                info18 = re.sub('被引用:','',info20)
                break   
    #     print('被引用:', info18)

        # 點閱
        for element in tbody.select('tr'):
            if '相關次數' in element.text:
                info19 = element.findAll('li')[1].text
                break   
    #     print('點閱:', info19)

        # 下載
        for element in tbody.select('tr'):
            if '相關次數' in element.text:
                info20 = element.findAll('li')[3].text
                info20 = re.sub('下載:','',info20)
                break   
    #     print('下載:', info20)

        # 書目收藏
        for element in tbody.select('tr'):
            if '相關次數' in element.text:
                info21 = element.findAll('li')[4].text
                info21 = re.sub('書目收藏:','',info21)
                break   
    #     print('書目收藏:', info21)

        # 摘要
        try:
            info22 = soup.find('td',{'class':'stdncl2'}).text
        except:
            info22 = ''
    #     print('摘要：', info22)
        # 口試委員
        for element in tbody.select('tr'):
            if '口試委員' in element.text:
                info24 = element.find('td').text
                break   
        #     print('口試委員:', info24)

        # 口試委員_外文
        for element in tbody.select('tr'):
            if '口試委員(外文)' in element.text:
                info25 = element.find('td').text
                break   
        #     print('口試委員_外文:', info25)

        # 引用
        info23 = str(soup.find('div',{'style':'padding:10px;text-align:left;'}))
    #     print('引用：', info23)
        ndf = pd.DataFrame([{'研究生:':info1,
                             '研究生_外文':info2,
                             '論文名稱':info3,
                             '論文名稱_外文:':info4,
                             '指導教授':info5,
                             '指導教授_外文':info6,
                             '口試委員':info24,
                             '口試委員_外文':info25,                         
                             '學位類別':info7,
                             '校院名稱':info8,
                             '系所名稱':info9,
                             '學門':info10,
                             '學類':info11,
                             '論文出版年':info12,
                             '畢業學年度':info13,
                             '語文別':info14,
                             '論文頁數':info15,
                             '中文關鍵詞':info16,
                             '外文關鍵詞':info17,
                             '相關次數':info18,
                             '點閱':info19,
                             '下載':info20,
                             '書目收藏':info21,
                             '摘要':info22,
                             '引用':info23,
                             '連結網址':url}])
        df.append(ndf)
        i += 1
    except:
        driver.close()
        sleep(2)
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(ChromeDriverManager().install())
        sleep(1)
        driver.get('https://ndltd.ncl.edu.tw/')
        sleep(5)
        driver.find_element_by_xpath('//a[@title="指令查詢"]').click()
        sleep(1)
        driver.find_element_by_id('ysearchinput0').send_keys('sc="國立中正大學" and "資訊管理系".sdp and "吳帆".ad')
        driver.find_element_by_id('gs32search').click()
        sleep(3)
        cookie = re.findall(r'ccd=(.*?)/', driver.current_url)[0]


# Export Part
pd.concat(df, ignore_index=True).to_excel('./dataset/MISCCU.xlsx')
pd.concat(df, ignore_index=True).to_pickle('./dataset/MISCCU.pickle')

# distinct by 學門校系
df2 = pd.concat(df, ignore_index=True)
df2.info()


tmp = df2.groupby(['校院名稱','系所名稱','學類','學門']).size().reset_index()
tmp.columns = ['學類', '學門', '校院名稱', '系所名稱', '則數']
tmp.to_excel('校系學門學類.xlsx')

driver.close