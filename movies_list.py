import requests
from bs4 import BeautifulSoup

movies_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# get data using requests.get()

response = requests.get(movies_url)
data = response.text

# Parse data using BeautifulSoup

soup = BeautifulSoup(data, "html.parser")
titles = soup.find(name="h3", class_="title").getText()

movie_titles = []

for title in soup.find_all(name="h3", class_="title"):
    title_text = title.getText()
    movie_titles.append(title_text)

# reverse movie titles

movie_titles.reverse()

# Transfer data to text file

with open("movie_list.txt", "w") as file:
    for movie in movie_titles:
        file.write(movie + "\n")
