from django.shortcuts import render, redirect
from django.contrib import messages
from .controllers import *
from .forms import *


def render_main_page(request):
    category_id = request.GET.get('id')
    if category_id:
        questions = get_all_questions_with_answers_for_category(category_id)
    else:
        questions = get_all_questions_with_answers()
    return render(request, 'main.html', context={'questions': questions})


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            create_question_with_success_message(form, request)
        else:
            messages.error(request, 'There was an error while adding question, check your data and try again.')
        return redirect('/')


def create_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            create_answer_with_success_message(form, request)
        else:
            messages.error(request, 'There was an error while adding answer, check your data and try again.')
        return redirect('/')


def render_categories_page(request):
    return render(request, 'categories.html', {'categories': get_all_categories()})


def render_question_page(request):
    question_id = request.GET.get('id')
    answer_form = AnswerForm()
    return render(request, 'question.html', {'question': get_question_by_id(question_id),
                                             'answers': get_answers_for_question(question_id),
                                             'answer_form': answer_form})


def edit_question(request, question_id):
    return edit_record(request, Question, QuestionForm, question_id)


def edit_answer(request, answer_id):
    return edit_record(request, Answer, AnswerForm, answer_id)


def delete_question(request, question_id):
    return delete_record(request, Question, question_id)


def delete_answer(request, answer_id):
    return delete_record(request, Answer, answer_id)


def user_questions(request):
    questions = get_all_questions_for_user(request.user)
    answers = get_all_answers_for_user(request.user)
    return render(request, 'user.html', {'questions': questions, 'answers': answers})


def search(request):
    search_query = request.GET.get('query')
    questions = get_questions_by_search_query(search_query)
    return render(request, 'main.html', {'questions': questions})


def ask_question(request):
    question_form = QuestionForm()
    return render(request, 'ask_question.html', {'question_form': question_form})
