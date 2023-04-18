from selenium import webdriver
import time
import openpyxl

# Open the Excel file and get the data
workbook = openpyxl.load_workbook('example.xlsx')
sheet = workbook.active
data = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    data.append(row[0])

# Start a new instance of the Firefox browser
browser = webdriver.Firefox()

# Navigate to the website
browser.get('https://www.example.com')

# Wait for the page to load
time.sleep(5)

# Find the search box and enter the first record from the Excel file
search_box = browser.find_element_by_name('q')
search_box.send_keys(data[0])

# Click the search button
search_button = browser.find_element_by_name('btnK')
search_button.click()

# Wait for the search results to load
time.sleep(5)

# Print the title of the first search result
first_result = browser.find_element_by_css_selector('h3.r a')
print(first_result.text)

# Close the browser
browser.quit()
