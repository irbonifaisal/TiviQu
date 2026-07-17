from encoder.services import FFProbeService


class Analyzer:

    def __init__(self):

        self.ffprobe = FFProbeService()

    def analyze(self, movies):

        for movie in movies:

            print()
            print(f"Movie : {movie.title}")

            for ep in movie.episodes:

                print(f"    {ep.filename}")

                info = self.ffprobe.probe(str(ep.filepath))

                print(
                    f"        Streams : {len(info.get('streams', []))}"
                )