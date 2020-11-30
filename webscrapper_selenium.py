from selenium import webdriver

url = 'https://www.youtube.com/c/SsethTzeentach/videos'
browser = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')
browser.get(url)

browser.find_element_by_xpath('//*[@id="thumbnail"]').click()
