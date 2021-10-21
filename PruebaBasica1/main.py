import requests
from bs4 import BeautifulSoup

class Recipe:
    name = ''
    autor = ''
    difficulty = ''
    recipeCategory = ''
    recipeCuisine = ''
    description = ''
    image = ''
    videoContentUrl = ''
    calories = ''
    totalTime = ''
    recipeYield = ''
    estimatedCost = ''
    ratingValue = ''
    reviewCount = ''
    dataPublished = ''
    categoryTags = []


    def loadRecipeFromUrl(self,url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        # Se obtiene el titulo de la receta
        div_recipe = soup.find('div', id="recipe")
        self.name=div_recipe.article.section.header.h1.text.strip()
        self.image=div_recipe.article.section.header.img.get('src')

        rdr_tags=soup.find_all('span', class_='rdr-tag')
        self.difficulty=rdr_tags[0].text
        self.totalTime=rdr_tags[1].text
        self.recipeYield=rdr_tags[2].text
        self.ratingValue=soup.find('span', 'rf_average').text
        self.reviewCount=soup.find('span', 'rf_count').text

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
            break
        break
    #Evidencia de que se ha guardado bien
    print("receta name: " + recipes[0].name)
    print("receta image: " + recipes[0].image)
    print("receta difficulty: " + recipes[0].difficulty)
    print("receta totalTime: " + recipes[0].totalTime)
    print("receta recipeYield: " + recipes[0].recipeYield)
    print("receta ratingValue: " + recipes[0].ratingValue)
