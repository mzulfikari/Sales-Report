import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-6)_w93d+nk+9ps3$v8wxe9@44-7llw12d0o)5iu9#bq1jeos@-'

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #jalali_date
    'jalali_date',
    
    #my_app 
    'Services.apps.ServicesConfig',
    'account.apps.AccountConfig',
    'Store.apps.StoreConfig',
    'Dashbord.apps.DashbordConfig',
      

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SalesReport.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SalesReport.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': 'DB_NAME',
#         'USER': 'DB_USER',
#         'PASSWORD': 'DB_PASSWORD',
#         'HOST': 'localhost',   
#         'PORT': '3306',
#     }
# }



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# default settings (optional)
JALALI_DATE_DEFAULTS = {
   # if change it to true then all dates of the list_display will convert to the Jalali.
   'LIST_DISPLAY_AUTO_CONVERT': False,
   'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            'admin/js/django_jalali.min.js',
        ],
        'css': {
            'all': [
              'admin/css/django_jalali.min.css',
            ]
        }
    },
}

AUTH_USER_MODEL = "account.User"
LOGOUT_REDIRECT_URL = '/'
