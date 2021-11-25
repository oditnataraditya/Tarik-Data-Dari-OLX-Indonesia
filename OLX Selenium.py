from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pandas as pd

profile_path = r'C:\Users\Acer\AppData\Roaming\Mozilla\Firefox\Profiles\51rk56w7.default'
options=Options()
options.set_preference = ('profile', profile_path)
options.headless = False
service = Service(r'D:\Python YGB\Scraper\geckodriver.exe')
driver = webdriver.Firefox(options=options, service=service)

driver.get("https://www.olx.co.id/bali_g2000002/dijual-rumah-apartemen_c5158?filter=price_max_400000000")
for i in range(50):
    try:
        last_height = driver.execute_script("return document.documentElement.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            break


        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_20FqS')))
        cons = driver.find_element(By.CLASS_NAME, '_20FqS')
        cons.location_once_scrolled_into_view
        cons.click()
    except:
        continue

driver.implicitly_wait(2)

jumlah = driver.find_elements(By.XPATH, '/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li')

links = []
hargas = []
kamars = []
desc = []
locs = []
dates = []
for x in range(1,len(jumlah)): 
    if x != 7:
        try:  
            harga = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li[{x}]/a/div/span[1]').text
            kamar = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li[{x}]/a/div/span[2]').text
            mini_desc = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li[{x}]/a/div/span[3]').text
            lokasi = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li[{x}]/a/div/div[2]/span[1]').text
            date_iklan = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li[{x}]/a/div/div[2]/span[2]').text
            link = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li[{x}]/a').get_attribute('href')
        except:
            harga = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li[{x}]/a/div/span[1]').text
            kamar = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li[{x}]/a/div/span[2]').text
            mini_desc = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li[{x}]/a/div/span[3]').text
            lokasi = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li[{x}]/a/div/div/span[1]').text
            date_iklan = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li[{x}]/a/div/div/span[2]').text
            link = driver.find_element(By.XPATH, f'/html/body/div[1]/div/main/div/div/section/div/div/div[5]/div[2]/div/div[3]/ul/li[{x}]/a').get_attribute('href')
        finally:
            hargas.append(harga)
            kamars.append(kamar)
            desc.append(mini_desc) 
            locs.append(lokasi)
            dates.append(date_iklan) 
            links.append(link)
    else:
        pass

list_to_pd = {
    "Harga Rumah" : hargas,
    "Jumlah Kamar" : kamars,
    "Mini Deskripsi" : desc,
    "Lokasi Rumah" : locs,
    "Tanggal Upload Iklan" : dates,
    "Link Iklan" : links
}
df = pd.DataFrame(list_to_pd)
df.to_csv("Rekapan total OLX.csv", index=False)