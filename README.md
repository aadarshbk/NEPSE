# HTML to JSON Converter

This Python script utilizes Selenium to extract data from HTML files and convert it into JSON format. The script is specifically designed for processing HTML files from the Nepal Stock Exchange website.

## Requirements

- Python 3
- Selenium
- Chrome WebDriver (for Selenium)

## Setup

1. Install Python 3: [Python Downloads](https://www.python.org/downloads/)
2. Install Selenium: `pip install selenium`
3. Download Chrome WebDriver: [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

## Usage

1. Place your HTML files in the same directory as the script.
2. Run the script using the command: `python script_name.py`

## Script Details

- The script uses Selenium to scrape data from the Nepal Stock Exchange website.
- It iterates through HTML files (assumed to be named 'htmls_1.html' to 'htmls_15.html') and converts each file's data to JSON.
- The resulting JSON files are saved in the same directory with the suffix '_output.json'.

## Example

```bash
python script_name.py
