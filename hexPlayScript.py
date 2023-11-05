import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/hex.html")#assuming the server is running at port 5500
driver.find_element(By.XPATH, "//input[@value='Blue: Player']").click()#this is used to change the mode to player v/s player, we can comment this out to play v/s AI
driver.execute_script('MakeMove(2,1,false);')#instead of 2,1 we can change the values for a specific move

time.sleep(5)
