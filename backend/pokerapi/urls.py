from django.contrib import admin
from django.urls import path, include
from .views import games_list, games_detail



urlpatterns = [
	path("admin/", admin.site.urls),
	path("games/", games_list),
	path("games/<name>", games_detail)
	]
