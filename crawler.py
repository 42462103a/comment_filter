from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException


store_list=list(map(str,input("輸入店家名稱:").split()))
for num in range(len(store_list)): 
    store=store_list[num]

    driver=webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("https://www.google.com/maps/@23.4857501,119.4996499,7z?authuser=0&entry=ttu")
    driver.switch_to.active_element.send_keys(store)
    driver.switch_to.active_element.send_keys(Keys.RETURN)
    
    try:
        
        buttons = driver.find_elements(By.CLASS_NAME, "hh2c6")
        buttons[1].click()
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
        print("店家:",store)
        print("真實星數=",real_ratings_ave)
        print("評論真實度=",comments_long/len(ratings))
    except:
        print("Can't fihd",store)