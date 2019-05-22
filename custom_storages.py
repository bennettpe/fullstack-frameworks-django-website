from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# STATIC FILES
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

# MEDIA FILES   
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION    