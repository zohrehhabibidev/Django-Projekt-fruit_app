from django.urls import path
from .views import FruitListView

urlpatterns = [
    # path('', send_fruits),
    path('', FruitListView.as_view(), name='fruit-list'),
]
