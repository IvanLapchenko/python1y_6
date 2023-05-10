from .models import Question, Answer


def get_all_questions():
    return Question.objects.all()


def get_all_answers():
    return Answer.objects.all()


def get_all_questions_with_answers():
    return Question.objects.all().prefetch_related('answer_set')
