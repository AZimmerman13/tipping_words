import requests
from bs4 import BeautifulSoup

result = requests.get("https://tippingpitchespod.wordpress.com/blog/")
src = result.content
soup = BeautifulSoup(src, 'lxml')