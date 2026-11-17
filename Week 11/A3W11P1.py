import os
import sys
import json


MOVIES_FILE = "movies.json"


def load_movies(filename=MOVIES_FILE):
    with open(filename, "r") as file:
        return json.load(file)


def save_movies(movies, filename=MOVIES_FILE):
    with open(filename, "w") as file:
        json.dump(movies, file, indent=4)


def find_movie(movies, title):
    return next((movie for movie in movies if movie["title"] == title), None)


def modify_movies(movies):
    gladiator = find_movie(movies, "Gladiator")
    if gladiator is not None:
        gladiator["year"] = 2001

    oldest_movie = min(movies, key=lambda movie: movie["year"])
    oldest_movie["year"] -= 1

    for movie in movies:
        movie["cast"] = [
            "Nat Portman" if actor == "Natalie Portman" else actor
            for actor in movie["cast"]
            if actor != "Kevin Spacey"
        ]


def print_information_overview(movies):
    movies_from_2004 = sum(movie["year"] == 2004 for movie in movies)
    science_fiction_movies = sum(
        "Science Fiction" in movie["genres"] for movie in movies
    )
    keanu_movies = [
        movie for movie in movies if "Keanu Reeves" in movie["cast"]
    ]
    stallone_movies = [
        movie
        for movie in movies
        if "Sylvester Stallone" in movie["cast"]
        and 1995 <= movie["year"] <= 2005
    ]

    print(f"Movies released in 2004: {movies_from_2004}")
    print(f"Science Fiction movies: {science_fiction_movies}")
    print("Movies with Keanu Reeves:")
    for movie in keanu_movies:
        print(movie)
    print("Movies with Sylvester Stallone from 1995 to 2005:")
    for movie in stallone_movies:
        print(movie)


def run_application(filename=MOVIES_FILE):
    movies = load_movies(filename)

    while True:
        choice = input().upper()

        if choice == "I":
            print_information_overview(movies)
        elif choice == "M":
            modify_movies(movies)
            save_movies(movies, filename)
        elif choice == "S":
            title = input("Enter movie title: ")
            movie = find_movie(movies, title)
            if movie is not None:
                print(movie)
        elif choice == "C":
            title = input("Enter movie title: ")
            movie = find_movie(movies, title)
            if movie is None:
                continue
            movie["title"] = input("Enter new title: ")
            movie["year"] = int(input("Enter new release year: "))
            save_movies(movies, filename)
            print(movie)
        elif choice == "Q":
            break


def main() -> None:
    print("[I] Movie information overview")
    print("[M] Make modification based on assignment")
    print("[S] Search a movie title ")
    print("[C] Change title and/or release year by search on title")
    print("[Q] Quit program")
    run_application()


if __name__ == "__main__":
    main()