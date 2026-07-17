from dataclasses import dataclass
from pathlib import Path

from .episode import Episode


@dataclass(slots=True)
class Movie:
    id: str
    title: str
    genre: str
    year: int

    rating: str
    language: str
    description: str

    poster: str
    banner: str
    logo: str

    folder: Path
    episodes: list[Episode]