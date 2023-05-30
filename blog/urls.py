from django.urls import path
from .views import render_main_page, create_question, render_categories_page, \
    create_answer, render_question_page, edit_question, edit_answer, user_questions, search, \
    ask_question

urlpatterns = [
    path('', render_main_page, name='render_main_page'),
    path('create_question', create_question, name='create_question'),
    path('create_answer', create_answer, name='create_answer'),
    path('categories', render_categories_page, name='render_categories_page'),
    path('question', render_question_page, name='render_question_page'),
    path('question/edit/<int:question_id>/', edit_question, name='edit_question'),
    path('answer/edit/<int:answer_id>/', edit_answer, name='edit_answer'),
    path('my_questions', user_questions, name='user_questions'),
    path('ask_question', ask_question, name='ask_question'),
    path('search', search, name='search'),
]
