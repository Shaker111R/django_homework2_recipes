from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 300,
        'сыр, г': 50,
    },
    'sandwich': {
        'хлеб, кусок': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def cook_book(request):
    context = {'recipe': {}}
    dish = request.path_info[1:-1]
    servings = request.GET.get("servings", 1)

    if servings == 1 or servings is None or not servings.isdecimal():
        context['recipe'] = DATA[dish]
    else:
        servings = int(servings)
        for ingredient, count in DATA[dish].items():
            context['recipe'][ingredient] = count * servings

    return render(request, 'calculator/index.html', context)
