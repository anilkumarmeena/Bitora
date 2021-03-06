"""
Django settings for howto project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1gy51#bmv^g^#fc&w9wt)77i!t2au5100jd&0yao%=49bc6m71'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SOCIAL_AUTH_FACEBOOK_KEY = '1909808875929144'
SOCIAL_AUTH_FACEBOOK_SECRET = '60e47322c1d39381de500da161216d76'

SOCIAL_AUTH_GITHUB_KEY = '41c47d472803e4a9f9ba'
SOCIAL_AUTH_GITHUB_SECRET = 'ed5652ef80e72b2ee6141e43972ba2e4919a9950'


SOCIAL_AUTH_TWITTER_KEY = 'M3uqIK0z971dgqYTgDvoVf3jx'
SOCIAL_AUTH_TWITTER_SECRET = 'rW1GD44y5gTzKFLsMPNS80d6glswIo9CXGOFNxHeiPWAFO0DFV'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '811893039464-cgqc42i1r5e0b7jaq69a13ie4gimunqu.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'RdY2UkdkT0V6FMfrzvyv5qt3'

# Imgur Draceditor requirements
# Global draceditor settings
# Input: string boolean, `true/false`
DRACEDITOR_ENABLE_CONFIGS = {
    'imgur': 'true',     # to enable/disable imgur/custom uploader.
    'mention': 'false',  # to enable/disable mention
    'jquery': 'true',    # to include/revoke jquery (require for admin default django)
}

# Imgur API Keys
DRACEDITOR_IMGUR_CLIENT_ID = '59117600889b35e'
DRACEDITOR_IMGUR_API_KEY = 'c5f26349a9a1e32e49170f5a9bdfe0eeb4c8d44e'

# Safe Mode
DRACEDITOR_MARKDOWN_SAFE_MODE = True # default

# Markdownify
DRACEDITOR_MARKDOWNIFY_FUNCTION = 'draceditor.utils.markdownify' # default
DRACEDITOR_MARKDOWNIFY_URL = '/draceditor/markdownify/' # default

# Markdown extensions (default)
DRACEDITOR_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.fenced_code',

    # Custom markdown extensions.
    'draceditor.extensions.urlize',
    'draceditor.extensions.del_ins', # ~~strikethrough~~ and ++underscores++
    'draceditor.extensions.mention', # require for mention
    'draceditor.extensions.emoji',   # require for emoji
]

# Markdown Extensions Configs
DRACEDITOR_MARKDOWN_EXTENSION_CONFIGS = {}

# Markdown urls
DRACEDITOR_UPLOAD_URL = '/draceditor/uploader/' # default
DRACEDITOR_SEARCH_USERS_URL = '/draceditor/search-user/' # default

# Markdown Extensions
DRACEDITOR_MARKDOWN_BASE_EMOJI_URL = 'https://assets-cdn.github.com/images/icons/emoji/' # default
DRACEDITOR_MARKDOWN_BASE_MENTION_URL = 'https://forum.dracos-linux.org/profile/' # default (change this)


# Django allauth settings
LOGIN_URL = 'login/'
LOGOUT_URL = 'logout/'
LOGIN_REDIRECT_URL = '/'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'howto.quora@gmail.com'#email of sender
EMAIL_HOST_PASSWORD = 'howto1234'# password of sender
EMAIL_PORT = 587

ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_AUTHENTICATION_METHOD ='username_email'
ACCOUNT_CONFIRM_EMAIL_ON_GET=True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL='/accounts/login/'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_CONFIRMATION_HMAC=True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'howto '
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_SIGNUP_FORM_CLASS = 'login.forms.UserRegisterForm'
ACCOUNT_USERNAME_MIN_LENGTH = 3

# Application definition

INSTALLED_APPS = [
    'login.apps.LoginConfig',
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pagedown',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'markdownx',
    'draceditor',
    'crispy_forms',
    'braces',
    'notification_channels.apps.NotificationChannelsConfig',
    'notifications',
    'bootstrap3',
    'social_django',
    'friendship',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'howto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {

            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

WSGI_APPLICATION = 'howto.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.howto'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

CRISPY_TEMPLATE_PACK = 'bootstrap3'
STATIC_URL = '/static/'
STATIC_ROOT = 'D:\GitHub\spacesuite\login\static'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
