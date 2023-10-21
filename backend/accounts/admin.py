from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields':()}),
    )
    list_display = [
        "id",
        "email",
        "username",
        "is_superuser",
        "is_staff",
      
    ]  

admin.site.register(CustomUser, CustomUserAdmin)