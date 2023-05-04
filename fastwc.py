
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
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

def InputData() :
    global link_produk,time_target,sekarang
    link_produk = input('(#) Link Produk Shopee : ')
    ### Jam keberapa
    jam = int(input('(#) Jam Beli : '))
    ### Menit keberapa
    menit = int(input('(#) Menit Beli : '))
    ### Detik keberapa
    detik = int(input('(#) Detik Beli : '))
    time_target=datetime.datetime(sekarang.year,sekarang.month,sekarang.day,jam,menit,detik)
# Inisialisasi WebDriver dalam mode headless
banner()
InputData()
driver = webdriver.Chrome()
# Tanpa menampilkan antarmuka grafis
driver.get('https://shopee.co.id/')

# Mendapatkan cookie yang ada
cookies = driver.get_cookies()

# Menyimpan cookie dalam variabel dictionary
cookies_dict = {}
for cookie in cookies:
    cookies_dict[cookie['name']] = cookie['value']

new_cookie = {'name': '_gcl_au', 'value': '1.1.1434682209.1681248787', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_fbp', 'value': 'fb.2.1681248787783.1901678351', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_tt_enable_cookie', 'value': '1', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_ttp', 'value': '3K0Vs7TjrH5GfmCnwRJsU2ltIPh', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'REC_T_ID', 'value': '73f242e6-d8b0-11ed-9a36-f4ee08261bbd', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_F', 'value': 'T7XNqbwPFiINY1yLoSXvW5SHRj5TkHqc', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_med', 'value': 'cpc', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_CLIENTID', 'value': 'VDdYTnFid1BGaUlOcasgvzxyartjraoj', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_gcl_aw', 'value': 'GCL.1681334879.CjwKCAjwrdmhBhBBEiwA4Hx5g2-t0NaOvKJMbi_whXWdrjVEBCAAHXeb5p5VhZbxYGMLZGmaJoHwSRoC888QAvD_BwE', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_gac_UA-61904553-8', 'value': '1.1681334883.CjwKCAjwrdmhBhBBEiwA4Hx5g2-t0NaOvKJMbi_whXWdrjVEBCAAHXeb5p5VhZbxYGMLZGmaJoHwSRoC888QAvD_BwE', 'domain': 'shopee.co.id'}
new_cookie = {'name': '__LOCALE__null', 'value': 'ID', 'domain': 'shopee.co.id'}
new_cookie = {'name': 'csrftoken', 'value': 'D9Z12J3G2NuJrORlfnVFRWnm3HV86eJJ', 'domain': 'shopee.co.id'}
new_cookie = {'name': 'SPC_SI', 'value': 'wcRIZAAAAAA1NFYwdnBJNV5SnwAAAAAAZXZOamhYc3U=', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_QPWSDCXHZQA', 'value': 'd23c8ade-5683-4b93-dc10-b109ca3b55e6', 'domain': 'shopee.co.id'}
new_cookie = {'name': 'AMP_TOKEN', 'value': '%24NOT_FOUND', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_gid', 'value': 'GA1.3.466728682.1683207127', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_ST', 'value': '.ZXpoWDljdGJzSWRLelBwer13uHlQBRdgOLcoZOTdaSxt9donmUowpIBs5xlbZWoQCMDHfPLIO8idbynWGvmH/qXX59Vi21vXLWhPFPRSLqQ3iJCeL6hTD2BJLxay6uYrF1eoyY4JHb0iEA0JRWjn800k2LWr7hSt2Zcnl2ugQrIQOLqYRDXb1pE7Io79dRJg2VqeTWX+eR/X5sOzcK1sxQ==', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_U', 'value': '338487471', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_R_T_ID', 'value': 'VDZyixU18Gg4Vkp4Gu2252KhOd4Z5KFuo4e7Z0Qw3kOcv64A6Pqjt/mEbzSrKjlRBLnuzK531PfjKrS780SP3QBAfT/QB7H02oVwIbcScaleVDjd4f5SRLjqMiLvEVZWtJVEYPEsYYkBl1WHdiWD67UwpwHS85414nzatnFTuxU=', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_R_T_IV', 'value': 'Zm1wZWJyUGRxYngyWVp6Mw==', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_T_ID', 'value': 'VDZyixU18Gg4Vkp4Gu2252KhOd4Z5KFuo4e7Z0Qw3kOcv64A6Pqjt/mEbzSrKjlRBLnuzK531PfjKrS780SP3QBAfT/QB7H02oVwIbcScaleVDjd4f5SRLjqMiLvEVZWtJVEYPEsYYkBl1WHdiWD67UwpwHS85414nzatnFTuxU=', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_T_IV', 'value': 'Zm1wZWJyUGRxYngyWVp6Mw==', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_ga', 'value': 'GA1.3.1024733529.1681248789', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_dc_gtm_UA-61904553-8', 'value': '1', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_IA', 'value': '1', 'domain': 'shopee.co.id'}
new_cookie = {'name': 'shopee_webUnique_ccd', 'value': 'GPjyjkvjIC4gHDI5Xjep8A%3D%3D%7CFhg%2BnOHPeTp0PCPMyVz2JPnXK7vsyrNHt72QGxF3tUC%2BMaGdUwbAX%2Bnp1YKJX1wQjJvvahdPCEUDuHn2%2F8SHSA3CUeRGuP%2BBtMw%3D%7Ccmhcmk0cvGPjODDD%7C06%7C3', 'domain': 'shopee.co.id'}
new_cookie = {'name': 'ds', 'value': '3e682784f422923ca3e030bc0c85b8fc', 'domain': 'shopee.co.id'}
new_cookie = {'name': 'SPC_EC', 'value': 'TkZMdWlVckZ6SGxYeWt6NZm5cDKOeeM11uCSdUsDG+iD2oM6C7LYbw5cw9nECrI9Vi1ujQltuWAbNf1LfeKg0Qaf7vg3FyLn5+XeJgINhWVqCXc44+XIbbZq3gkDgOnecLTpT1mnyrWr1HC6u5OG5qyEpfQUhl9/G/a2K91g698=', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_ga_SW6D8G0HXK', 'value': 'GS1.1.1683207126.10.1.1683207190.57.0.0', 'domain': '.shopee.co.id'}

driver.add_cookie(new_cookie)
driver.refresh()

driver.get(link_produk)

selisih = time_target-datetime.datetime.now()
print('(#) Harap Menunggu... ')
time.sleep(selisih.seconds)
driver.refresh()
print('(#) Browser Refresh... ')

def click(driiver,element_css):
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, element_css))
    )
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, element_css))
    )
    driver.find_element_by_css_selector(element_css).click()


click(driver,'button.btn:nth-child(1)')
WebDriverWait(driver, 10).until(
    ec.invisibility_of_element((By.CSS_SELECTOR, '.action-toast'))
)
