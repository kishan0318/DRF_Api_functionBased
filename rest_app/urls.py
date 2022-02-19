from typing import Pattern
from django.urls import path
from . import views

urlpatterns = [
    path('items',views.list_items),
    path('detail/<int:pk>',views.detailed_view),
    path('create',views.create_view),
    path('update/<int:pk>',views.update_view),
    path('delete/<int:pk>',views.delete_view),
]
