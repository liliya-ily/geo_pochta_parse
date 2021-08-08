import time
from selenium.webdriver import Chrome
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка работы selenium
chrome_options = Options()
driver = webdriver.Chrome('geo_pochta_parse\chromedriver.exe')
driver.set_window_size(1920, 1080)

# Вход на сайт и обход начального обучения 
url = "http://geo.pochta.ru/"
driver.get(url)
driver.get(url)

tutorial_xpath = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/i')))
tutorial_xpath.click()
time.sleep(5)

# Отдаление на карте
smaller__xpath = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,  '//*[@id="map-osm"]/div[2]/div[2]/div/a[2]')))
smaller__xpath.click()
time.sleep(5)
smaller__xpath.click()
time.sleep(5)

# Переключение получение данных с одной точки на контур
circuit = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,  '//*[@id="app"]/div[2]/div[1]/div[2]/div/div/div[2]/div/ul/li[3]')))
circuit.click()

# Границы проведения контуров точек
left_up = [524, 110]
right_up = [1374, 110]
left_down = [524, 910]
right_down = [1374, 910]

# Заполнение выбранной области контурами
while left_up[1] < left_down[1]:

    # левая верхняя точка
    ActionChains(driver).move_by_offset(*left_up).click().perform()

    # правая верхняя точка
    time.sleep(1)
    ActionChains(driver).reset_actions()
    ActionChains(driver).move_by_offset(*right_up).click().perform()
    right_up[1] += 20

    # правая нижняя точка
    time.sleep(1)
    ActionChains(driver).reset_actions()
    ActionChains(driver).move_by_offset(*right_up).click().perform()

    # левая нижняя точка
    time.sleep(1)
    ActionChains(driver).reset_actions()
    ActionChains(driver).move_by_offset(
        left_up[0], right_up[1]).click().perform()

    # левая верхняя точка
    time.sleep(1)
    ActionChains(driver).reset_actions()
    ActionChains(driver).move_by_offset(*left_up).click().perform()

    left_up[1] += 20
    ActionChains(driver).reset_actions()
    time.sleep(2)

# Появление скрытого окна с адресами и ящиками
hidden_address_window = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,  '//*[@id="app"]/div[2]/div[1]/div[3]/div/div/div[5]/span[2]/div/span')))
hidden_address_window.click()

# Получение и запись данных из скрытого окна 
table_xpath = '//*[@id="app"]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div/table/tbody/'
time.sleep(15)
columns = 3
rows = len(driver.find_elements_by_xpath(table_xpath + 'tr'))
# Необязательный вывод для проверки, что данные найдены
print("rows - ", rows)   

df = pd.DataFrame(columns=['street', 'house', 'amount_mailboxes'])

# Необязательная переменная для отслеживания работоспособности набора данных
i = 0

for row in range(2, rows+1):
    street = driver.find_element_by_xpath(
        table_xpath + "tr["+str(row)+"]/td[1]").text
    house = driver.find_element_by_xpath(
        table_xpath + "tr["+str(row)+"]/td[2]").text
    amount_mailboxes = driver.find_element_by_xpath(
        table_xpath + "tr["+str(row)+"]/td[3]").text
    df.loc[i] = street, house, amount_mailboxes
    i += 1
    if (i % 1000) == 0:
        print(i)

df.to_csv('test.csv', index=False)

# Закрыть окно браузера
# driver.close()
