import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import datetime
time=''#we can add ?date=week,?date=month,?date=week3month etc to select the timeframe we want to choose
baseurl='https://www.dotabuff.com/items' #this is the basic url it retrieves the item data of the current month
page=requests.get(url,headers={'user-agent':'item-scraper v0.1'})#we request the contents of the page
df=pd.DataFrame(columns=['item','times_used','use_rate','win_rate'])#we create a dataframe with the columns of the webtable
soup=bs(page.content,'html.parser')#we pass it to BeautifulSoup
#We start diggin into the html until we find the contents of the table
html=list(soup.children)[1]
body=list(html.children)[1]
div=list(body.children)[0]
div2=list(div.children)[7]
div3=list(div2.children)[2]
section=list(div3.children)[0]
article=list(section.children)[1]
table=list(article.children)[0]
tbody=list(table.children)[1]
items=list(tbody.children)
#once we are there we extract the data for each row on the original table
for i in range(len(items)):
    list_item=list(items[i].children)
    df=df.append(pd.Series([list_item[1].get_text(),list_item[2].get_text(),list_item[3].get_text(),list_item[4].get_text()],index=df.columns),ignore_index=True)
df['date']=datetime.today().strftime('%Y-%m-%d')
csv_name='item_data_'+str(datetime.today().strftime('%Y-%m-%d'))+'.csv'
df.to_csv(csv_name,sep=';')
