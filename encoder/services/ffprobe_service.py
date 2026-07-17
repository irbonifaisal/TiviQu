import json
import subprocess

from encoder.config import FFPROBE


class FFProbeService:
    """
    Service untuk membaca metadata video menggunakan FFprobe.
    """

    def probe(self, video_file: str) -> dict:

        if not FFPROBE.exists():
            raise FileNotFoundError(
                f"FFprobe tidak ditemukan:\n{FFPROBE}"
            )

        cmd = [
            str(FFPROBE),
            "-v",
            "quiet",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            video_file,
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr)

        return json.loads(result.stdout)