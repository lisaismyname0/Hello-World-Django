from django.contrib import admin
# django admin is a tool that helps us look at the database. we have to tell the django admin what models we have

# Register your models here.
from .models import Flavor, User, Season

admin.site.register(User)
admin.site.register(Flavor)
admin.site.register(Season)

