import requests
from bs4 import BeautifulSoup

numbers = [1361156,1355518,1361260]

url = "https://sportnet.sme.sk/futbalnet/clen/1468719/"


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
img_tag = soup.find(alt="1468719")
print(img_tag)

img_url = img_tag['src']
response = requests.get(img_url)
open('image.jpg', 'wb').write(response.content)