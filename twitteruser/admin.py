from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TwitUser

class CustomUserAdmin(UserAdmin):
  model = TwitUser

  fieldsets = (
    *UserAdmin.fieldsets,
    (
      "Connections Made",
      {
        'fields': (
          'following',
        )
      }
    )
  )


admin.site.register(TwitUser, CustomUserAdmin)

