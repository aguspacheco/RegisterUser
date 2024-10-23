from django.apps import AppConfig
import os

class PageConfig(AppConfig):
    name = 'page'
    default_auto_field = 'django.db.models.BigAutoField'
    path = os.path.dirname(__file__)

