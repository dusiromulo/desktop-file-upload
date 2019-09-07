from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import User as UserModel

# Unregister unnecessary models
admin.site.unregister(User)
admin.site.unregister(Group)

# Register my model
admin.site.register(UserModel)
