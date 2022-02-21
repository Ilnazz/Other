from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

def document_initialised(driver):
    return driver.execute_script("return document.readyState")

driver = webdriver.Edge('msedgedriver.exe')

WebDriverWait(driver, timeout=10).until(document_initialised)

driver.get('https://skillbox.ru/courses/?type=course')

load_more_button = driver.find_elements(By.CSS_SELECTOR, '.courses-block__load')[0]
while len(load_more_button) != 0:
	sleep(0.25)
	# add: check for element is not none
	load_more_button[0].click()


courses = driver.find_elements(By.CSS_SELECTOR, '.card--course')
for course in courses:
	course_title = course.find_elements(By.CSS_SELECTOR, '.card__title')[0].text
	course_duration = course.find_elements(By.CSS_SELECTOR, '.card__count')[0].text
	print(course_title, course_duration)


#driver.quit()