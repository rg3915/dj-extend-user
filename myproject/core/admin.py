from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile
from .forms import ProfileAdminForm


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_staff', 'get_location')
    list_select_related = ('profile', )
    actions = None

    def has_delete_permission(self, request, obj=None):
        return False

    def get_location(self, instance):
        return instance.profile.location
    get_location.short_description = 'Location'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    readonly_fields = ('user',)
    form = ProfileAdminForm


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
