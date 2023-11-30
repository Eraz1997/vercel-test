from uvicorn import run

from backend.app import create_api_app


def main() -> None:
    app = create_api_app()
    run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
