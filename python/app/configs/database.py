from app.packages.support import env

configs = {
    'default_driver': 'mongodb',
    'mongodb': {
        'host': env.get('MONGO_HOST'),
        'port': env.get('MONGO_PORT'),
        'name': env.get('MONGO_NAME'),
        'user': env.get('MONGO_USER'),
        'pass': env.get('MONGO_PASS')
    }
}