from selenium import webdriver
import sys
import psutil
import getpass
import os
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
def main():
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


	driver.add_cookie(new_cookie)

	# Memuat ulang halaman untuk menerapkan cookie baru
	driver.refresh()

	# Verifikasi login otomatis dengan memeriksa konten halaman
	if "Selamat datang" in driver.page_source:
	    print("Login otomatis berhasil!")
	else:
	    print("Login otomatis gagal.")
main()
