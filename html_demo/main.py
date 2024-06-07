import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.amazon.in/s?k=mobile+phone&sprefix=mob%2Caps%2C890&ref=nb_sb_ss_softlines-tsdoa-joint-contextual-")
webpage = response.text

soup = BeautifulSoup(webpage,'html.parser')
print(soup.find(name="a",class_="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"))
