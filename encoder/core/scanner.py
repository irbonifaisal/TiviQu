import inspect
import json

from encoder.config import INPUT_DIR
from encoder.models import Movie, Episode


print("Episode module :", Episode.__module__)
print("Episode sign   :", inspect.signature(Episode))
print("-" * 50)


class Scanner:

    def scan(self) -> list[Movie]:

        movies = []

        if not INPUT_DIR.exists():
            return movies

        for movie_folder in INPUT_DIR.iterdir():

            if not movie_folder.is_dir():
                continue

            movie_json = movie_folder / "movie.json"

            if not movie_json.exists():
                continue

            with open(movie_json, "r", encoding="utf-8") as f:
                data = json.load(f)

            movie = Movie(
                id=data["id"],
                title=data["title"],
                genre=data.get("genre", ""),
                year=data.get("year", ""),
                synopsis=data.get("synopsis", ""),
                folder=movie_folder,
                poster=data.get("poster", "poster.jpg"),
                banner=data.get("banner", "banner.jpg"),
                logo=data.get("logo", "logo.png"),
            )

            for ep_data in data.get("episodes", []):

                ep = Episode(
                    id=ep_data["id"],
                    number=ep_data["number"],
                    title=ep_data["title"],
                    filename=ep_data["filename"],
                    filepath=movie_folder / ep_data["filename"],
                )

                movie.episodes.append(ep)

            movies.append(movie)

        return movies