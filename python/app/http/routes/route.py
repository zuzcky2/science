from app.packages.api.src.http.fastapi_route import router


@router.get('/')
def root():
    return 'Hello World!'

