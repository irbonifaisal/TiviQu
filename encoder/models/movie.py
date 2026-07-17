from dataclasses import dataclass, field
from pathlib import Path

from encoder.models.episode import Episode


@dataclass(slots=True)
class Movie:
    """
    Informasi satu film.
    """

    id: str

    title: str

    genre: str

    year: int | str

    synopsis: str

    folder: Path

    poster: str

    banner: str

    logo: str

    episodes: list[Episode] = field(default_factory=list)