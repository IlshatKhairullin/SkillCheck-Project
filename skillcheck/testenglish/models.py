from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    parent = models.CharField(max_length=255)


class Test(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    type_test = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    complexity = models.CharField(max_length=255)
    category = Category()
    created_date = models.CharField(max_length=255)


class Question(models.Model):
    test = Test()
    text = models.TextField(blank=True)
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    answer4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)


class User(models.Model):
    user = models.CharField(max_length=255)
    test = Test()
    result = models.CharField(max_length=255)
