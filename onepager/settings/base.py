"""
Django settings for onepager project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# Build paths inside the project like this: os.path.join(SITE_ROOT, ...)
SITE_ROOT = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 1

ADMINS = (
    ('admins', 'admin@example.com'),
)
MANAGERS = ADMINS
EMAIL_SUBJECT_PREFIX = '[onepager] '  # subject prefix for managers & admins

SESSION_COOKIE_NAME = 'onepager_ssid'

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'accounts',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'reversion',

    'crispy_forms',
    'webpack_loader',
    'compressor',

    'onepager',
]


MIDDLEWARE_CLASSES = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SITE_ROOT, 'templates'),],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'onepager.context_processors.settings_export',
                'sekizai.context_processors.sekizai',
                'django.core.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]
MIGRATION_MODULES = {
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django'
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'db.sqlite3'),
    }
}


# Caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'KEY_PREFIX': 'onepager',
    }
}


# Internationalization
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'hide_untranslated': False,
            'name': 'en',
            'redirect_on_fallback': True,
            'code': 'en',
            'public': True,
        }
    ],
    'default': {
        'hide_untranslated': False,
        'public': True,
        'redirect_on_fallback': True,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('home.html', 'Main layout'),
    ('cms/pieces/content.html', 'Content block'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}
LOCALE_PATHS = (
    'locale',
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files and media (CSS, JavaScript, images)
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'assets')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
    os.path.join(SITE_ROOT, 'app', 'build'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'tg_utils.compressor_filters.CleanCssFilter',
]
COMPRESS_JS_FILTERS = [
    'tg_utils.compressor_filters.UglifyFilter',
]


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dummy key'

AUTH_USER_MODEL = 'accounts.User'

ALLOWED_HOSTS = []

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SITE_URL = 'http://127.0.0.1:8000'

# This needs to be at minimum "SAMEORIGIN" otherwise django cms on-site editing won't work
X_FRAME_OPTIONS = 'SAMEORIGIN'


ROOT_URLCONF = 'onepager.urls'

WSGI_APPLICATION = 'onepager.wsgi.application'


LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'


# Crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Email config
DEFAULT_FROM_EMAIL = "onepager <info@TODO.com>"
SERVER_EMAIL = "onepager server <server@TODO.com>"

# SMTP
EMAIL_HOST = 'smtp.sparkpostmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'info@TODO.com'
EMAIL_HOST_PASSWORD = 'TODO (test api key)'


# Base logging config. Logs INFO and higher-level messages to console. Production-specific additions are in
#  production.py.
#  Notably we modify existing Django loggers to propagate and delegate their logging to the root handler, so that we
#  only have to configure the root handler.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d %(funcName)s - %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django': {'handlers': [], 'propagate': True},
        'django.request': {'handlers': [], 'propagate': True},
        'django.security': {'handlers': [], 'propagate': True},
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Disable a few system checks. Careful with these, only silence what your really really don't need.
# TODO: check if this is right for your project.
SILENCED_SYSTEM_CHECKS = [
    'security.W001',  # we don't use SecurityMiddleware since security is better applied in nginx config
]


# Default values for sentry
RAVEN_BACKEND_DSN = ''
RAVEN_PUBLIC_DSN = ''
RAVEN_CONFIG = {}


WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': '',
        'STATS_FILE': os.path.join(SITE_ROOT, 'app', 'webpack-stats.json'),
    }
}

# All these settings will be made available to javascript app
SETTINGS_EXPORT = [
    'DEBUG',
    'SITE_URL',
    'STATIC_URL',
    'RAVEN_PUBLIC_DSN',
]
