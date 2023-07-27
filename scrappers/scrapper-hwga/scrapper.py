from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
from bs4.element import Tag
from pyvirtualdisplay import Display
import requests
from PIL import Image
import os

def work_with_path(count, ext):
    return os.path.join(os.path.dirname(__file__), f'imgs/{count}.{ext}')

def scrap_it():
    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
	# 'https://nudecosplaygirls.com/ai-art-anime-girl-7-nun-65-photos/' 
	driver.get(
            'some_hentai_stuff')

    full_html = driver.find_element(
            By.CLASS_NAME, 'g1-content-narrow').get_attribute("outerHTML")# get_attribute("src")
    
    soup = bs(full_html, 'html.parser')
    all_imgs = soup.find_all('img')
    count = 0
    for img in all_imgs:
        path_webp = work_with_path(count, 'webp')
        path_jpeg = work_with_path(count, 'jpeg')
        img = Image.open(requests.get(img['src'], stream = True).raw)
        img.save(path_webp)
        img_jpeg = Image.open(path_webp).convert('RGB').save(path_jpeg)
        print(count, path_webp, path_jpeg)
        os.remove(path_webp)
        count+=1


scrap_it()
