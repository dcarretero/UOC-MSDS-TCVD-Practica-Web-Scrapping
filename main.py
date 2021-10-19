import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    URL = "https://www.recetasderechupete.com/todas/recetas/carnes-aves/recetas-con-pollo/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")


