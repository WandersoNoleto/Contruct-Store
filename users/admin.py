from django.contrib import admin
from django.contrib.auth import admin as admin_auth

from .forms import UserChangeForm, UserCreationForm
from .models import Users


@admin.register(Users)
class UserAmin(admin_auth.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
