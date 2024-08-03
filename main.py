import requests
from bs4 import BeautifulSoup


url = 'https://www.shopsy.in/'


response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    headings = soup.h1.get_attribute_list('class')
    
    for heading in headings:
        print(headings)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

















# url = 'https://example.com'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Referer': 'https://example.com',
#     'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
# }

# cookies = {
#     'session_id': 'YOUR_SESSION_ID',
#     'auth_token': 'YOUR_AUTH_TOKEN'
# }

# response = requests.get(url, headers=headers, cookies=cookies)