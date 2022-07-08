from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def main_page(request):
    # тут будем доставать с бд тест и посылать отфильтрованную инфу в html
    return render(request, 'testenglish/Главная.html', {})


def main_test(request):
    questions = Question.objects.all()
    return render(request, 'testenglish/TestYourself.html', {'questions': questions})


def test_yourself_result(request):
    if request.method == 'GET':
        k = 0
        questions = Question.objects.filter(order__lt=16)
        for j in dict(request.GET)['answer']:
            for i in questions:
                if i.correct_answer == j:
                    k += 1
                    break
        if k <= 5:
            return HttpResponse(f'Your english level - Elementary. Количество правильных ответов - {k}')
        elif 5 < k <= 10:
            return HttpResponse(f'Your english level - Intermediate. Количество правильных ответов - {k}')
        else:
            return HttpResponse(f'Your english level - Advanced. Количество правильных ответов - {k}')


def help_page(request):
    return render(request, 'testenglish/Помощь.html', {})


def login(request):
    return render(request, 'testenglish/Вход.html', {})


def register(request):
    return render(request, 'testenglish/Регистрация.html', {})


def tests_page(request):
    return render(request, 'testenglish/Тесты.html', {})


def tests_by_level(request, level):
    questions = Question.objects.all()
    if level == 1:
        return render(request, 'testenglish/Test-1.html', {'questions': questions})
    elif level == 2:
        return render(request, 'testenglish/Test-2.html', {'questions': questions})
    elif level == 3:
        return render(request, 'testenglish/Test-3.html', {'questions': questions})


def pageNotFound(request, exception):
    return render(request, 'testenglish/NotFound.html')
