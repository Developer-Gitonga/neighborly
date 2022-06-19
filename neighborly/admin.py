from django.contrib import admin
from .models import Profile, Business, Neighborhood, Contact
# Register your models here.

admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Neighborhood)
admin.site.register(Contact)
