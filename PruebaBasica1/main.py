import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    URL = "https://www.recetasderechupete.com/todas/recetas/carnes-aves/recetas-con-pollo/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    tag_current_page=soup.find_all('span', class_ ='page-numbers current')
    tag_next_page=soup.find_all('a', class_= 'next page-numbers')
    print(URL)
    print("numero pagina actual"+ tag_current_page[0].text.strip())
    while len(tag_next_page)>0 :
        print("url siguiente pagina" + tag_next_page[0]['href'])  # Url de pagina siguiente
        page=requests.get(tag_next_page[0]['href'])
        soup = BeautifulSoup(page.content, "html.parser")
        url_current_page=tag_next_page[0]['href']
        tag_current_page = soup.find_all('span', class_='page-numbers current')
        tag_next_page = soup.find_all('a', class_='next page-numbers')
        print("url pagina actual" + url_current_page)
        print("numero pagina actual " + tag_current_page[0].text.strip())
        tags_recipes = soup.find_all('a', class_ ='recipephoto')
        for recipe in tags_recipes:
            print("receta " + recipe['href'])
