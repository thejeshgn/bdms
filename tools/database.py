import os
from functools import wraps
from fabric.api import local, settings


def needsdatabase(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        local("python manage.py syncdb --settings=bdms.settings")
        return f(*args, **kwargs)
    return wrap

def remote_syncdb():
    local("heroku run python manage.py syncdb --settings=bdms.settings")

def what_is_my_database_url():
    local("heroku config | grep POSTGRESQL")

# def remote_migrate(app_name):
#     if os.path.exists(os.path.join(app_name, "migrations")):
#         with settings(warn_only=True):
#             r = local("heroku run python manage.py migrate %s --settings=bdms.settings" % (app_name), capture=True)
#             if r.find("django.db.utils.DatabaseError") != -1:
#                 print "Normal migration failed. Running a fake migration..."
#                 local("heroku run python manage.py migrate %s --settings=bdms.settings --fake" % (app_name))

def remote_migrate(app_name):
    local("heroku run python manage.py migrate --settings=bdms.settings" , capture=True)


def local_migrate(app_name):
    #TODO: figure out if there are actual models within the app
    if not os.path.exists(os.path.join(app_name, "models.py")):
        return

    if not os.path.exists(os.path.join(app_name, "migrations")):
        with settings(warn_only=True):
            r = local("python manage.py convert_to_south %s --settings=bdms.settings" % app_name, capture=True)
            if r.return_code != 0:
                return
    else:
        #app has been converted and ready to roll
        
        with settings(warn_only=True):
            r = local("python manage.py schemamigration apps.%s --auto --settings=bdms.settings" % app_name)

            if r.return_code != 0:
                print "Scema migration return code != 0 -> nothing to migrate"
            else:
                local("python manage.py migrate apps.%s --settings=bdms.settings" % (app_name))