from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
	path('', views.home, name='reviews-home'),
	path('about/', views.about, name='reviews-about'),
	path('contact/', views.contact, name='reviews-contact'),
	path('product/', views.product, name='reviews-product'),
	path('register/', user_views.register, name='register'),
]