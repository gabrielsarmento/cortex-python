from core.dice.model import Die
from core.dice.exceptions import DieFacesValueException

import pytest
from unittest import mock


@pytest.fixture
def mock_die_faces_numbers():
    with mock.patch(
        'core.dice.model.DIE_FACES_NUMBERS'
    ) as mocked_constant:
        yield mocked_constant


def test_should_raise_die_faces_value_exception_when_not_valid_faces(
    mock_die_faces_numbers
):

    with pytest.raises(DieFacesValueException):
        Die()
