from django.urls import path
from .views import render_main_page, create_question

urlpatterns = [
    path('', render_main_page, name='render_main_page'),
    path('create_question', create_question, name='create_question')
]
