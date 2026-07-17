from encoder.models import Movie


class Validator:

    def validate(self, movies: list[Movie]) -> bool:

        ok = True

        for movie in movies:

            print()
            print(f"Movie : {movie.title}")

            assets = [
                movie.poster,
                movie.banner,
                movie.logo
            ]

            for asset in assets:

                file = movie.folder / asset

                if file.exists():
                    print(f"    ✓ {asset}")
                else:
                    print(f"    ✗ {asset}")
                    ok = False

            for ep in movie.episodes:

                if ep.filepath.exists():
                    print(f"    ✓ {ep.filename}")
                else:
                    print(f"    ✗ {ep.filename}")
                    ok = False

        return ok