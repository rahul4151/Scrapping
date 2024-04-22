from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By

district_name  = input("Enter District Name : ")
mandal_name  = input("Enter Mandal Name : ")
village_name  = input("Enter Village Name : ")

driver = webdriver.Chrome()
driver.get("https://dharani.telangana.gov.in/knowLandStatus")
time.sleep(5)

# district_name = "Adilabad|ఆదిలాబాద్"

district_dropdown = Select(driver.find_element(By.ID,'districtID'))  	
district_dropdown.select_by_visible_text(district_name)

time.sleep(5)

# mandal_name = "Adilabad (Rural)|ఆదిలాబాద్ (రూరల్)"

mandal_dropdown = Select(driver.find_element(By.ID,'mandalID'))  	
mandal_dropdown.select_by_visible_text(mandal_name)

time.sleep(5)

# village_name = "Ankapoor|అంకాపూర్"
village_dropdown = Select(driver.find_element(By.ID,'villageId'))  	
village_dropdown.select_by_visible_text(village_name)

time.sleep(5)

survey_dropdown = Select(driver.find_element(By.ID,'surveyIdselect'))
survey_options = [option.text for option in survey_dropdown.options]
driver.quit()
print(survey_options)

