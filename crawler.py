from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

import time


driver=webdriver.Chrome()
driver.get("https://www.google.com/maps/place/Match19-%E6%95%B8%E4%BD%8D%E7%A7%91%E6%8A%80%E9%A1%A7%E5%95%8F%E5%85%AC%E5%8F%B8%EF%BD%9C%E7%B6%B2%E9%A0%81%E8%A8%AD%E8%A8%88+%E5%AE%A2%E8%A3%BD%E5%8C%96%E7%B6%B2%E7%AB%99+%E8%B3%BC%E7%89%A9%E8%BB%8A%E7%B6%B2%E7%AB%99+%E8%BB%9F%E9%AB%94%E9%96%8B%E7%99%BC+%E5%A4%96%E6%8E%9B%E7%A8%8B%E5%BC%8F%E7%B7%A8%E5%AF%AB/@23.4634915,116.8579793,7z/data=!4m8!3m7!1s0x3442a94953346643:0xd666490eefdd8483!8m2!3d23.4857501!4d119.49965!9m1!1b1!16s%2Fg%2F11qr9fs7dt?entry=ttu")

driver.implicitly_wait(2)
scroll = driver.find_element(By.CLASS_NAME,"m6QErb.DxyBCb.kA9KIf.dS8AEf")

for i in range(1,11):
    val=i*2000
    driver.execute_script("arguments[0].scrollTop=" + str(val), scroll)
    time.sleep(1)
    top=scroll.get_attribute("scrollTop")

buttons=driver.find_elements(By.CLASS_NAME,"w8nwRe.kyuRq")
for button in buttons:
    button.click()

# all=driver.find_elements(By.CSS_SELECTOR,"div[class=\"GHT2ce\"]")

# comments = []
# ratings = []

# for i in all:
#     try:
#         star= i.find_element(By.CSS_SELECTOR, "span[class=\"kvMYJc\"]")
#         star=int(star.get_attribute("aria-label")[0]) 
#     except NoSuchElementException:
#         continue

#     try:
#         comment= i.find_element(By.CSS_SELECTOR, "div[class=\"MyEned\"] span[class=\"wiI7pd\"]").text
#     except NoSuchElementException:
#         comment=""

#     comments.append(comment)
#     ratings.append(star)
#     print(comment)
#     print(star)

# combine=pd.DataFrame({"comments":comments,"ratings":ratings})
# combine.to_csv("google_comments.tsv",sep="\t",index=False)



try:
    comments= driver.find_elements(By.CSS_SELECTOR, "div[class=\"MyEned\"] span[class=\"wiI7pd\"]")
   
except:
    comments=[]

comments=[comment.text for comment in comments]


stars= driver.find_elements(By.CLASS_NAME,"kvMYJc")

ratings=[int(star.get_attribute("aria-label")[0]) for star in stars]

h=len(ratings)-len(comments)
for i in range(h):
    comments.append("")
print(len(comments))
print(len(ratings))
comments = pd.Series(comments)
stars=pd.Series(stars)
combine=pd.DataFrame({"comments":comments,"ratings":ratings})
combine.to_csv("google_comments.tsv",sep="\t",index=False)