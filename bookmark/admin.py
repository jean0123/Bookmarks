from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import *

admin.site.site_header = 'BOOKMARKS'


class UsuarioAdmin(UserAdmin):
    model = User

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)
    group.short_description = 'Groups'

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (None, {'fields': ('roles', )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
         'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('username', 'first_name', 'last_name', 'group', 'is_staff')


admin.site.register(User, UsuarioAdmin)
admin.site.register(Rol)


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'private')
    readonly_fields = ('created_by',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
