from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def main_page(request):
    # тут будем доставать с бд тест и посылать отфильтрованную инфу в html
    return render(request, 'testenglish/Главная.html', {})


def help_page(request):
    return render(request, 'testenglish/Помощь.html', {})


def login(request):
    return HttpResponse('Вход')


def register(request):
    return HttpResponse('Регистрация')


def tests_page(request):
    return render(request, 'testenglish/Тесты.html', {})


def test_button_A(request):
    # аналогичная работа как в main_page
    return render(request, 'testenglish/ТестA.html', {})


def test_button_B(request):
    # аналогичная работа как в main_page
    return render(request, 'testenglish/ТестB.html', {})


def test_button_C(request):
    # аналогичная работа как в main_page
    return render(request, 'testenglish/ТестC.html', {})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
