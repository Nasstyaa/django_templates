from django.shortcuts import render

from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def index(request):
  return HttpResponse('Главная страница')

def get_reciept(request, dish_name):
  if dish_name in DATA:
    reciept = DATA[dish_name]
    quantity = request.GET.get('quantity', 1)

    if quantity:
      new_reciept = {}
      for key, value in reciept.items():
        new_value = value * int(quantity)
        new_reciept[key] = new_value

      context = {
        'dish_name': dish_name,
        'reciept': new_reciept,
      }

  else:
    context = None

  return render(request, template_name='calc/reciepts.html',context=context)
# Create your views here.
