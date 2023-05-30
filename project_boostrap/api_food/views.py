from django.shortcuts import render
from utils.empresas.factory import make_recipe


def home(request):
    return render(request, 'api_food/pages/home.html', 
                  context={
        "empresas": [make_recipe() for _ in range(10)]
    }
    )