import json
from selenium import webdriver
from selenium.webdriver.common.by import By

def html_to_json(file_path):
    try:
        driver = webdriver.Chrome()
        url = "https://www.nepalstock.com/today-price"
        driver.get(url)
        driver.implicitly_wait(10)

        content_divs = driver.find_elements(By.CLASS_NAME, 'table-responsive')
        extracted_data = [div.text for div in content_divs]
        driver.quit()
        data = {'extracted_data': extracted_data}
        #print(data)
        
        json_data = json.dumps(data, indent=2)

        # Save JSON to a file
        output_file_path = file_path.replace('.html', '_output.json')
        with open(output_file_path, 'w') as json_file:
            json_file.write(json_data)

        return json_data
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        driver.quit()

# Use a loop to process multiple HTML files
for i in range(1, 16):
    file_path = f'htmls_{i}.html'
    result = html_to_json(file_path)
    print(f'Processed: {file_path}')