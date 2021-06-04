from dataclasses import is_dataclass

from core.dice.model import Die


def test_should_be_a_dataclass():
    assert is_dataclass(Die)
