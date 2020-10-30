import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager

# *********************************************
# **************  BUG FIX NEEDED  *************
# *********************************************

df = []
r1 = 1
while r1 <= 249:
    columns = []
    values = []
    try:
        res2 = requests.get('https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd={}/record?r1={}&h1=1'.format(cookie, r1))
        soup = BeautifulSoup(res2.text)
        for i in soup.find('table', {'id':'format0_disparea'}).findAll('tr'):
            if 'std1' in str(i):
#                 print(i.find('th',{'class':'std1'}).text)
                columns.append(i.find('th',{'class':'std1'}).text)
#                 print(i.find('td',{'class':'std2'}).text)
                values.append(i.find('td',{'class':'std2'}).text)
        
        # 永久網址
        columns.append('永久網址')
        try:
            permanent = soup.find('input',{'id':'fe_text1'})['value']
        except:
            permanent = ''
        values.append(permanent)
        
        
        # 摘要
        columns.append('摘要')
        try:
            abst = soup.find('td',{'class':'stdncl2'}).text
        except:
            abst = ''
        values.append(abst)
#         print('摘要：', abst)
        
        # 引用
        columns.append('引用')
        try:
            Quote = str(soup.find('div',{'style':'padding:10px;text-align:left;'}))
        except:
            Quote = ''
        values.append(Quote)
#         print('引用：', Quote)
        
        ndf = pd.DataFrame(data=values, index=columns).T
        print('論文名稱：',ndf['論文名稱'])
        print('永久網址：', ndf['永久網址'])
        df.append(ndf)
        r1 += 1  
        print('='*88)
    except:
        # Cookie 失效時自動重啟 Selenium 取得新的 Cookie，並更新參數
        print('Get New Cookie')
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver = webdriver.Chrome()
        driver.get('https://ndltd.ncl.edu.tw/')
        sleep(2)
        driver.find_element_by_xpath('//a[@title="指令查詢"]').click()
        sleep(2)
        driver.find_element_by_id('ysearchinput0').send_keys('sc="國立中正大學" and "資訊管理系".sdp')
        sleep(0.5)
        driver.find_element_by_id('gs32search').click()
        sleep(2)
        cookie = re.findall(r'ccd=(.*?)/', driver.current_url)[0]
        driver.close()
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                 'Cookie': 'ccd={}'.format(cookie)}
        
        payload = {'qs0': 'sc="國立中正大學" and "資訊管理系".sdp',
                   'qf0': '_hist_',
                   'gs32search.x': '27',
                   'gs32search.y': '9',
                   'displayonerecdisable': '1',
                   'dbcode': 'nclcdr',
                   'action':'',
                   'op':'',
                   'h':'',
                   'histlist':'',
                   'opt': 'm',
                   '_status_': 'search__v2'}
        
        rs = requests.session()
        res = rs.post('https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd={}/search'.format(cookie),data=payload, headers=headers)

df = pd.concat(df, ignore_index=True)
print(df.shape)
df

df.to_pickle('./博碩士論文.pickle')
df.to_excel('./博碩士論文.xlsx')

# distinct by 學門校系
df2 = pd.concat(df, ignore_index=True)
df2.info()

tmp = df2.groupby(['校院名稱','系所名稱','學類','學門']).size().reset_index()
tmp.columns = ['學類', '學門', '校院名稱', '系所名稱', '則數']
tmp.to_excel('校系學門學類.xlsx')