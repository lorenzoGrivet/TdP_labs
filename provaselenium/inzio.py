import time
from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait



from selenium.webdriver.chrome.options import Options
# import os
#
# options=Options()
#
# options.add_argument("--window-size=1920,1080")
#
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.polito.it/")
#*****************************************************
#barra cerac polito: id=q3
path="C:\\Users\\lorig\\Desktop\\Python_tdp\\provaselenium\\chromedriver-win64\\chromedriver.exe"

driver = webdriver.Firefox()
driver.get("https://www.polito.it")
time.sleep(20)

# search= driver.find_element(by=By.ID,value="onetrust-accept-btn-handler") #bottone accetta cookie di firefox
# search.send_keys(Keys.RETURN)

time.sleep(10)

# el=driver.find_element(by=By.CLASS_NAME,value="biGQs _P pZUbB hmDzD") #classe indirizzo pagina trip
# print(el)
