from .models import Question, Answer, Category


def get_all_questions():
    return Question.objects.all()


def get_all_answers():
    return Answer.objects.all()


def get_all_questions_with_answers_for_category(category_id):
    return Question.objects.all().filter(category=int(category_id)).prefetch_related('answer_set')


def get_all_categories():
    return Category.objects.all()
