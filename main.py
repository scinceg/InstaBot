from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from data import username, password
import time
import random
from selenium.webdriver.common.by import By

def hashtag_search(username, password, hashtag):
    browser = webdriver.Chrome('Part 2\chromedriver\chromedriver.exe')

    browser.get('https://www.instagram.com')
    time.sleep(2)
    try: 
        username_input = browser.find_element('name', 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element('name', 'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(5)

            for i in range(1):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(3, 5))

            hrefs = browser.find_elements(By.TAG_NAME, 'a')
            print(hrefs)
            
            posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]

            for url in posts_urls:
                time.sleep(3)
                try:
                    browser.get(url)
                except Exception as ex:
                    print(ex)

            browser.close()
            browser.quit()


        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


hashtag_search(username, password, 'basketball')