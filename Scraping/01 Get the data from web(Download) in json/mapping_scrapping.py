from selenium import webdriver
import json
import time 

################  Ye code web sy data ko Json file me download krta hy ##################

# Web browser driver ka path set karein (Chrome ya Firefox ke liye)
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to your Chrome executable


# Web browser driver ko launch karein
driver = webdriver.Chrome(options=options)  # For Chrome  # Chrome ke liye

# Website URL
url = 'https://www.komoot.com/tour/1410921231'

# Website par navigate karein
driver.get(url)

# Wait karein taaki page load ho sake
time.sleep(5)



# JavaScript code ko execute karke data extract karein
data = driver.execute_script("return document.documentElement.outerHTML")

# JSON file mein save karein
with open('coordinates.json', 'w') as json_file:
    json.dump(data, json_file)

# Web browser driver ko band karein wait kr
driver.quit()
