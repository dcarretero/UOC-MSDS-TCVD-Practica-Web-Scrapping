import requests
from bs4 import BeautifulSoup

class Recipe:
    name =''
    difficulty=''
    recipeCategory = ''
    recipeCuisine = ''
    description = ''
    image = ''
    videoContentUrl = ''
    calories = ''
    totalTime = ''
    recipeYield=''
    estimatedCost=''
    ratingValue=''
    reviewCount=''
    dataPublished=''
    categoryTags= []


    def loadRecipeFromUrl(self,url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        # Se obtiene el titulo de la receta
        div_recipe = soup.find('div', id="recipe")
        self.name=div_recipe.article.section.header.h1.text.strip()

if __name__ == '__main__':
    URL = "https://www.recetasderechupete.com/todas/recetas/carnes-aves/recetas-con-pollo/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    recipes = []

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
            currentRecipe=Recipe()
            currentRecipe.loadRecipeFromUrl(recipe['href'])
            recipes.append(currentRecipe)
    #Evidencia de que se ha guardado bien
    print(recipes[0].name)
