import requests
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

import random

proxies = {
      "http": "http://3fc2340246f74c12acc93f293f1a69d7:@proxy.crawlera.com:8011/",
        "https": "http://3fc2340246f74c12acc93f293f1a69d7:@proxy.crawlera.com:8011/",
}

HugoButtonsDict = {
    1:"/html/body/app-root/div[2]/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div/div[1]/div[1]/h3/div/div[1]/a[2]", 
    2: "/html/body/app-root/div[2]/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div/div[1]/div[1]/h3/div/div[1]/a[3]", 
    3: "/html/body/app-root/div[2]/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div/div[1]/div[1]/h3/div/div[1]/a[4]", 
    4: "/html/body/app-root/div[2]/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div/div[1]/div[1]/h3/div/div[1]/a[1]"
}

timeASleep = 5
print("[+] Dextools Bot Starting")
options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.dextools.io/app/bsc/pair-explorer/0xde3e9cd3d43baf931f71618d37ab0c3e8c6c44f9"
driver.get(url)
#proxies=dict(http='socks5://127.0.0.1:9150',https='socks5://127.0.0.1:9150')

print("[+] Go for settings. You have 120 seconds!!")
#time.sleep(120)
driver.implicitly_wait(30)
time.sleep(timeASleep)

def ma_ip():
    
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url, proxies=proxies, verify="./zyte-proxy-ca.crt") # You need the CA certificate to make a Secure HTTP connection
    return get_ip.text

def randomNumber(min, max): 
    return random.randint(min, max)

while True:
    driver.get(url)
    print ('[+] Your IP was for this refresh : '+str(ma_ip()))
    time.sleep(timeASleep)
    number = randomNumber(1, HugoButtonsDict.__len__())
    button = driver.find_element_by_xpath(HugoButtonsDict[number]).click()