from django.contrib import admin
from .models import Chapter

# Custom function that might cause duplicate registrations
def register_model(model):
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass  # Ignore if already registered

register_model(Chapter)
