from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "https://rozetka.com.ua/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)


search_string = browser.find_element(By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/div/div/input')
search_string.send_keys("Смартфоны")
button = browser.find_element(By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/button').click()
test = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/div/div/rz-category/div/main/div[1]/div/h1'))).text
test1 = "Смартфоны"

assert test == test1, f"Тест не пройден, вот что получилось - {test}"

browser.quit()