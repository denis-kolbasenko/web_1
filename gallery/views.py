from django.shortcuts import render
from .models import Asset # Импортируем модель, чтобы спрашивать данные

def home(request):
# all() возвращает хаос.
# order_by('-created_at') сортирует по полю created_at.
# Минус (-) означает "по убыванию" (DESC).
    assets = Asset.objects.all().order_by('-created_at')
    context_data = {
        'page_title': 'Главная Галерея',
        'assets': assets,
    }
    return render(request, 'gallery/index.html', context_data)

def about(request):
    return render(request, 'gallery/about.html')

def upload(request):
    return render(request, 'gallery/upload.html')
