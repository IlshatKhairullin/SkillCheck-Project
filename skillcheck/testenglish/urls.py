from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('test_yourself/', views.main_test, name='test_yourself'),
    path('help/', views.help_page, name='help_page'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('tests/', views.tests_page, name='tests_page'),
    path('tests/level-A', views.test_button_A, name='test_button_A'),
    path('tests/level-B', views.test_button_B, name='test_button_B'),
    path('tests/level-C', views.test_button_C, name='test_button_C'),
]
