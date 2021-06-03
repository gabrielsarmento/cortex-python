from dataclasses import is_dataclass

import pytest
from unittest.mock import patch

from cortex.dice.exceptions import (
    DieFacesValueException,
    DieOperationException
)


@pytest.fixture
def die_class():
    from cortex.dice.model import Die

    return Die


@pytest.fixture
def allowed_faces_numbers():
    with patch(
        'cortex.dice.model.DIE_FACES_NUMBERS',
        [1]
    ) as mocked_constant:
        yield mocked_constant


def test_should_exist_a_die_class_at_die_module():
    try:
        from cortex.dice.model import Die  # noqa
    except ImportError:
        pytest.fail('Cannot import Die class')


def test_die_class_should_be_a_dataclass(die_class):
    assert is_dataclass(die_class)


def test_die_class_should_raise_exception_for_not_allowed_number_of_faces(
    die_class,
    allowed_faces_numbers
):
    with pytest.raises(DieFacesValueException):
        die_class(4)


def test_default_die_result_must_be_zero(die_class):
    assert die_class().result == 0


def test_after_roll_the_result_attribute_must_be_updated(die_class):
    die = die_class()
    result = die.roll()
    assert die.result == result


def test_default_die_number_of_faces_attribute_must_be_4(die_class):
    assert die_class().faces == 4


def test_die_is_hitch_property_should_return_true_when_result_is_1(die_class):
    die = die_class()
    die.result = 1
    assert die.is_hitch is True


def test_should_raise_die_operation_exception_when_try_to_step_up_on_last_lvl(
    die_class,
    allowed_faces_numbers
):
    die = die_class(1)
    with pytest.raises(DieOperationException):
        die.step_up()


def test_should_step_up_successfully_a_die(die_class):
    die = die_class()
    assert die.faces == 4
    die.step_up()
    assert die.faces == 6


def test_should_raise_die_operation_exception_when_try_to_step_down_first_lvl(
    die_class,
    allowed_faces_numbers
):
    die = die_class(1)
    with pytest.raises(DieOperationException):
        die.step_down()


def test_should_step_down_successfully_a_die(die_class):
    die = die_class(8)
    assert die.faces == 8
    die.step_down()
    assert die.faces == 6
