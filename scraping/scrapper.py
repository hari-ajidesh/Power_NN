from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import pandas as pd
import lxml

df = pd.read_excel(r'vessel_data.xlsx')
ship_ids = df['id'].to_list()
urls = [];
for id in ship_ids:
    url = 'https://www.fleetmon.com/vessels/' + id + '/#tab-datasheet'
    urls.append(url)

frames=[]
for url in urls:
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome("chromedriver", options=options)
    driver.get("https://www.fleetmon.com/")
    button = driver.find_element_by_xpath ("//a[contains( text( ), 'Sign In')]")
    button.click()
    username = driver.find_element_by_id("id_username")
    username.clear()
    username.send_keys("your_fleetmon_username_here")

    password = driver.find_element_by_id("id_password")
    password.clear()
    password.send_keys("your_fleetmon_password_here")
    signin = driver.find_element_by_id('button-sign-in')
    signin.click()
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    ul = [a for a in soup.findAll('ul',attrs={'class':'list-unstyled margin-0 laksbfdabfg'})]
    col_names=[x.text for x in ul[0].findAll('span', attrs=None) if x.text!='...']
    col_names=[x for i,x in enumerate(col_names) if i%2==0]
    vals=[x.text for x in ul[0].findAll('span', attrs={'class':'font-daxmedium'})]
    col_names.pop()
    vals.pop()
    vals=[s[1:-1] for s in vals]
    tables = soup.find_all('table')
    vessel_name = pd.read_html(str(tables))[1][0][0][5::]
    col_names.insert(0, 'Vessel_Name')
    vals.insert(0, vessel_name)
    engine_details = pd.read_html(str(tables))[3][0][0][19::]
    col_names.append('Engine')
    vals.append(engine_details)
    data = { k:[v] for (k,v) in zip(col_names, vals)}
    df = pd.DataFrame(data)
    frames.append(df)
    driver.quit()

result = pd.concat(frames)
result.to_excel('output.xlsx')
