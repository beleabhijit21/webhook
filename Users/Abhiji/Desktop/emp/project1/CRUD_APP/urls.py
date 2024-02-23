from django.urls import path
from . import views

urlpatterns = [
    path('av/', views.addOrder_view,name='add_urls'),
    path('sv/',views.show_view,name='show_urls'),
    path('up/<int:upk>/', views.update_view, name='update_url'),
    path('dl/<int:pk>/', views.delete_view,name='delete_url')
]
