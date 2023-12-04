from uvicorn import run

from backend.app import create_app
from backend.settings import Settings


def main() -> None:
    settings = Settings()
    app = create_app()
    run(app, host=settings.host, port=settings.port)


if __name__ == "__main__":
    main()
