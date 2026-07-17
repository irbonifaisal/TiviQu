from encoder.config import OUTPUT_DIR
from encoder.services.ffmpeg_service import FFmpegService
from encoder.utils.logger import Logger


class Encoder:

    def __init__(self):

        self.ffmpeg = FFmpegService()

    def encode(self, movies):

        for movie in movies:

            Logger.line()
            Logger.info(f"Encoding : {movie.title}")

            movie_output = OUTPUT_DIR / movie.id

            for episode in movie.episodes:

                Logger.info(f"  EP{episode.number:02d}")

                output = movie_output / f"episode{episode.number:02d}"

                playlist = self.ffmpeg.encode_hls(
                    episode.filepath,
                    output
                )

                Logger.success(f"HLS : {playlist}")