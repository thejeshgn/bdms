from settings import *
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False


DATABASES = {}

DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = os.environ['SECRET_KEY']



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "bdms","static"),
    os.path.join(PROJECT_ROOT, "django_admin_bootstrapped","static"),

    )



BASE_URL='http://buzzdatabase.herokuapp.com/'

