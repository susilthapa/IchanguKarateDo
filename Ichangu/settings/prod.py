from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', cast=bool)

ALLOWED_HOSTS = ['.herokuapp.com']

# Heroku
# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES.update(default=db_from_env)

DATABASES = {
	'default': dj_database_url.config()
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600 
SECURE_HSTS_INCLUDE_SUBDOMAINS = True 
SECURE_HSTS_PRELOAD = True 
SECURE_CONTENT_TYPE_NOSNIFF = True 
SESSION_COOKIE_SECURE = True 
CSRF_COOKIE_SECURE = True
SECURE_REFERRER_POLICY= 'origin'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

