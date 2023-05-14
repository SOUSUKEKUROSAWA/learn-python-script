from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = "https://www.thesun.co.uk/sport/football/"
path = "\Program Files\chromedriver_win32"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=Service(path))

driver.get(url)

soccer_news_list = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

for a_soccer_news in soccer_news_list:
    title = a_soccer_news.find_element(by="xpath", value='./a/h3').text
    subtitle = a_soccer_news.find_element(by="xpath", value='./a/p').text
    link = a_soccer_news.find_element(by="xpath", value='./a').get_attribute('href')
