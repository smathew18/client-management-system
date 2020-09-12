from django.contrib import admin

from .models import Client, Comment, Vehicle


class VehicleInline(admin.TabularInline):
    model = Vehicle


class CommentInline(admin.TabularInline):
    model = Comment


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        VehicleInline,
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
admin.site.register(Vehicle)
