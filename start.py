from selenium.webdriver import Chrome
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options()
driver = webdriver.Chrome('D:\Dev\selenium\chromedriver.exe')
import time
import logging
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


url = "http://geo.pochta.ru/"
driver.get(url)
driver.get(url)
time.sleep(10)
tutorial_xpath = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/i')
tutorial_xpath.click()
time.sleep(5)
one_xpath = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li[1]')
one_xpath.click()

# actions = ActionChains(driver)
# actions.move_by_offset(300, 150).perform()
# time.sleep(5)
# actions.click().perform()

# actions.move_by_offset(220, 110).perform()
# time.sleep(5)
# actions.click().perform()
ActionChains(driver).move_by_offset(700, 200).click().perform()
for i in range(10, 90, 10):
    ActionChains(driver).move_by_offset(10, i).click().perform()
    # ActionChains(driver).reset_actions()
    time.sleep(5)
time.sleep(10)
take_hidden_window = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[3]/div/div/div[5]/span[2]/div/span')
take_hidden_window.click()

total = []

quote_text = driver.find_elements_by_class_name('element-addresses')
print('тут работает element')
print(quote_text)
quote_text = driver.find_elements_by_class_name('unselectable')
print('тут работает unselectable')
print(quote_text)

for quote in quote_text:
        # quote_text = quote.find_element_by_class_name('column-1 column-row-header ng-binding')
        print(quote)
        # total.append(quote_text)

# driver.close()
df = pd.DataFrame(total,columns=['quote'])
df.to_csv('quoted.csv')
# pages = 11


# for page in range(1,pages):
    
#     url = "http://quotes.toscrape.com/js/page/" + str(page) + "/"

#     driver.get(url)
    
#     quotes = driver.find_elements_by_class_name("quote")
#     for quote in quotes:
#         quote_text = quote.find_element_by_class_name('text').text[1:-2]
#         author = quote.find_element_by_class_name('author').text
#         new = ((quote_text,author))
#         total.append(new)

# driver.close()
# df = pd.DataFrame(total,columns=['quote','author'])
# df.to_csv('quoted.csv')