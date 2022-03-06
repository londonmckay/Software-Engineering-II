"""Assignment1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from users import views as user_views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('mysite/', include('mysite.urls')),
    path('register/', user_views.register, name="register"),
    path('accounts/', include("django.contrib.auth.urls")),

    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    # path('login/', user_views.user_login, name="login"),
    # path('logout/', user_views.user_logout, name="logout"),

    path('profile/', user_views.profile, name="profile"),
    path('calendar/', user_views.calendar, name="calendar"),
    path('courses/', include('course.urls')),

    #******For payment urls
    path('payment/', include('payment.urls')),


]


