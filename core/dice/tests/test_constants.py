from core.dice.constants import DIE_FACES_NUMBERS


def test_die_faces_numbers_must_be_valid():
    assert DIE_FACES_NUMBERS == [4, 6, 8, 10, 12]
