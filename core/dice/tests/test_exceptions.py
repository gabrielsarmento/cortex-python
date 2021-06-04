import pytest


@pytest.fixture
def die_exception():
    from core.dice.exceptions import DieException
    return DieException


@pytest.fixture
def die_faces_value_exception():
    from core.dice.exceptions import DieFacesValueException
    return DieFacesValueException


@pytest.fixture
def die_operation_exception():
    from core.dice.exceptions import DieOperationException
    return DieOperationException


def test_should_exists_a_die_base_exception():
    try:
        from core.dice.exceptions import DieException  # noqa
    except ImportError:
        pytest.fail('Cannot import DieException')


def test_die_exception_should_be_a_exception(die_exception):
    assert issubclass(die_exception, Exception)


def test_should_exists_a_die_faces_value_exception():
    try:
        from core.dice.exceptions import DieFacesValueException  # noqa
    except ImportError:
        pytest.fail('Cannot import DieFacesValueException')


def test_die_faces_value_exception_should_be_a_die_exception(
    die_exception,
    die_faces_value_exception
):
    assert issubclass(die_faces_value_exception, die_exception)


def test_should_exists_a_die_operation_exception():
    try:
        from core.dice.exceptions import DieOperationException  # noqa
    except ImportError:
        pytest.fail('Cannot import DieOperationException')


def test_die_operation_exception_should_be_a_die_exception(
    die_exception,
    die_operation_exception
):
    assert issubclass(die_operation_exception, die_exception)
