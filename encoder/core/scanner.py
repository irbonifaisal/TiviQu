import json
from pathlib import Path

from encoder.config import INPUT_DIR
from encoder.models import Movie, Episode


class Scanner:
    """
    Scanner untuk mencari seluruh movie pada workspace/input
    """

    def scan(self) -> list[Movie]:

        movies = []

        if not INPUT_DIR.exists():
            return movies

        for folder in INPUT_DIR.iterdir():

            if not folder.is_dir():
                continue

            movie_file = folder / "movie.json"

            if not movie_file.exists():
                continue

            movie = self.load_movie(folder, movie_file)

            if movie:
                movies.append(movie)

        return movies

    def load_movie(self, folder: Path, movie_file: Path) -> Movie:

        with open(movie_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        movie = Movie(

            id=data.get("id", ""),

            title=data.get("title", ""),

            genre=data.get("genre", ""),

            year=data.get("year", ""),

            synopsis=data.get("synopsis", ""),

            folder=folder,

            poster=data.get("poster", ""),

            banner=data.get("banner", ""),

            logo=data.get("logo", ""),

        )

        for ep in data.get("episodes", []):

            episode = Episode(

                id=ep.get("id", ""),

                number=ep.get("number", 0),

                title=ep.get("title", ""),

                filename=ep.get("filename", ""),

                filepath=folder / ep.get("filename", "")

            )

            movie.episodes.append(episode)

        return movie