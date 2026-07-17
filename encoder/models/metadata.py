from dataclasses import dataclass


@dataclass(slots=True)
class VideoMetadata:
    """
    Metadata video hasil analisis FFprobe.
    """

    duration: float = 0.0

    width: int = 0
    height: int = 0

    fps: float = 0.0

    video_codec: str = ""
    audio_codec: str = ""

    bitrate: int = 0

    file_size: int = 0

    format_name: str = ""