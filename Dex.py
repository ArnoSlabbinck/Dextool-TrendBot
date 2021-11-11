import requests
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


proxies = {
      "http": "http://3fc2340246f74c12acc93f293f1a69d7:@proxy.crawlera.com:8011/",
        "https": "http://3fc2340246f74c12acc93f293f1a69d7:@proxy.crawlera.com:8011/",
}


print("[+] Dextools Bot Starting")
options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.dextools.io/app/bsc/pair-explorer/0xfd1a80992f06bf1912024ae4415874b4e5ea00e7"
driver.get(url)
#proxies=dict(http='socks5://127.0.0.1:9150',https='socks5://127.0.0.1:9150')

print("[+] Go for settings. You have 120 seconds!!")
#time.sleep(120)
driver.implicitly_wait(30)
time.sleep(5)

def ma_ip():
    
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url, proxies=proxies, verify="./zyte-proxy-ca.crt") # You need the CA certificate to make a Secure HTTP connection
    return get_ip.text

while True:
    driver.get(url)
    print ('[+] Your IP was for this refresh : '+str(ma_ip()))
    time.sleep(5)
    button = driver.find_element_by_xpath("/html/body/app-root/div[2]/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div/div[1]/div[1]/h3/div/div[1]/a[3]").click()