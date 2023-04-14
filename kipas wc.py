from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

banner()
InputData()
# Inisialisasi ChromeDriver
driver = webdriver.Chrome()
# Membuka situs web
driver.get("https://shopee.co.id/")

# Mendapatkan cookie yang ada
cookies = driver.get_cookies()

# Menyimpan cookie dalam variabel dictionary
cookies_dict = {}
for cookie in cookies:
    cookies_dict[cookie['name']] = cookie['value']

# Menambahkan cookie manual
new_cookie = {'name': '_gcl_au', 'value': '1.1.1434682209.1681248787', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_fbp', 'value': 'fb.2.1681248787783.1901678351', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_SI', 'value': 'HgM1ZAAAAABKUmVLU3M2MB6CDAAAAAAATHFBMTJlcDc=', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_tt_enable_cookie', 'value': '1', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_ttp', 'value': '3K0Vs7TjrH5GfmCnwRJsU2ltIPh', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'REC_T_ID', 'value': '73f242e6-d8b0-11ed-9a36-f4ee08261bbd', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_F', 'value': 'T7XNqbwPFiINY1yLoSXvW5SHRj5TkHqc', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_gid', 'value': 'GA1.3.461654168.1681248789', 'domain': '.shopee.co.id'}
new_cookie = {'name': '__LOCALE__null', 'value': 'ID', 'domain': 'shopee.co.id'}
new_cookie = {'name': '_med', 'value': 'cpc', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'csrftoken', 'value': 'TJw9dJKcMrY1ytmZWmS04fBfJMfDu8Xe', 'domain': 'shopee.co.id'}
new_cookie = {'name': '_QPWSDCXHZQA', 'value': 'd23c8ade-5683-4b93-dc10-b109ca3b55e6', 'domain': 'shopee.co.id'}
new_cookie = {'name': 'AMP_TOKEN', 'value': '%24NOT_FOUND', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_ST', 'value': '.amV4NU5JTzE2TWtqTW80QU17BrZxPBCJhOhy50tgfurLohwJIve5Q2/qMJGJvczEJT4Tc1uL+VCORjOe0FJGoAvFx6DtPdIfUeasSCln3GprZD208ON/UmE8L0h/8HOROSZZmOJNdZEoC0M1fdxkOEOK4tm083UBywWBKA2eDKRPg+L3e3b5QRZkGJKduhsDxz7G2c/ameltqIj2B1Qwng==', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_CLIENTID', 'value': 'VDdYTnFid1BGaUlOcasgvzxyartjraoj', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_gcl_aw', 'value': 'GCL.1681321075.CjwKCAjwrdmhBhBBEiwA4Hx5g1TcFiOe_z8rkspMaGduFZ2fdlJCfMGWvEbOIu9x8CfDm5MNZDQK-RoCy0oQAvD_BwE', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_U', 'value': '338487471', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_R_T_ID', 'value': 'DE9nlKletw7rforjArxGxsg5WKfW69cPs8c1K7HL2sLTQS1OFf20bCqIOX9IThHI5+FSeFWJaKMNWLMVNIVbSTQQn7UeNYF4LbeIl1g5dl1SJ6ptjbjEv62G8Dpby+xaRdgzoR65iG2Vizp9ZNUn3iCqQPcevC6bDwOyLWdhlOI=', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_R_T_IV', 'value': 'SFViTVVWR0lSVVk2VEFxcw==', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_T_ID', 'value': 'DE9nlKletw7rforjArxGxsg5WKfW69cPs8c1K7HL2sLTQS1OFf20bCqIOX9IThHI5+FSeFWJaKMNWLMVNIVbSTQQn7UeNYF4LbeIl1g5dl1SJ6ptjbjEv62G8Dpby+xaRdgzoR65iG2Vizp9ZNUn3iCqQPcevC6bDwOyLWdhlOI=', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_T_IV', 'value': 'SFViTVVWR0lSVVk2VEFxcw==', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_gac_UA-61904553-8', 'value': '1.1681321076.CjwKCAjwrdmhBhBBEiwA4Hx5g1TcFiOe_z8rkspMaGduFZ2fdlJCfMGWvEbOIu9x8CfDm5MNZDQK-RoCy0oQAvD_BwE', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_ga_SW6D8G0HXK', 'value': 'GS1.1.1681321022.3.1.1681321076.6.0.0', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_ga', 'value': 'GA1.1.1024733529.1681248789', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_IA', 'value': '1', 'domain': 'shopee.co.id'}
new_cookie = {'name': 'shopee_webUnique_ccd', 'value': 'Ju2bPW25OdHYOps4r6x9Vw%3D%3D%7CMS0MmzWxMqESlidMUvMnRkI%2BvBev1vnBEV9GkaarIfeL5eUaiIJWx0ewn1kg7WVLxpvBLGLCHlmCwpec6OISjO4Hkz%2F7oTH6NA%3D%3D%7CJA%2FNZZYBGmV3zfNO%7C06%7C3', 'domain': 'shopee.co.id'}
new_cookie = {'name': 'ds', 'value': 'b92ec114574b9d2925cbe415900af0a0', 'domain': 'shopee.co.id'}
new_cookie = {'name': '_dc_gtm_UA-61904553-8', 'value': '1', 'domain': '.shopee.co.id'}
new_cookie = {'name': '_gali', 'value': 'main', 'domain': '.shopee.co.id'}
new_cookie = {'name': 'SPC_EC', 'value': 'cjFta2RId2VySlBMRWdPdWuHxEh+3qmo3npWJAQLTF2Im+0fkL0hImrg0nT0RbRzs9gGTsA/j+K+oXFKAqoUWUiGBwia485JsAKNOPsV4t6iOevD1MxkHNh/sV2F+Dc73tB8siFR91qzYO9xaU3kYJTscdiUDUSmXEdUtUxMKKQ=', 'domain': '.shopee.co.id'}

driver.add_cookie(new_cookie)

driver.refresh()

driver.get(link_produk)

selisih = time_target-datetime.datetime.now()
print('(#) Harap Menunggu... ')
time.sleep(selisih.seconds)
driver.refresh()
print('(#) Browser Refresh... ')

def click(driiver,element_css):
    WebDriverWait(driver, 20).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, element_css))
    )
    WebDriverWait(driver, 20).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, element_css))
    )
    driver.find_element_by_css_selector(element_css).click()

click(driver, 'button.product-variation:nth-child(1)')

click(driver,'button.btn--l:nth-child(2)')
WebDriverWait(driver, 20).until(
    ec.invisibility_of_element((By.CSS_SELECTOR, '.action-toast'))
)
