from datetime import date
from setup import prepareBrowser
from csv_writer import csv_WriteRowData
from selenium.webdriver.common.by import By

browser = prepareBrowser()
title_price_list = []
resultIndexList = []
results = []
searchAgent = None
today = date.today()
source = 'Amazon'

def changePageUrl(pageNumber):
    return f'https://www.amazon.com/s?k=iphone+11&page={pageNumber}&crid=19QVE3PB66B8U&qid=1662432049&sprefix=iphone11%2Caps%2C417&ref=sr_pg_{pageNumber}'

def generateResultsIndex():
    for number in range(2, 17):
        formatNumber = str(number)
        resultIndexList.append(
            f'//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[{formatNumber}]')
   
generateResultsIndex()

def generateResults():
    global searchAgent
    for index in resultIndexList:
        if(searchAgent):
            data = searchAgent.find_element(By.XPATH, index)
            results.append(data)

def fotmatResults():
    global title_price_list
    for result in results:
        try:       
            listItem = {}
            name = result.find_element(
                By.CSS_SELECTOR, '.sg-col-inner .a-section  .sg-row .sg-col-inner h2 a span').text
            listItem["Product Name"] = name
            price = result.find_element(
                By.CSS_SELECTOR, '.sg-col-inner .a-section  .sg-row .sg-col-inner .sg-row .sg-col-inner a span span:nth-child(2) .a-price-whole').text
            listItem["Product Price"] = price
            listItem["Date"] = today
            listItem["Source"] = source
            title_price_list.append(listItem)
        except:
            print("An exception occurred")

def generateData(page):
    global searchAgent
    global results
    url = changePageUrl(page)
    browser.get(url)
    searchAgent = browser.find_element(
        By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]')
    generateResults()
    fotmatResults()
    results = []

counter = 1
while counter < 4:
    generateData(str(counter))
    counter += 1
print('Total rows: ',len(title_price_list)) # Print total rows 
browser.quit()

# Write data to csv
file='sample.csv' # Fill in filename
collums = ['Product Name', 'Product Price', 'Date', 'Source'] # Fill in collum 
csv_WriteRowData(file,collums,title_price_list)

