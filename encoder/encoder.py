from encoder.config import APP_NAME, VERSION
from encoder.core import Scanner, Validator, Analyzer
from encoder.core.logger import success, error


def print_summary(movies):

    total_episode = 0

    print()

    for movie in movies:

        print(f"Movie : {movie.title}")
        print(f"Genre : {movie.genre}")
        print(f"Year  : {movie.year}")
        print()

        for ep in movie.episodes:
            print(f"    Episode {ep.number:02d} : {ep.title}")

        total_episode += len(movie.episodes)

        print()

    print(f"Movies Found   : {len(movies)}")
    print(f"Episodes Found : {total_episode}")


def main():

    print("=" * 50)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print("=" * 50)

    print()
    print("Scanning workspace/input ...")

    scanner = Scanner()
    movies = scanner.scan()

    print_summary(movies)

    print()
    print("Validating ...")

    validator = Validator()

    if not validator.validate(movies):
        print()
        error("Validation Failed")
        return

    print()
    success("Validation Passed")

    print()
    print("Analyzing ...")

    analyzer = Analyzer()
    analyzer.analyze(movies)

    print()
    success("Scanner Finished")


if __name__ == "__main__":
    main()