# Create your tests here.
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

class QuestionMethodTests(TestCase):
    def test_was_published_recently_wish_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question=Question(pd=time)
        self.assertEqual(future_question.publishrec(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pd=time)
        self.assertEqual(old_question.publishrec(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pd=time)
        self.assertEqual(recent_question.publishrec(), True)


