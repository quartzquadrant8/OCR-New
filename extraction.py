import json
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time


def extract_and_group_text_by_line(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    print("Debug: Loaded JSON data")

   
    lines = {}
    for item in data:
        vertices = item['bounding_poly']
        y_min = min(vertices, key=lambda v: v['y'])['y']
        y_max = max(vertices, key=lambda v: v['y'])['y']
        y_avg = (y_min + y_max) // 2  
        description = item['description']
        
        if y_avg not in lines:
            lines[y_avg] = []
        lines[y_avg].append(description)
        print(f"Debug: Appended '{description}' to line at y_avg = {y_avg}")

   
    sorted_lines = [lines[key] for key in sorted(lines.keys())]
    
    return sorted_lines


def process_and_filter_text(lines):
    filtered_text = []
    for line in lines:
        line_text = ' '.join(line)
       
        line_text = re.sub(r'[^\w\s]', '', line_text)
        filtered_text.append(line_text)
    
    return ' '.join(filtered_text)


def perform_google_search(query):
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)  
    driver.get("https://www.google.com")
    
   
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    
    try:
      
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="g"]/div/div/a')))
        
       
        links = driver.find_elements(By.XPATH, '//div[@class="g"]/div/div/a')
        print(f"Debug: Found {len(links)} links")
        with open('links.txt', 'w') as file:
            for link in links:
                href = link.get_attribute('href')
                print(f"Debug: Writing link {href}")
                file.write(href + '\n')
    except Exception as e:
        print(f"Error while extracting links: {e}")
    finally:
        
        driver.quit()


if __name__ == "__main__":

    vision_json_path = 'vision.json'
    
 
    grouped_lines = extract_and_group_text_by_line(vision_json_path)
    print(f"Grouped Lines: {grouped_lines}") 
    processed_text = process_and_filter_text(grouped_lines)
    print(f"Processed Text: {processed_text}")
    

    perform_google_search(processed_text)
    print(f"Search results saved to links.txt")
