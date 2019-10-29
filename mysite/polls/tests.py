import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Question
#najpierw importy z bibliotek standardowych, potem z zainstalwanych rzeczy, na koniec z naszych plików
# Create your tests here.
#najlepiej do testów PyTest

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        # was_published_recently - return false for question whose pub_date is in the future
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently, False)
    def test_was_published_recently_with_recent_question(self):
        # was published recently - return true for question whose pub_date is recent
        time = timezone.now()
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently, True)
    def test_was_published_recently_with_old_question(self):
        # was published recently - return false for question whose pub_date is older
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently, False)
        # assert future_question.was_published_recently is False
        # w pythonie dla x = true nie sprawdzamy x == true tylko x is True bo wszystko w pythonie jest obiektem

#anotacje
def concatenate_numbers(a: int, b: int) -> str:
    return str(a) + str(b)
 #python zignoruje to a MyPy ma static type checker

def create_question(question_text, days):
    '''
    Ctreate question with given question text and pub_date
    that is 10 days from now +/-
    '''
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionDetailViewTests(TestCase):
    def test_question_published_in_future_visibility(self):
        future_question = create_question("test", days=2)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    def test_question_published_in_past_visibility(self):
        past_question = create_question("test", days=-2)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)