class Logger:

    @staticmethod
    def line():
        print("-" * 60)

    @staticmethod
    def info(text):
        print(text)

    @staticmethod
    def success(text):
        print(f"[ OK ] {text}")

    @staticmethod
    def warning(text):
        print(f"[WARN] {text}")

    @staticmethod
    def error(text):
        print(f"[FAIL] {text}")