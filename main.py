from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import sqlite3

#Downloading the CSV file
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('--start-maximized')
driver = webdriver.Chrome(options=chrome_opt)
driver.get('https://jobs.homesteadstudio.co/data-engineer/assessment/download')
button = driver.find_element(by=By.CLASS_NAME, value='wp-element-button')
button.click()

# Pivot and Aggregate Table
data = pd.read_csv('skill_test_data.csv')
pivoted_table = data.pivot_table(index='Platform (Northbeam)',values=['Spend', 'Attributed Rev (1d)', 'Imprs', 'Visits', 'New Visits', 'Transactions (1d)', 'Email Signups (1d)'], aggfunc='sum', sort='')
pivoted_table.sort_values(by=('Attributed Rev (1d)'), ascending=False)
print(pivoted_table)

# Uploading to database
conn = sqlite3.connect('database.db')
pivoted_table.to_sql('test_data', conn, if_exists='replace')
conn.close()






