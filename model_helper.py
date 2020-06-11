from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

def checkprice(link,type):

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    web = webdriver.Chrome(options=options)
    wait = WebDriverWait(web,10)

    if(type=="Flipkart"):
        print(link)
        web.get(link)
        time.sleep(3)
        a = web.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]").text
        a = str(a)[1:]
    else:
        print(link)
        web.get(link)
        time.sleep(3)
        a = web.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[5]/div[4]/div[9]/div[1]/div/table/tbody/tr[2]/td[2]/span[1]").text
        a = str(a)[2:]

    web.close()
    return a
