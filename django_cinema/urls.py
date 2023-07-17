"""
URL configuration for django_cinema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from cinema_app.views import Login, Logout, Register, HallCreateView, SessionCreateView, FilmCreateView, FilmListView, \
    SessionUpdateView, PurchaseCreateView, FilmDetailView, BasketListView, HallUpdateView

urlpatterns = [
    path('admin', admin.site.urls),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('register', Register.as_view(), name='register'),
    path('create_hall', HallCreateView.as_view(), name='create_hall'),
    path('create_session', SessionCreateView.as_view(), name='create_session'),
    path('create_film', FilmCreateView.as_view(), name='create_film'),
    path('show_purchase/<int:pk>', FilmDetailView.as_view(), name='purchase_detail'),
    path('create_purchase/<int:session_id>', PurchaseCreateView.as_view(), name='purchase_create'),
    path('update_session/<int:pk>', SessionUpdateView.as_view(), name='update_session'),
    path('update_hall/<int:pk>', HallUpdateView.as_view(), name='update_hall'),
    path('basket/', BasketListView.as_view(), name='basket'),
    path('', FilmListView.as_view(), name='index'),
    path('', include('cinema_app.urls')),
    ]
