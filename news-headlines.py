from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

url = "https://www.thesun.co.uk/sport/football/"
path = "\Program Files\chromedriver_win32"

service = Service(executable_path=path)

class WebDriverContext:
    def __init__(self, service):
        self.service = service

    def __enter__(self):
        self.driver = webdriver.Chrome(service=self.service)
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()

with WebDriverContext(service) as driver:
    driver.get(url)

    soccer_news_containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

    titles = []
    subtitles = []
    links = []

    for soccer_news_container in soccer_news_containers:
        title = soccer_news_container.find_element(by="xpath", value='./a/h3').text
        subtitle = soccer_news_container.find_element(by="xpath", value='./a/p').text
        link = soccer_news_container.find_element(by="xpath", value='./a').get_attribute('href')

        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)

    soccer_news = {
        'title': titles,
        'subtitle': subtitles,
        'link': links,
    }

    df_headlines = pd.DataFrame(soccer_news)

    df_headlines.to_csv('headline.csv')
