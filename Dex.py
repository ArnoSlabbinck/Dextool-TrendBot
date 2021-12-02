from typing import List, cast
import requests
from requests.sessions import _ParamsMappingKeyType
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading
import random
import json
from web3 import Web3

proxies = {
      "http": "http://3fc2340246f74c12acc93f293f1a69d7:@proxy.crawlera.com:8011/",
        "https": "http://3fc2340246f74c12acc93f293f1a69d7:@proxy.crawlera.com:8011/",
}

#Xpaths for the links
HugoButtonsDict = {
    1:"/html/body/app-root/div[2]/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div/div[1]/div[1]/h3/div/div[1]/a[2]", 
    2: "/html/body/app-root/div[2]/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div/div[1]/div[1]/h3/div/div[1]/a[3]", 
    3: "/html/body/app-root/div[2]/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div/div[1]/div[1]/h3/div/div[1]/a[4]", 
    4: "/html/body/app-root/div[2]/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div/div[1]/div[1]/h3/div/div[1]/a[1]"
}



cryptos = []
timeStopProgram = 60 * 60 * 24
timeToWait = 60 * 10
timeRunningProgram = 0
timeASleep = 45
print("[+] Dextools Bot Starting")
Metamask = "/html/body/app-root/div[2]/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div/div[2]/div[2]/div/app-aggregator/section/div/div/div/div/div/div/div/div[4]/button"
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

def findAllCryptosInBanner(substring): 
    banner4 = driver.find_elements_by_class_name('ng-star-inserted')
    counter = 0
    try: 
       for items in banner4: 
        if substring in items.text: 
            print('Found')
            print('Hugo finance on place: {0}'.format(counter))
            print(items.size)
        counter += 1
    except: 
        print("An exception occured")

   


#Programma naar een Daemon zetten

def checkTimeProgram(RunTime): 
    if(RunTime >= timeStopProgram): 
        return False
    else: 
        return True

def ma_ip():
    
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url, proxies=proxies, verify="./zyte-proxy-ca.crt") # You need the CA certificate to make a Secure HTTP connection
    return get_ip.text

def randomNumber(min, max): 
    return random.randint(min, max)


def checktop10spot(): 
    return 0

def main(RunTime): 
    while (checkTimeProgram(RunTime)):
        time.sleep(timeASleep)
        driver.get(url)
        print ('[+] Your IP was for this refresh : '+str(ma_ip()))
        connectToMetamask()
        #findAllCryptosInBanner('Hugo Finance')
        RunTime += timeToWait
        number = randomNumber(1, HugoButtonsDict.__len__())
        driver.find_element_by_xpath(HugoButtonsDict[number]).click()

def SetUpWeb3Client(url, address): 
        web3 = Web3(Web3.HTTPProvider(url))

def connectToMetamask(): 
    buyButton = "/html/body/app-root/div[2]/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div/div[2]/div[2]/ul/li[1]/span/button"
    buy = driver.find_element_by_xpath(buyButton)
    buy.click()
    print(buyButton)
    time.sleep(5)
 
if __name__ == "__main__": 
    main(timeRunningProgram)


