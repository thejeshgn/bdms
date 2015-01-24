from settings import *
import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = True


DATABASES = {}

DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = os.environ['SECRET_KEY']


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



BASE_URL='http://buzzdatabase.herokuapp.com/'

