from django.urls import path
from .views import FruitDetailView, FruitListView, FruitSearchView

urlpatterns = [
    # path('', send_fruits),
    path('', FruitListView.as_view(), name='fruit-list'),

    path(
        'search/<str:name>/',
        FruitSearchView.as_view(),
        name='fruit-search'
    ),

    # path(
    #     '<int:pk>/',
    #     FruitDetailView.as_view(),
    #     name='fruit-detail'
    # ),
    path('<str:name>/', FruitDetailView.as_view(), name='fruit-detail')

]
