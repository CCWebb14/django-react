from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    print(request.body)
    return render(request, 'frontend/index.html')



