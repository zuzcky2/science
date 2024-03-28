from app.packages.support import env

configs = {
    'default_driver': 'fastapi',
    'root_path': '',
    'openapi_url': '/openapi.json',
    'redoc_url': '/redoc',
    'title': 'mlOps',
    'description': 'mlOps description',
    'version': '1.0.0',
    'security': {
        'allow_origins': ["*"],
        'allow_credentials': True,
        'allow_methods': ["*"],
        'allow_headers': ["*"]
    }
}