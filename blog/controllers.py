from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import Question, Answer, Category


def get_all_questions():
    return Question.objects.all()


def get_all_answers():
    return Answer.objects.all()


def get_all_questions_with_answers_for_category(category_id):
    return Question.objects.all().filter(category=int(category_id)).prefetch_related('answer_set')


def get_question_by_id(question_id):
    return get_object_or_404(Question, pk=question_id)


def get_answers_for_question(question_id):
    return Answer.objects.all().filter(question=question_id)


def get_all_questions_with_answers():
    return Question.objects.all().prefetch_related('answer_set')


def get_all_categories():
    return Category.objects.all()


def create_question_with_success_message(form, request):
    question = form.save(commit=False)
    question.author = request.user
    question.publish()
    messages.success(request, message='Question asked!')


def create_answer_with_success_message(form, request):
    answer = form.save(commit=False)
    answer.author = request.user
    question_pk = request.POST.get('pk')
    question = Question.objects.get(pk=question_pk)
    answer.question = question
    answer.publish()
    messages.success(request, message='Question asked!')


def edit_record(request, model_class, form_class, record_id):
    record = get_object_or_404(model_class, pk=record_id)
    if request.method == 'POST':
        form = form_class(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = form_class(instance=record)
    return render(request, 'edit_record.html', {'form': form, 'model': record.__class__.__name__})
