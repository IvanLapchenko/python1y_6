from django.shortcuts import render, redirect
from django.contrib import messages
from .controllers import *
from .forms import *
# TODO add function that crates answers


def render_main_page(request):
    category_id = request.GET.get('id')
    question_form = QuestionForm()
    answer_form = AnswerForm()
    questions = get_all_questions_with_answers_for_category(category_id)
    return render(request, 'main.html', context={'questions': questions,
                                                 'question_form': question_form,
                                                 'answer_form': answer_form})


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            print(request.user)
            question.author = request.user
            question.publish()
            messages.success(request, message='Question asked!')
        return redirect('/')


def render_categories_page(request):
    return render(request, 'categories.html', {'categories': get_all_categories()})
