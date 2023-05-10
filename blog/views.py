from django.shortcuts import render, redirect
from django.contrib import messages
from .controllers import *
from .forms import *


def render_main_page(request):
    question_form = QuestionForm()
    answer_form = AnswerForm()
    questions = get_all_questions_with_answers()
    print(questions)
    for i in questions:
        print(f'{i} - object')
        print(f'{i.answer_set.all()} - answers')
        for answer in i.answer_set.all():
            pass

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

