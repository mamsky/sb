from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import sys
import psutil
import getpass
import os
import datetime
import time

link_produk = time_target=None
sekarang = datetime.datetime.now()

def banner():
        print('\033[94m==========================================')
        print('''\033[91m==========================================|
| ______  ___  ______ _______   __    |   |
| | ___ \/ _ \ | ___ \  _  \ \ / /    |   |
| | |_/ / /_\ \| |_/ / | | |\ V /     |   |
| |  __/|  _  ||  __/| | | | \ /      |   |
| | |   | | | || |   \ \_/ / | |      |   |
| \_|   \_| |_/\_|    \___/  \_/      |   |
|                                     |   |
|buatan sansboy by: Paste             |   |
==========================================|''')
        print('\033[94m==========================================')
banner()

def InputData() :
    global link_produk,time_target,sekarang
    link_produk = input('(#) Link web : ')
    ### Jam keberapa
    jam = int(input('(#) Jam Beli : '))
    ### Menit keberapa
    menit = int(input('(#) Menit Beli : '))
    ### Detik keberapa
    detik = int(input('(#) Detik Beli : '))
    time_target=datetime.datetime(sekarang.year,sekarang.month,sekarang.day,jam,menit,detik)

InputData()
# Inisialisasi ChromeDriver
driver = webdriver.Chrome()

# Membuka situs web
driver.get("https://www.google.com/")

selisih = time_target-datetime.datetime.now()
print('(#) Harap Menunggu... ')
time.sleep(selisih.seconds)
driver.get(link_produk)
print('(#) Browser Refresh... ')

def click(driiver,element_css):
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, element_css))
    )
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, element_css))
    )
    driver.find_element_by_css_selector(element_css).click()


click(driver, '.lp-button--label')

#click(driver,'button.btn--l:nth-child(2)')
#WebDriverWait(driver, 10).until(
#    ec.invisibility_of_element((By.CSS_SELECTOR, '.action-toast'))

