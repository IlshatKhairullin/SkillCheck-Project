from django.shortcuts import render
from .models import *


def main_page(request):
    return render(request, 'testenglish/Главная.html', {})


def main_test(request):
    questions = Question.objects.all()
    return render(request, 'testenglish/TestYourself.html', {'questions': questions})


def test_yourself_result(request):
    if request.method == 'GET':
        k = 0
        order = 0
        questions = Question.objects.filter(order__lt=16)

        for j in dict(request.GET)['answer']:
            order += 1
            for i in questions:
                if i.correct_answer == j and order == i.order:
                    k += 1
                    break
        if k <= 6:
            return render(request, 'testenglish/Результат.html',
                          {'result': f'Your english level - Elementary. Количество правильных ответов - {k}/15'})
        elif 6 < k <= 11:
            return render(request, 'testenglish/Результат.html',
                          {'result': f'Your english level - Intermediate. Количество правильных ответов - {k}/15'})
        else:
            return render(request, 'testenglish/Результат.html',
                          {'result': f'Your english level - Advanced. Количество правильных ответов - {k}/15'})


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


def tests_by_level_result(request, level):
    if request.method == 'GET' and level == 1:
        k = 0
        order = 0
        questions = Question.objects.filter(category=1)

        for j in dict(request.GET)['answer']:
            order += 1
            for i in questions:
                if i.correct_answer == j and order == i.order:
                    k += 1
                    break

        return render(request, "testenglish/Результат.html", {'result': f'Ваш результат - {k}/15'})

    elif request.method == 'GET' and level == 2:
        k = 0
        order = 15
        questions = Question.objects.filter(category=2)

        for j in dict(request.GET)['answer']:
            order += 1
            for i in questions:
                if i.correct_answer == j and order == i.order:
                    k += 1
                    break
        return render(request, "testenglish/Результат.html", {'result': f'Ваш результат - {k}/15'})

    elif request.method == 'GET' and level == 3:
        k = 0
        order = 29
        questions = Question.objects.filter(category=3)

        for j in dict(request.GET)['answer']:
            order += 1
            for i in questions:
                if i.correct_answer == j and order == i.order:
                    k += 1
                    break
        return render(request, "testenglish/Результат.html", {'result': f'Ваш результат - {k}/15'})


def pageNotFound(request, exception):
    return render(request, 'testenglish/NotFound.html')
