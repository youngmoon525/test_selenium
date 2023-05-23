from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
# pip installs --> setting


    time.sleep(2)
    query="광주"
    target_blog_link="https://blog.naver.com/bin4930e/223034348501"
    querys[] = ["", ""]
for query , target_blog_link in zip (querys , target_blog_links ):
    search_link=f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}"
    driver.get(search_link)
    time.sleep(2)

    link_selector = f'a[href^="{target_blog_link}"]'
    element_target = driver.find_element(By.CSS_SELECTOR , link_selector)
    isBlog = False 
    for _ in range(7):
        try:
            while True:
                temp_element = element_target.find_element(By.XPATH , "./..")
                now_element = temp_element.get_attribute("data-cr-rank")
                if now_element != None:
                        print("찾음 : " , now_element)
                        isBlog = True
                        break
                print("몾찾?")
                element_target = temp_element
                if isBlog:
                    False
        except:
            print("타겟 못찾음 에러발생")
            driver.excute_script("window.scrollBy(0,10000);")
            time.sleep(3)
    print(f"{query} : 타겟 블로그의 랭크를 찾음")
input()


