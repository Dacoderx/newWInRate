from selenium import webdriver
from selenium.webdriver import ChromeOptions
import pandas as pd
import csv

options = ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)
driver.get('https://na.op.gg/statistics/champion/')

rows = driver.find_elements_by_xpath('//*[@id="ChampionStatsTable"]//tr[./td]')
data = []
for row in rows:
    name = row.find_element_by_xpath('./td[@class="Cell ChampionName"]').text
    win_rate = row.find_element_by_xpath('./td[@class="Cell ChampionName"]/following-sibling::td[1]').text
    print(name + ': ' + win_rate)
    #data.append({'Champion':name, 'Winrate': win_rate})
#df = pd.DataFrame(data)
#print(df)
#df.to_csv('championWinRate.csv')
