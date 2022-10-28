from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Book, Category, Email, Listing, active_all
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Category)
# admin.site.register(Comment)
admin.site.register(Email)
admin.site.register(Listing)
admin.site.register(active_all)


