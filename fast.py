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
options = Options()
options.add_argument('--headless')  # Menambahkan argument --headless
driver = webdriver.Chrome(chrome_options=options)
# Tanpa menampilkan antarmuka grafis
driver.get('https://shopee.co.id/')

# Mendapatkan cookie yang ada
cookies = driver.get_cookies()

# Menyimpan cookie dalam variabel dictionary
cookies_dict = {}
for cookie in cookies:
    cookies_dict[cookie['name']] = cookie['value']

# Menambahkan cookie manual
new_cookie = {'name': '_gcl_au', 'value': '1.1.1434682209.1681248787', 'domain': '.shopee.co.id'}
#cookie ++++++++++++ haris diganti
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
