import os  # <-- 1. Add this import
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jiqy%haz7m+v*^akke^m9mff3c8i%cvmqnhs3)8u72j5)_6w!w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 2. Change this line to read from the environment
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1').split(',')


# Application definition

INSTALLED_APPS = [
    'api',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# ... (the rest of your file is correct and remains unchanged) ...
# ...
# ...

# Add this at the end of settings.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
# Add this at the end of settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}