from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load environment variables from .env file
load_dotenv()
# Access the variables

os.getenv('PASSWORD')

# Specify the path to your ChromeDriver
service = Service('/Users/hyunjoon/Downloads/chromedriver')

# Initialize WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# Open Baekjoon Online Judge login page
driver.get('https://www.acmicpc.net/login')

# Log in to your account (replace 'your_username' and 'your_password')
username_input = driver.find_element(By.NAME, 'login_user_id')
password_input = driver.find_element(By.NAME, 'login_password')

username_input.send_keys(os.getenv('USERNAME'))
password_input.send_keys(os.getenv('PASSWORD'))

password_input.send_keys(Keys.RETURN)

# Wait for login to complete
time.sleep(3)

# Navigate to the specific workbook page
workbook_url = 'https://www.acmicpc.net/group/workbook/edit/21964/73393'
driver.get(workbook_url)

# text path
text = 'problems/dfs.txt'

# Read numbers from file and submit each one
with open(text, 'r') as file:
    for line in file:
        number = line.strip()
        
        # Find the input field for problem number
        problem_input = driver.find_element(By.NAME, 'problem')
        
        # Enter the number and press Enter
        problem_input.clear()
        problem_input.send_keys(number)
        problem_input.send_keys(Keys.RETURN)
        
        # Wait between submissions if necessary
        time.sleep(1)

time.sleep(2)

try:
    # Wait for the button to be clickable and then click it
    modify_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary' and text()='수정하기']"))
    )
    modify_button.click()
    print("Clicked the '수정하기' button successfully.")
except Exception as e:
    print(f"Failed to click the '수정하기' button: {e}")

# Close the browser after completion
driver.quit()