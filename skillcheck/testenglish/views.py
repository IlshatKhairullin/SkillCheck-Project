from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *


def main_page(request):
    # тут будем доставать с бд тест и посылать отфильтрованную инфу в html
    return render(request, 'testenglish/Главная.html', {})


def main_test(request):
    # questions = Questions.objects.all()
    return render(request, 'testenglish/FirstTest.html',)  # {'questions': questions})


def help_page(request):
    return render(request, 'testenglish/Помощь.html', {})


def login(request):
    return render(request, 'testenglish/Вход.html', {})


def register(request):
    return render(request, 'testenglish/Регистрация.html', {})


def tests_page(request):
    return render(request, 'testenglish/Тесты.html', {})


def test_button_A(request):
    # аналогичная работа как в main_page
    return HttpResponse('Тест А(А1/A2)')


def test_button_B(request):
    # аналогичная работа как в main_page
    return HttpResponse('Тест B(B1/B2)')


def test_button_C(request):
    # аналогичная работа как в main_page
    return HttpResponse('Тест C(C1/C2)')


def pageNotFound(request, exception):
    return render(request, 'testenglish/NotFound.html')
