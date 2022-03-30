from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Testcase Started")

driver.maximize_window()

driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("Iphone 13")
time.sleep(1)
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(3)
driver.find_element_by_partial_link_text("1,19,900").click()
time.sleep(7)

driver.close()
print("Testcase Completed")