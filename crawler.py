from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time


store=input("The name of the store")

driver=webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://www.google.com/maps/@23.4857501,119.4996499,7z?authuser=0&entry=ttu")
driver.switch_to.active_element.send_keys(store)
driver.switch_to.active_element.send_keys(Keys.RETURN)
buttons = driver.find_elements(By.CLASS_NAME, "hh2c6")

buttons[1].click()


# driver=webdriver.Chrome()
# driver.get("https://www.google.com/maps/place/%E9%BA%B5%E5%BF%83%E7%84%A1%E7%95%8C(%E7%87%9F%E6%A5%AD%E6%99%82%E9%96%93%E4%BB%A5Google%E5%9C%B0%E5%9C%96%E7%82%BA%E6%BA%96%2F%E4%BE%86%E5%BA%97%E5%89%8D%E8%AB%8B%E5%85%88%E7%9C%8B%E7%B2%89%E5%B0%88%E7%BD%AE%E9%A0%82%E5%85%AC%E5%91%8A)/@24.953707,121.237616,17z/data=!4m8!3m7!1s0x346823e8a8b1c50d:0x5c91bf4a87dbe0d1!8m2!3d24.953707!4d121.2401909!9m1!1b1!16s%2Fg%2F11j86jxrbk?entry=ttu")
driver.implicitly_wait(2)
scroll = driver.find_element(By.CLASS_NAME,"m6QErb.DxyBCb.kA9KIf.dS8AEf")
last_scroll_height = 0

while True:
  
    scroll_height = driver.execute_script("return arguments[0].scrollHeight", scroll)
    
    
    if scroll_height == last_scroll_height:
        break
    

    driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight)", scroll)
    
    
    last_scroll_height = scroll_height
    
    
    time.sleep(0.7)

time.sleep(5)
buttons=driver.find_elements(By.CLASS_NAME,"w8nwRe.kyuRq")
for button in buttons:
    button.click()
try:
    comments= driver.find_elements(By.CSS_SELECTOR, "div[class=\"MyEned\"] span[class=\"wiI7pd\"]")
   
except:
    comments=[]

comments=[comment.text for comment in comments]


stars= driver.find_elements(By.CLASS_NAME,"kvMYJc")

ratings=[int(star.get_attribute("aria-label")[0]) for star in stars]
real_ratings=0
for i in range(0,len(comments)):
    real_ratings+=ratings[i]
real_ratings_ave=real_ratings/len(comments)
h=len(ratings)-len(comments)
comments_long=len(comments)

for i in range(h):
    comments.append("")

comments = pd.Series(comments)
stars=pd.Series(stars)
combine=pd.DataFrame({"comments":comments,"ratings":ratings})
combine.to_csv("google_comments.tsv",sep="\t",index=False)
print("真實星數=",real_ratings_ave)
print("評論真實度=",comments_long/len(ratings))