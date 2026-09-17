from django.urls import path
from .views import FruitListView, FruitSearchView

urlpatterns = [
    # path('', send_fruits),
    path('', FruitListView.as_view(), name='fruit-list'),
    path(
        'search/<str:name>/',
        FruitSearchView.as_view(),
        name='fruit-search'
    ),
]
