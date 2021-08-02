from django.contrib import admin

# Register your models here.

from .models import User, Lead, Agent, UserProfiles

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(UserProfiles)
