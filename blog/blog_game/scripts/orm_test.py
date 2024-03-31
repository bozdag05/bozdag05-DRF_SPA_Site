from django.contrib.contenttypes.models import ContentType
from django.db import connection

def master():
    content_types = ContentType.objects.all()