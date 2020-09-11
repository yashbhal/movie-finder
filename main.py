import random
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'


def main():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # gets all movie tags
    movietags = soup.select('td.titleColumn')
    # seleects the actors list
    inner_movietags = soup.select('td.titleColumn a')
    # gets movie ratings
    rating_tags = soup.select('td.posterColumn span[name=ir]')

    # year is the last element in the split. get_year gets all years in the movietags
    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        return year

    year = [get_year(tag) for tag in movietags]  # gets all years
    actors_list = [tag['title'] for tag in inner_movietags]  # gets all actors
    title = [tag.text for tag in inner_movietags]  # gets all movie titles
    rating = [float(value['data-value'])
              for value in rating_tags]  # gets all ratings

    n_movies = len(title)

    while(True):
        i = random.randrange(0, n_movies)

        print(
            f'{title[i]} {year[i]}, rating: {rating[i]:.1f}, starring: {actors_list[i]}')

        user_input = input("Do you want another movie suggestion? (y/n)")
        if user_input != 'y':
            break


if __name__ == '__main__':
    print("Here's a movie suggestion for you!")
    main()
