from settings import *
import dj_database_url

DATABASES = {}

DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = os.environ['SECRET_KEY']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
