from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

script_path = os.path.dirname(sys.executable)

today = datetime.now().strftime("%m%d%Y") # MMDDYYYY

url = "https://www.thesun.co.uk/sport/football/"
executable_path = "\Program Files\chromedriver_win32"

# headless-mode
options = Options()
options.headless = True

service = Service(executable_path=executable_path)

class WebDriverContext:
    def __init__(self, service, options):
        self.service = service
        self.options = options

    def __enter__(self):
        self.driver = webdriver.Chrome(service=self.service, options=options)
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()

with WebDriverContext(service, options) as driver:
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

    output_file_name = f'headline-{today}.csv'
    output_file_path = os.path.join(script_path, output_file_name)

    df_headlines.to_csv(output_file_path)
