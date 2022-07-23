# pip install selenium
# pip install requests

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import shutil
import requests

search = input("What image would you like to scrape? ")
number = input("Num of page scrolls to scrape: ")
d = input("What driver will be used? (Chrome, Edge, Firefox): ")
if d.lower() == "edge":
    driver = webdriver.Edge()
elif d.lower() == "chrome":
    driver = webdriver.Chrome()
elif d.lower() == "firefox":
    driver = webdriver.Firefox()
else:
    driver = webdriver.Edge()
print("")
sleeptime = float(input("Time to sleep in between page scrolls, decimal number 1.0-5.0. Use larger numbers for slower internet connections: "))


driver.get("https://www.google.com/search?q={0}&tbm=isch".format(search))

for i in range(1,int(number)):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(sleeptime)
    
    try:
        driver.find_element("class name","mye4qd").click()
        time.sleep(sleeptime*2)
    except Exception:
        pass


images = driver.find_elements("xpath", '//img')

cont = input("Would you like to download? [y/n] ")
if cont == "y":
    for i,j in enumerate(images):
        try:
            res = requests.get(j.get_attribute("src"),stream = True)
            if res.status_code == 200:
                with open("{0}{1}.png".format(search,i),"wb") as file:
                    shutil.copyfileobj(res.raw,file)
        except Exception:
            pass

