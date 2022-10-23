from django.urls import path

from inventory import views

urlpatterns = [
    path('add_produto/', views.add_product, name="add_product"),
    path('produto/<slug:slug>/', views.show_product, name="show_product")
]
