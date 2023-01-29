#importing the required libraries

from selenium import webdriver #pip install selenium
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome(executable_path= r'D:\\Coding\\py\\chromedriver.exe') # change path to chromedriver.exe (try to put it in the same folder as this script)

# navigate to the login page URL
driver.get("http://192.168.46.1:20097/local/auth/custom/portal.htm?portalType=portal1") # change the URL to your wifi login page
element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "accountIn"))) # change the ID to the ID of the username field


# find the username field and enter the username
username = driver.find_element(By.ID, "accountIn") # change the ID to the ID of the username field
username.send_keys('Enter Your Account Username Here') # change he username to your username


# find the password field and enter the password
password = driver.find_element(By.ID, "accountInPwd") # change the ID to the ID of the password field
password.send_keys('Enter Your Account Password Here') # change the password to your password


check = driver.find_element(By.ID, "gouxuan") # change the ID to the ID of the checkbox (if there is one)
check.click()


# find the submit button and click it
submit_button = driver.find_element(By.ID, "portalBtn") # change the ID to the ID of the submit button
submit_button.click()
