from django.contrib import admin
from django.urls import path
from fee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.custom_login, name='custom_login'),
]
