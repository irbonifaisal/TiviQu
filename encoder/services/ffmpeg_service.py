import subprocess
from pathlib import Path

from encoder.config import FFMPEG


class FFmpegService:

    def encode_hls(
        self,
        input_file: Path,
        output_dir: Path,
    ) -> Path:

        output_dir.mkdir(parents=True, exist_ok=True)

        playlist = output_dir / "master.m3u8"
        segment_pattern = output_dir / "segment_%03d.ts"

        cmd = [
            str(FFMPEG),

            "-y",

            "-i", str(input_file),

            "-c:v", "libx264",
            "-preset", "veryfast",

            "-c:a", "aac",
            "-b:a", "128k",

            "-hls_time", "4",
            "-hls_playlist_type", "vod",

            "-hls_segment_filename",
            str(segment_pattern),

            str(playlist)
        ]

        subprocess.run(cmd, check=True)

        return playlist