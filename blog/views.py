from django.shortcuts import render, redirect
from django.contrib import messages
from .controllers import *
from .forms import *
# TODO add function that crates answers


def render_main_page(request):
    category_id = request.GET.get('id')
    if category_id:
        questions = get_all_questions_with_answers_for_category(category_id)
    else:
        questions = get_all_questions_with_answers()
    question_form = QuestionForm()
    answer_form = AnswerForm()
    return render(request, 'main.html', context={'questions': questions,
                                                 'question_form': question_form,
                                                 'answer_form': answer_form})


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
