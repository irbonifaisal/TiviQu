from encoder.config import APP_NAME, VERSION
from encoder.utils.logger import Logger

from encoder.core.scanner import Scanner
from encoder.encoder import Encoder


def main():

    Logger.line()
    Logger.info(APP_NAME)
    Logger.info(f"Version : {VERSION}")
    Logger.line()
    print()

    # ==========================================
    # Scan Workspace
    # ==========================================

    Logger.info("Scanning workspace...")

    scanner = Scanner()
    movies = scanner.scan()

    Logger.success(f"{len(movies)} movie ditemukan")

    if not movies:
        Logger.warning("Tidak ada movie yang ditemukan.")
        Logger.line()
        return

    print()

    for movie in movies:

        Logger.info(f"Movie : {movie.title}")
        Logger.info(f"Genre : {movie.genre}")
        Logger.info(f"Tahun : {movie.year}")

        print()

        for episode in movie.episodes:

            Logger.info(
                f"  EP{episode.number:02d}  {episode.title}"
            )

        print()

    # ==========================================
    # Encode HLS
    # ==========================================

    Logger.line()
    Logger.info("Memulai proses encoding...")
    Logger.line()

    encoder = Encoder()
    encoder.encode(movies)

    print()

    Logger.line()
    Logger.success("Semua proses selesai.")
    Logger.line()