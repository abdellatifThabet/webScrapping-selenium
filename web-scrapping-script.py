from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
url = r'https://www.tradingview.com/symbols/BTCUSD/technicals/'
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
import xlwt
from xlwt import Workbook
from time import time, sleep

def scrap_data():
    driver.get(url)
    driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/button[1]').click()
    sleep(1)
    oscilators = driver.find_elements_by_class_name("tableWrapper-2-juHm8n")

    # Workbook is created
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write_merge(0, 0, 0, 2, 'OSCILLATORS')
    sheet1.write_merge(0, 0, 3, 5, 'MOVING AVERAGES')
    sheet1.write_merge(0, 0, 6, 11, 'PIVOTS')

    ## filling the file
    sum_c = 0
    total_c = 0
    for osc in oscilators:

        rows = osc.find_elements_by_tag_name("tr")
        for i,row in enumerate(rows):

            if(i<1):
                cols = row.find_elements_by_tag_name("th")
                for c, col in enumerate(cols):

                    #print(col.text) #prints text from the element
                    sheet1.write(i+1, sum_c, col.text)
                    sum_c = sum_c+1
            elif(i>0):
                cols = row.find_elements_by_tag_name("td")
                for c, col in enumerate(cols):
                    sheet1.write(i+1, total_c+c, col.text)
                    #print(col.text) #prints text from the element
        total_c = total_c+len(cols)
        #print("*************************this is another table ***************************")
    wb.save('scrap_data.xls')
    return 

from time import time, sleep
while True:
    scrap_data()
    sleep(60 - time() % 60)