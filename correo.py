import requests
from bs4 import BeautifulSoup, Comment
import re

url = "http://127.0.0.1:8000/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#Sacar correos electrónicos
patron1 = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'
emails = re.findall(patron1, response.text)
for email in emails:
    print(email)

#Sacar comentarios
"""
patron2 = r'<!--(.*?)-->'
comentarios = re.findall(patron2, response.text)

comentarios = soup.find_all('--')
for comentario in comentarios:
    print(comentario.get('href'))
"""

comentarios = soup.find_all(string=lambda text: isinstance(text, Comment))
for comentario in comentarios:
    print(comentario.strip())
