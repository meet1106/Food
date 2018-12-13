from .common import *
DEBUG = True
ALLOWED_HOSTS = ['*']
import os.path
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
FIXTURE_DIRS = (os.path.join(PROJECT_ROOT, 'fixtures'),)

import dj_database_url
DATABASES = {
    'default':'postgres://qexwkdgfglcjja:48c7f388c55b3ea266a3d83d343da9d35bb5705ff575db0801522207a194c11b@ec2-23-21-65-173.compute-1.amazonaws.com:5432/ddrg8b9rhtils2'
}
DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'