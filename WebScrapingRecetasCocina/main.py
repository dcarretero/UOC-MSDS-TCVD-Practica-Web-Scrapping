import requests
import os
import csv
from bs4 import BeautifulSoup

def extract_csv(recipes):
    ruta = os.path.dirname(os.path.abspath(__file__)) + "\\datasets\\recetasDataset.csv"
    with open(ruta,'w', newline='') as file:
        writer = csv.writer(file,delimiter=";")
        writer.writerow(["url","name","author","difficulty","image","videoContentUrl",
                         "calories","totalTime","recipeYield","estimatedCost","ratingValue","reviewCount",
                         "ingredients","categoryTags"])
        for recipe in recipes:
            writer.writerow([recipe.url,recipe.name,recipe.author,recipe.difficulty,
                             recipe.image,recipe.videoContentUrl,recipe.calories,recipe.totalTime,
                             recipe.recipeYield,recipe.estimatedCost,recipe.ratingValue,
                             recipe.reviewCount, recipe.ingredients,recipe.categoryTags])

def load_requests(source_url):
    r = requests.get(source_url, stream = True)
    if r.status_code == 200:
        aSplit = source_url.split('/')
        ruta = os.path.dirname(os.path.abspath(__file__))+"\\Images\\" + aSplit[len(aSplit) - 1]
        print(ruta)
        output = open(ruta,"wb")
        for chunk in r:
            output.write(chunk)
        output.close()

class Recipe:
    url = ''
    name = ''
    author = ''
    difficulty = ''
    ingredients = []
    image = ''
    videoContentUrl = ''
    calories = ''
    totalTime = ''
    recipeYield = ''
    estimatedCost = ''
    ratingValue = ''
    reviewCount = ''
    categoryTags = []

    

    def loadRecipeFromUrl(self,url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        # Se obtiene el titulo de la receta
        div_recipe = soup.find('div', id="recipe")
        ingredients = div_recipe.find(id="ingredients").find('ul').find_all('li')

        for index, value in enumerate(ingredients):
            self.ingredients.append(value.text)

        rdr_tags = div_recipe.find_all('span', class_='rdr-tag')
        extrainfo = div_recipe.find(id="extrainfo").find('ul').find_all('li')

        for index, value in enumerate(extrainfo):
            if index == 0:
                self.estimatedCost = value.text
            if index == 1:
                self.calories = value.text
            if index == 2:
                categories = value.text
                self.categoryTags = categories.split(" · ")

        self.url = url
        self.name = div_recipe.article.section.header.h1.text.strip()
        self.author = div_recipe.find('p', class_ ='rdr-author').find('a').text
        self.difficulty = rdr_tags[0].text
        self.image = div_recipe.find('img', class_ = 'mainphoto').get('src')

        load_requests(self.image)
        try:
            self.videoContentUrl = str(div_recipe.find('div', class_ = "wp-block-embed__wrapper").find('iframe').attrs['src'])
        except :
            print ("No hay video de receta: " + self.name)
        self.totalTime = rdr_tags[1].text
        self.recipeYield = rdr_tags[2].text
        self.ratingValue = div_recipe.find('span', class_ = 'rf_average').text
        self.reviewCount = div_recipe.find('span', class_ = 'rf_count').text

if __name__ == '__main__':
    URL = "https://www.recetasderechupete.com/todas/recetas/carnes-aves/recetas-con-pollo/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    recipes = []

    tag_current_page=soup.find_all('span', class_ = 'page-numbers current')
    tag_next_page=soup.find_all('a', class_ = 'next page-numbers')
    print(URL)
    print("numero pagina actual" + tag_current_page[0].text.strip())
    while len(tag_next_page)>0 :
        print("url siguiente pagina" + tag_next_page[0]['href'])  # Url de pagina siguiente
        page=requests.get(tag_next_page[0]['href'])
        soup = BeautifulSoup(page.content, "html.parser")
        url_current_page = tag_next_page[0]['href']
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
            #break
        #break
    extract_csv(recipes)
    # Evidencia de que se ha guardado bien
    print("receta url: " + recipes[0].url)
    print("receta name: " + recipes[0].name)
    print("receta author: " + recipes[0].author)
    print("receta difficulty: " + recipes[0].difficulty)
    print("receta ingredients: " + str(recipes[0].ingredients))
    print("receta videoContentUrl: " + recipes[0].videoContentUrl)
    print("receta calories: " + recipes[0].calories)
    print("receta totalTime: " + recipes[0].totalTime)
    print("receta recipeYield: " + recipes[0].recipeYield)
    print("receta estimatedCost: " + recipes[0].estimatedCost)
    print("receta ratingValue: " + recipes[0].ratingValue)
    print("receta reviewCount: " + recipes[0].reviewCount)
    print("receta categoryTags: " + str(recipes[0].categoryTags))
    print("receta image: " + recipes[0].image)
