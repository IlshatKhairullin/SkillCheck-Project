from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=255)
    type_test = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    complexity = models.CharField(max_length=255)
    created_date = models.CharField(max_length=255)


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.PROTECT, null=True)
    text = models.TextField(blank=True)
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    answer4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    order = models.IntegerField(null=True)
    category = models.CharField(max_length=255, null=True)


class User(models.Model):
    user = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.PROTECT, null=True)
    result = models.CharField(max_length=255)
