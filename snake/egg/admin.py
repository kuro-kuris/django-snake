from django.contrib import admin

from .models import User, Pet, Saving_Account

class PetInline(admin.StackedInline):
    model = Pet

class Saving_AccountInLine(admin.StackedInline):
    model = Saving_Account

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User name:',               {'fields': ['username']}),
        ('Budge amount:', {'fields': ['budget'], 'classes': ['collapse']}),
    ]
    inlines = [PetInline,Saving_AccountInLine]

admin.site.register(User, UserAdmin)
