from app.packages.support import env

configs = {
    'app_name': env.get('APP_NAME'),
    'app_version': env.get('APP_VERSION'),
    'project_root': env.get('PROJECT_ROOT')
}