from settings import *
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False


DATABASES = {}

DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = os.environ['SECRET_KEY']


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'

if DEBUG: 
   STATIC_ROOT = os.path.join(BASE_DIR, '/static')
else:
   STATIC_ROOT = os.path.join(BASE_DIR, 'static') 

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


BASE_URL='http://buzzdatabase.herokuapp.com/'

