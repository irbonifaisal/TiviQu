from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Episode:
    """
    Menyimpan informasi satu episode beserta metadata video.
    """

    # Metadata dari movie.json
    id: str
    number: int
    title: str

    # Lokasi file video
    filename: str
    filepath: Path

    # Metadata video (akan diisi oleh Analyzer / FFprobe)
    duration: float = 0.0

    width: int = 0
    height: int = 0

    fps: float = 0.0

    video_codec: str = ""
    audio_codec: str = ""

    bitrate: int = 0