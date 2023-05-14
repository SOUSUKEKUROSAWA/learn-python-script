from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = "\Program Files\chromedriver_win32"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=Service(path))

driver.get(website)
