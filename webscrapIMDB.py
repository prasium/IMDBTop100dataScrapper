from bs4 import BeautifulSoup
import requests
import pandas as pd

# Download IMDB's Top 250 data
url = 'https://www.imdb.com/list/ls091520106/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
movie_containers = soup.find_all('div', class_= 'lister-item mode-detail')
print(len(movie_containers))

#lists to store values
names=[]
years=[]
directors=[]
imdb_ratings=[]
genres=[]

for container in movie_containers:
    name = container.h3.a.text
    names.append(name)
    director= container.find_all('p',class_='text-muted text-small')[1].a.text
    directors.append(director)
    year=container.h3.find('span', class_='lister-item-year text-muted unbold').text.strip('()')
    years.append(year)
    rating=float(container.find('span', class_='ipl-rating-star__rating').text)
    imdb_ratings.append(rating)
    genre=container.find('span', class_='genre').text.strip(' \n').split(', ')
    genres.append(genre)

test_df = pd.DataFrame({
    'Movie': names,
    'Director': directors,
    'Year': years,
    'Rating': imdb_ratings,
    'Genre': genres
})
print(test_df.info())
test_df.to_csv('ImdbTop100.csv')
