import pytest
import hypothesis.strategies as st
from hypothesis import assume, given, example, extra
from hypothesis.extra.django import TransactionTestCase, from_model
from people.models import Person, Course


def add(x, y):
    return x + y


person_st = from_model(Person)
course_st = from_model(Course, author=person_st)

@pytest.mark.transactional_db
class PersonTest(TransactionTestCase):


    # @pytest.mark.transactional_db
    @given(course_st.example(), person_st.example())
    def test_add(self):
        i = course_st.example()
        b = person_st.example()
        assert i.author == b

