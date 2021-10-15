# import pandas as pd
# import numpy as np
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# import time
# import plotly
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# import plotly.figure_factory as ff
# import chart_studio.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as ff

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time

chromedriver = '/Users/jordan5560/Desktop/Projects/Canada/chromedriver'

driver = webdriver.Chrome(chromedriver)
driver.get("https://ocs.ca/collections/dried-flower")

age_month = '//*[@id="dob__month"]'

age_day = '//*[@id="dob__day"]'

age_year = '//*[@id="dob__year"]'

# driver.find_element_by_xpath(age_month).send_keys(input("Enter the month of your birth date (MM):\n"))
driver.find_element_by_xpath(age_month).send_keys("12")
# driver.find_element_by_xpath(age_day).send_keys(input("Enter the day of your birth date (DD): \n"))
driver.find_element_by_xpath(age_day).send_keys("12")
# driver.find_element_by_xpath(age_year).send_keys(input("Enter the year of your birth date (YYYY): \n"))
driver.find_element_by_xpath(age_year).send_keys("1998")

driver.find_element_by_xpath('//*[@id="shopify-section-overlay"]/div/section/div/div[2]/form/p[3]/button').click()

strains = driver.find_elements_by_css_selector('#product_6536042547020--')
strain_list = []
price_list = []
gram_list = []
type_list = []
producer_list = []
brand_list = []
potency_list = []
thc_list = []
cbd_list = []
province_list = []

index = 0
while index < len(strains):
        
        try:
            driver.implicitly_wait(3)
            strains[index].click()
            # driver.find_element_by_xpath('//*[@id="product-description--4357898995532"]/div/div[2]/button[1]').click()
            # driver.find_element_by_css_selector('#product-description--5795347990348 > div > div.properties__toggles.js-properties-toggles > button.properties__show-more.js-properties-show-more.btn.btn--outline.enabled').click()

            name = driver.find_element_by_css_selector('#main > section > div.container--product > header > h1').text
            price = float(driver.find_element_by_class_name('swatch__price').text[1:])
            gram = float(driver.find_element_by_class_name('swatch__title').text[:-1])
            type = driver.find_element_by_css_selector('#main > section > div.container--product > div.row > div.product__gallery > div > ul > li:nth-child(3) > p').text
            producer = driver.find_element_by_css_selector('#product__properties-table > tbody > tr:nth-child(1) > td:nth-child(2)').text
            brand = driver.find_element_by_css_selector('#product__properties-table > tbody > tr:nth-child(2) > td:nth-child(2)').text
            potency = driver.find_element_by_css_selector('#product__properties-table > tbody > tr:nth-child(3) > td:nth-child(2)').text
            thc = driver.find_element_by_css_selector('#product__properties-table > tbody > tr:nth-child(4) > td:nth-child(2)').text
            cbd = driver.find_element_by_css_selector('#product__properties-table > tbody > tr:nth-child(5) > td:nth-child(2)').text
            province = driver.find_element_by_xpath('/html/body/div[1]/div[6]/section/section[1]/div/table/tbody/tr[8]/td[2]').text

            strain_list.append(name)
            price_list.append(price)
            gram_list.append(gram)
            type_list.append(type)
            producer_list.append(producer)
            brand_list.append(brand)
            potency_list.append(potency)
            thc_list.append(thc)
            cbd_list.append(cbd)
            province_list.append(province)

            print(str(index) + ': ' + name)

            index += 1
            driver.back()
       
        except StaleElementReferenceException as Exception:
            strains = driver.find_elements_by_css_selector('#product_2109146269516-- > div > a > div > div.product-tile__info > div')
    
driver.close()
    
df = pd.DataFrame()
df['name'] = strain_list
df['price'] = price_list
df['grams'] = gram_list
df['type'] = type_list
df['producer'] = producer_list
df['brand'] = brand_list
df['potency'] = potency_list
df['thc'] = thc_list
df['cbd'] = cbd_list
df['province'] = province_list

df.to_csv('ocs.csv')