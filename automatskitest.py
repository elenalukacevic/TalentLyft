import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Konfiguracija drivera (Chrome)
driver = webdriver.Chrome()
driver.get("https://dailytodo.org/vcSZc?edit=1")  # Otvaranje stranice

# Pronalaženje elementa za unos teksta
text_input = driver.find_element("name", "tasks")

# Unos zadataka
for i in range(1,175,1):
    text_input.send_keys(str(i))
    text_input.send_keys("\n")
    

# Odabir opcije Sav Tasks
button = driver.find_element(By.XPATH, '//input[@type="submit" and @class="big" and @value="Save tasks"]')
button.click()
# Pauza u slučaju da se sporije odvijao unos zadataka
time.sleep(2)

# Zatvaranje aplikacije
#driver.quit()
