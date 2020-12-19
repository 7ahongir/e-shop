from django.contrib import admin

from .models import Adress

from django.contrib.auth import get_user_model

class UserAdress(admin.ModelAdmin):
	list_display = ['id', 'adress', 'user_name', 'created_at']

	def user_name(self, obj):
		return obj.user.username

admin.site.register(Adress, UserAdress)

