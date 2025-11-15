from bs4 import BeautifulSoup

import requests 
import re # Import the regular expression module
url= "https://shakhawatsabbir.com/"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
text_content = soup.get_text()

#print("Extracted Raw Text:")
#print(text_content)

# Refined email pattern to account for potential spaces around the '@' symbol
email_pattern = r'[a-zA-Z0-9._%+-]+\s?@\s?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Refined phone pattern to specifically target the format seen in the HTML content, including +880 prefix and 5-digit groups
phone_pattern = r'\+880\s?\d{5}[-.\s]?\d{5}'

found_emails = re.findall(email_pattern, text_content)
found_phone_numbers = re.findall(phone_pattern, text_content)

print("\nExtracted Emails:", found_emails)
print("Extracted Phone Numbers:", found_phone_numbers)