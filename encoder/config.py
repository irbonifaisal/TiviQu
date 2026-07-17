from pathlib import Path

APP_NAME = "TiviQu Encoder"
VERSION = "2.0.0"

# folder encoder/
BASE_DIR = Path(__file__).resolve().parent

# root project
PROJECT_DIR = BASE_DIR.parent

# workspace
WORKSPACE_DIR = BASE_DIR / "workspace"

INPUT_DIR = WORKSPACE_DIR / "input"
OUTPUT_DIR = WORKSPACE_DIR / "output"
CACHE_DIR = WORKSPACE_DIR / "cache"
TEMP_DIR = WORKSPACE_DIR / "temp"
LOG_DIR = WORKSPACE_DIR / "logs"

# tools
TOOLS_DIR = PROJECT_DIR / "tools"

FFMPEG = TOOLS_DIR / "ffmpeg" / "ffmpeg.exe"
FFPROBE = TOOLS_DIR / "ffmpeg" / "ffprobe.exe"
FFPLAY = TOOLS_DIR / "ffmpeg" / "ffplay.exe"

# encoder
VIDEO_CODEC = "libx264"
AUDIO_CODEC = "aac"

SEGMENT_DURATION = 4
THUMBNAIL_TIME = 10