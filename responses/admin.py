from django.contrib import admin

from .models import Responses, Profile


# Register your models here.
class Responses_admin_view(admin.ModelAdmin):
    list_display = ('id', 'employee', 'top_goal', 'highlights', 'lowlights', 'w_load', 'goal_obs', 'm_tip', 'date')
    list_display_links = ('employee',)
    search_fields = ('employee', 'highlights', 'lowlights', 'date')
    list_filter = ('highlights', 'lowlights', 'date')


class users_admin_view(admin.ModelAdmin):
    list_display = ('user', 'Surname', 'FirstName', 'LastName', 'Role', 'Gender')
    list_display_links = ('user',)
    search_fields = ('Surname',)
    list_filter = ('Role', 'Gender')


admin.site.register(Responses, Responses_admin_view)
admin.site.register(Profile, users_admin_view)
