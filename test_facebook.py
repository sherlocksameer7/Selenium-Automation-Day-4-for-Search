from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test Started Successfully")

driver.maximize_window()

driver.get("https://www.facebook.com/")
driver.find_element_by_name("email").send_keys("arijitsameers@gmail.com")
time.sleep(3)
driver.find_element_by_name("pass").send_keys("sammu007")
time.sleep(5)

driver.find_element_by_name("login").send_keys(Keys.ENTER)
time.sleep(10)

driver.close()
print("Test Completed")

