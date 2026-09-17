import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import Fruit


class FruitListView(ListView):
    queryset = Fruit.objects.all()
    template_name = 'fruit_list.html'


class FruitSearchView(ListView):
    model = Fruit
    template_name = 'fruit_list.html'

    def get_queryset(self):
        name = self.kwargs['name']
        return Fruit.objects.filter(name__icontains=name)


class FruitDetailView(DetailView):
    model = Fruit
    template_name = 'fruit_detail.html'

    # def get_queryset(self):
    #     slug = self.kwargs['slug']
    #     return Fruit.objects.filter(slug=slug)

    def get_object(self):
        return Fruit.objects.get(name=self.kwargs['name'])


# def send_fruits(request):
#     # fruits - List containing 5 fruits as dictionaries
#     fruits = [
#         {
#             'name': 'Apple',
#             'color': 'Red',
#             'weight': 150
#         },
#         {
#             'name': 'Banana',
#             'color': 'Yellow',
#             'weight': 120
#         },
#         {
#             'name': 'Mango',
#             'color': 'Yellow',
#             'weight': 200
#         },
#         {
#             'name': 'Grapes',
#             'color': 'Purple',
#             'weight': 50
#         },
#         {
#             'name': 'Lemon',
#             'color': 'Yellow',
#             'weight': 100
#         }
#     ]

#     # return HttpResponse(
#     #     json.dumps({'fruits': fruits}),
#     #     content_type='application/json'
#     # )

#     # Alternative:
#     return JsonResponse({'fruits': fruits})
