from django.urls import path

from animal.views import home_page, create_animal, edit_animal, delete_animal, animal_details, cure_animal

urlpatterns = [
    path('', home_page, name='home page'),
    path('create/', create_animal, name='create animal'),
    path('edit/<int:pk>/', edit_animal, name='edit animal'),
    path('delete/<int:pk>', delete_animal, name='delete animal'),
    path('details/<int:pk>', animal_details, name='animal details'),
    path('cure/<int:pk>', cure_animal, name='cure animal'),
]
