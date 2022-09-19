import requests
from bs4 import BeautifulSoup
from Session26A import IMDBMovieRating

url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)

# HTML Source Code
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

# tag = soup.find("title")
# print(tag.text)

# tags = soup.find_all("title")
tags = soup.find_all("td", class_="titleColumn")
rating_tags = soup.find_all("td", class_="ratingColumn imdbRating")

years = []
names = []
ratings = []

movies = []

for tag in tags:
    text = tag.text.strip()
    # print(text)
    # print(text)
    # print(text[-5:-1])
    years.append(int(text[-5:-1]))
    data = text[:-6]
    idx = data.index(".") + 1
    # print(data[idx:].strip())
    names.append(data[idx:].strip())

for tag in rating_tags:
    # print(tag.text)
    ratings.append(float(tag.text.strip()))

# print(years)
# print(names)
# print(ratings)


for idx in range(len(years)):
    rating = IMDBMovieRating(year=years[idx], name=names[idx], rating=ratings[idx])
    movies.append(rating)

file = open("ratings.csv", "a")

for movie in movies:
    # print(movie.to_csv())
    file.write(movie.to_csv())

print("THANK YOU :)")

# Assignment: Web Scrap IPL Data and generate CSV Files :)