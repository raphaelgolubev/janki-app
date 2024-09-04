import uvicorn


def main():
    module = "src.app:fastapi_app"
    uvicorn.run(
        module,
        host="0.0.0.0",
        port=8000,
        log_level="info",
        reload=True,
    )


if __name__ == '__main__':
    main()
