# %% [markdown]
# ## Python Google image scrapper
# Python program to get the images from the google based on the query search - 
# 
# - This program can be used to collect the `Train & Test data` for the `Neural Network`

# %%
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import base64

# %%
# Getting the chrome web driver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

searchitem = str(input("Enter the search query")).strip()
searchitem.replace(" ", "+")

driver.get(
    "https://www.google.com/search?q=" + searchitem + "&source=lnms&tbm=isch&sa=X"
)
content = driver.page_source
soup = BeautifulSoup(content)

filename_number = 0

os.chdir(os.getcwd())
os.mkdir(searchitem)
os.chdir(os.getcwd() + "/" + searchitem)

for a in soup.findAll("img", attrs={"class": "rg_i Q4LuWd"}):
    try:
        decodedImage = base64.b64decode(a.get_attribute_list(key="src")[0][23:])
        img_file = open( searchitem + str(filename_number) +".jpeg", "wb")
        img_file.write(decodedImage)
        img_file.close()
        filename_number += 1
    except:
        pass

print("Action completed.")



