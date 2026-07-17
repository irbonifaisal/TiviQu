from dataclasses import dataclass, field
from pathlib import Path

from encoder.models.metadata import VideoMetadata


@dataclass(slots=True)
class Episode:
    """
    Satu episode film.
    """

    id: str

    number: int

    title: str

    filename: str

    filepath: Path

    metadata: VideoMetadata = field(default_factory=VideoMetadata)