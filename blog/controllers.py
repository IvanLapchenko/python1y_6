from django.contrib import messages
from .models import Question, Answer, Category


def get_all_questions():
    return Question.objects.all()


def get_all_answers():
    return Answer.objects.all()


def get_all_questions_with_answers_for_category(category_id):
    return Question.objects.all().filter(category=int(category_id)).prefetch_related('answer_set')


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

