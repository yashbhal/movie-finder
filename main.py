import random
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'


def main():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # selects all html td elements with class titleColumn
    movietags = soup.select('td.titleColumn')
    # selects the a tag inside the titleColumns
    inner_movietags = soup.select('td.titleColumn a')
    # gets ratings
    rating_tags = soup.select('td.posterColumn span[name=ir]')

    movietag0 = movietags[0]
    innermovietag0 = inner_movietags[0]

    # year is the last element in the split. get_year gets all years in the movietags

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        return year

    years = [get_year(tag) for tag in movietags]  # gets all years

    actors_list = [tag['title'] for tag in inner_movietags]  # gets all actors
    titles = [tag.text for tag in inner_movietags]  # gets all movie titles
    ratings = [float(value['data-value']) for value in rating_tags]

    n_movies = len(titles)

    while(True):
        i = random.randrange(0, n_movies)

        print(
            f'{titles[i]} {years[i]}, rating: {ratings[i]:.1f}, starring: {actors_list[i]}')

        user_input = input("Do you want another movie suggestion? (y/n)")
        if user_input != 'y':
            break


if __name__ == '__main__':
    main()
